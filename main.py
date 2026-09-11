# This is the main program.
# It connects the Student classes, data tools, analytics,
# and reporting functions into one terminal menu.


from models import Student
from data_tools import generate_data_file, load_students, export_report
from analytics import (
    class_average,
    highest,
    lowest,
    pass_rate,
    passing_students,
    make_grader,
    get_first_student
)
from reporting import environment_report, date_report


students = []


def display_menu():
    print("\n===== STUDENT ANALYTICS TOOLKIT =====")
    print("1. Generate sample data file")
    print("2. Load & clean records from file")
    print("3. View all students")
    print("4. Analyse")
    print("5. Filter students")
    print("6. Grade with a custom pass mark")
    print("7. Environment & date report")
    print("8. Export results to a file")
    print("9. Exit")


while True:
    display_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        generate_data_file()

    elif choice == "2":
        records = load_students()

        students = []

        for number, (name, score) in enumerate(records, start=1):
            student = Student(name, f"ST{number:03d}", score)
            students.append(student)

        print(f"{len(students)} student records loaded successfully.")

    elif choice == "3":
        if not students:
            print("No students loaded. Please load the records first.")
        else:
            print("\n===== ALL STUDENTS =====")

            for student in students:
                print(student)

    elif choice == "4":
        if not students:
            print("No students loaded. Please load the records first.")
        else:
            records = [(student.name, student.score) for student in students]

            average = class_average(records)
            top_student = highest(records)
            bottom_student = lowest(records)
            rate = pass_rate(records)

            print("\n===== CLASS ANALYSIS =====")
            print(f"Class Average: {average:.2f}%")
            print(f"Highest: {top_student[0]} - {top_student[1]}%")
            print(f"Lowest: {bottom_student[0]} - {bottom_student[1]}%")
            print(f"Pass Rate: {rate:.2f}%")

            print("\nPassing Students:")

            for name, score in passing_students(records):
                print(f"- {name}: {score}%")

    elif choice == "5":
        if not students:
            print("No students loaded. Please load the records first.")
        else:
            try:
                minimum_score = int(input("Enter minimum score to filter by: "))

                print(f"\nStudents with scores of {minimum_score}% or higher:")

                found = False

                for student in students:
                    if student.score >= minimum_score:
                        print(student)
                        found = True

                if not found:
                    print("No students matched that score.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "6":
        if not students:
            print("No students loaded. Please load the records first.")
        else:
            try:
                pass_mark = int(input("Enter custom pass mark: "))

                grader = make_grader(pass_mark)

                print(f"\nStudents passing with a {pass_mark}% pass mark:")

                for student in students:
                    result = "Pass" if grader(student.score) else "Fail"
                    print(f"{student.name}: {student.score}% - {result}")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "7":
        print(environment_report())
        print(date_report())

    elif choice == "8":
        if not students:
            print("No students loaded. Please load the records first.")
        else:
            records = [(student.name, student.score) for student in students]

            report = f"""
STUDENT ANALYTICS REPORT
========================

Number of Students: {len(students)}
Class Average: {class_average(records):.2f}%
Pass Rate: {pass_rate(records):.2f}%

Highest Student:
{highest(records)[0]} - {highest(records)[1]}%

Lowest Student:
{lowest(records)[0]} - {lowest(records)[1]}%

Passing Students:
"""

            for name, score in passing_students(records):
                report += f"- {name}: {score}%\n"

            export_report(report)

    elif choice == "9":
        print("Thank you for using the Student Analytics Toolkit.")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 9.")
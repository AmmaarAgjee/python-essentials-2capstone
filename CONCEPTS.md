# Python Essentials 2 Capstone - Concepts

## 1. Which module does each file draw on?

### models.py

The `models.py` file uses Object-Oriented Programming.

I created a `Student` class to represent a student. The class stores the student's name, student ID, and score. I also created an `HonoursStudent` class that inherits from the `Student` class.

Example:

```python
class Student:
    school_name = "Melsoft Academy"
    total_students = 0

    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score
        Student.total_students += 1

    def get_grade(self):
        if self.score >= 75:
            return "Distinction"
        elif self.score >= 50:
            return "Pass"
        else:
            return "Fail"

    def has_passed(self):
        return self.score >= 50

## 2. Why did I split the project into different files instead of putting everything into one big file?

I split the project into different files because I felt it would be easier to keep everything organised and know what each part of the program is responsible for.

For example, `models.py` deals with the student classes, while `data_tools.py` deals with creating, reading, and cleaning the data.

Having everything separated also makes it easier for me to find and change something when I need to, instead of having all my code in one big file.

def load_students():
    students = []

    try:
        with open("data/students.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                name = parts[0].strip().title()
                score = int(parts[1].strip())

                students.append((name, score))

        log_event("Loaded and cleaned student records.")
        return students

    except FileNotFoundError:
        print("Student data file not found. Generate the data first.")
        return []

## 3. What is the difference between a class and an object?

To me, a class is like a blueprint that tells the program what a student should have and what they can do.

An object is an actual student that I create using that blueprint.

For example, I can create a student like this:

```python
student = Student("John Smith", "ST001", 75)

def passing_students(students):
    for name, score in students:
        if score >= 50:
            yield (name, score)

## 4. What is the difference between a generator and a normal function?

A normal function gives me a result when I call it. A generator is a bit different because it uses `yield` to give me the results one at a time.

I used a generator in my project to get the students who passed:

```python
def passing_students(students):
    for name, score in students:
        if score >= 50:
            yield (name, score)

 ## 5. What is a closure?

A closure is basically a function that remembers a value from the function around it.

In my project, I used it for the custom pass mark. So if I give it a pass mark of 60, the function remembers that 60 when it checks the student's score.

For example:

```python
def make_grader(pass_mark):
    def grader(score):
        return score >= pass_mark

    return grader

## 6. What is the difference between "w" and "a" when working with files?

The main difference is that `"w"` writes to a file and `"a"` adds to the file without removing what was already there.

I used `"w"` when creating the student data file:

```python
with open("data/students.txt", "w") as file:
    file.write("John Smith, 75\n")

    ## 7. What was the hardest part of combining the four modules?

The hardest part for me was getting all the different files to work together properly.

Each file does something different, so I had to make sure that the data from one file could be used by another file.

I solved this by using `main.py` to connect everything together. I imported the classes and functions from the other files and then used them in the menu.

For example, in my `main.py` I imported functions and the `Student` class from my other files:

```python
from models import Student
from data_tools import generate_data_file, load_students
from analytics import class_average
from reporting import environment_report

This allowed the different parts of my project to work together through the main menu.

---

## Conclusion

This project helped me understand how different Python concepts can work together in one program.

I used classes and objects for the students, file handling for the student data, generators for finding passing students, closures for the custom pass mark, and `iter()` and `next()` for working with iterators.

Splitting the project into different files also helped me keep everything organised and made it easier to understand what each part of the program does. 
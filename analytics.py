# This file contains functions for analysing student data.
# It calculates class averages, highest and lowest scores,
# pass rates, and demonstrates generators, closures, and iterators.


def class_average(students):
    if not students:
        return 0

    total = sum(score for name, score in students)
    return total / len(students)


def highest(students):
    if not students:
        return None

    return max(students, key=lambda student: student[1])


def lowest(students):
    if not students:
        return None

    return min(students, key=lambda student: student[1])


def pass_rate(students):
    if not students:
        return 0

    passed = sum(1 for name, score in students if score >= 50)
    return (passed / len(students)) * 100


def passing_students(students):
    for name, score in students:
        if score >= 50:
            yield (name, score)


def make_grader(pass_mark):
    def grader(score):
        return score >= pass_mark

    return grader


def get_first_student(students):
    student_iterator = iter(students)

    try:
        return next(student_iterator)
    except StopIteration:
        return None
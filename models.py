# This file contains the Student and HonoursStudent classes.
# The Student class stores each student's name, ID, and score,
# and provides methods for calculating grades and checking passes.
# HonoursStudent inherits from Student and adds a research topic
# and a special Honours Distinction grade.

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

    def __str__(self):
        return f"{self.student_id} - {self.name}: {self.score}% ({self.get_grade()})"


class HonoursStudent(Student):
    def __init__(self, name, student_id, score, research_topic):
        super().__init__(name, student_id, score)
        self.research_topic = research_topic

    def get_grade(self):
        if self.score >= 75:
            return "Honours Distinction"
        return super().get_grade()
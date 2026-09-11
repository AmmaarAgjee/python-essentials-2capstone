# This file handles creating, reading, cleaning, exporting,
# and logging student data.

import random
from datetime import datetime


def generate_data_file():
    names = [
        " john smith ",
        "MARY JONES",
        "  peter brown",
        "sarah WILLIAMS ",
        "  david davis",
        "lisa miller ",
        "MICHAEL WILSON",
        "  amanda taylor "
    ]

    scores = [random.randint(35, 95) for _ in range(8)]

    with open("data/students.txt", "w") as file:
        for name, score in zip(names, scores):
            file.write(f" {name} , {score} \n")

    log_event("Generated sample student data.")
    print("Sample student data generated successfully.")


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


def export_report(text):
    with open("data/report.txt", "w") as file:
        file.write(text)

    log_event("Exported report to data/report.txt.")
    print("Report exported successfully.")


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("data/activity.log", "a") as file:
        file.write(f"[{timestamp}] {message}\n")
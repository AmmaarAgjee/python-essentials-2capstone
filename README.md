# python-essentials-2capstone
A Python terminal application for generating, cleaning, analysing, and reporting student data.
# Student Analytics Toolkit

The Student Analytics Toolkit is a Python terminal application that generates, cleans, analyses, and reports on student data. The project combines Python skills from Modules 1–4 into one application.

## Student Information

**Name:** Ammaar Agjee  
**Cohort:** Data Science 2026

## Features

The Student Analytics Toolkit can:

- Generate sample student data
- Load and clean student records from a file
- Create student objects using Object-Oriented Programming
- View all students
- Calculate the class average
- Find the highest-scoring student
- Find the lowest-scoring student
- Calculate the pass rate
- Filter students using a generator
- Grade students using a custom pass mark
- Use a closure to remember the custom pass mark
- Use iterators with `iter()` and `next()`
- Generate an environment report
- Generate a date report
- Export results to a file
- Record activity in a log file

## How To Run

1. Open the project folder in VS Code.

2. Open the VS Code terminal.

3. Run the program using:

```text
python main.py

## Project Structure

- `main.py` - Runs the main menu and connects all the different parts of the project.
- `models.py` - Contains the `Student` and `HonoursStudent` classes.
- `data_tools.py` - Creates, reads, cleans, and exports the student data and records activity in a log file.
- `analytics.py` - Handles the calculations, passing students, custom pass marks, generators, and closures.
- `reporting.py` - Creates reports about the computer environment and date information.
- `requirements.txt` - Lists any Python packages needed for the project.
- `README.md` - Explains the project and how to run it.
- `CONCEPTS.md` - Explains the Python concepts I used in the project.
- `.gitignore` - Stops files such as generated data and log files from being uploaded to GitHub.
- `data/` - Stores the student data, report, and activity log files.

## Concepts Demonstrated

This project helped me use different Python concepts that I learned during Python Essentials 2.

- **Object-Oriented Programming** - I used classes and objects to represent students.
- **Inheritance** - I used `HonoursStudent` to inherit from the `Student` class.
- **File Handling** - I used files to create, read, and export student data.
- **Data Cleaning** - I cleaned the student names and scores before using the data.
- **Generators** - I used `yield` to find students who passed.
- **Closures** - I used a closure for the custom pass mark.
- **Iterators** - I used `iter()` and `next()` to work with student records.
- **Exception Handling** - I used `try` and `except` to handle errors and bad input.
- **Modules** - I separated the project into different files so each part has its own job.

## Sample Output

Example of the program running in the terminal:

```text
=================================
 Student Analytics Toolkit
=================================

1. Generate sample data file
2. Load & clean records from file
3. View all students
4. Analyse
5. Filter students
6. Grade with a custom pass mark
7. Environment & date report
8. Export results to a file
9. Exit

Enter your choice: 4

Class Average: 68.50%
Highest Score: 92%
Lowest Score: 41%
Pass Rate: 75.00%
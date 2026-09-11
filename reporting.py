# This file creates reports about the computer environment
# and the current date.


import os
import platform
import calendar
from datetime import datetime


def environment_report():
    data_file = "data/students.txt"

    if os.path.exists(data_file):
        file_size = os.path.getsize(data_file)
        file_status = f"Found - {file_size} bytes"
    else:
        file_status = "Not found"

    report = f"""
ENVIRONMENT REPORT
------------------
Operating System: {platform.system()}
Python Version: {platform.python_version()}
Working Directory: {os.getcwd()}
Student Data File: {file_status}
"""

    return report


def date_report():
    today = datetime.now()
    current_year = today.year
    current_month = today.month

    future_date = datetime(current_year, 12, 31)
    days_until_future_date = (future_date - today).days

    month_name = calendar.month_name[current_month]
    days_in_month = calendar.monthrange(current_year, current_month)[1]

    report = f"""
DATE REPORT
-----------
Today's Date: {today.strftime("%A, %d %B %Y")}
Current Time: {today.strftime("%H:%M:%S")}
Current Month: {month_name}
Days in Current Month: {days_in_month}
Days Until 31 December: {days_until_future_date}
"""

    return report
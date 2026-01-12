import csv
from course import Course

def load_courses(filename):
    courses = []
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            courses.append(
                Course(
                    row["title"],
                    row["code"],
                    row["credits"],
                    row["prerequisite"]
                )
            )
    return courses


def load_history(filename):
    history = []
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            history.append((row["student_id"], row["course_code"]))
    return history



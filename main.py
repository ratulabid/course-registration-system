from student import Student
from file_handler import load_courses, load_history

def main():
    print("University Course Registration System\n")

    # Take student ID input
    student_id = input("Enter Student ID: ").strip()
    student = Student(student_id)

    # Load data
    courses = load_courses("courses.csv")
    history = load_history("history.csv")
    student.load_history(history)

    print("\n Available Courses:")
    for course in courses:
        print(course)

    # Dictionary for fast lookup
    course_dict = {course.code: course for course in courses}

    print("\n Register Courses (type course code, 'done' to finish):")

    while True:
        choice = input("Enter course code: ").strip().upper()

        if choice == "DONE":
            break

        if choice not in course_dict:
            print(" Invalid course code")
            continue

        student.register_course(course_dict[choice])

    print("\n Registration Summary")
    for course in student.registered_courses:
        print(course.code, "-", course.title)

    print("Total Credits:", student.total_credits)


if __name__ == "__main__":
    main()


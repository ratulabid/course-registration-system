class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.passed_courses = set()
        self.registered_courses = []
        self.total_credits = 0

    def load_history(self, history_data):
        for sid, course_code in history_data:
            if sid == self.student_id:
                self.passed_courses.add(course_code)

    def can_register(self, course):
        # Prerequisite check
        if course.prerequisite and course.prerequisite not in self.passed_courses:
            print(f" Cannot register {course.code}: prerequisite not passed")
            return False

        # Credit limit check
        if self.total_credits + course.credits > 15:
            print(f"Cannot register {course.code}: credit limit exceeded")
            return False

        return True

    def register_course(self, course):
        if self.can_register(course):
            self.registered_courses.append(course)
            self.total_credits += course.credits
            print(f"Registered: {course.code}")

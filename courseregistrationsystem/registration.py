from course import Course
from student import Student
from datetime import datetime


class Registration:
    def __init__(self, student: Student, course: Course, registration_time: datetime):
        super().__init__()
        self.student = student
        self.course = course
        self.registration_time = registration_time

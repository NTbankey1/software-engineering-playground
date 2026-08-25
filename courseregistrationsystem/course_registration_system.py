from course import Course
from typing import Dict
from student import Student
from typing import List
from registration import Registration
from datetime import datetime
class CourseRegistrationSystem:
    instance: CourseRegistrationSystem | None = None
    courses: Dict[str, Course] = {}
    students: Dict[int, Student]  = {}
    registrations: List[Registration] = []

    @staticmethod
    def get_instance() -> CourseRegistrationSystem:
        if CourseRegistrationSystem.instance is None:
            CourseRegistrationSystem.instance = CourseRegistrationSystem()
        return CourseRegistrationSystem.instance

    def add_course(self, course: Course) -> None:
        self.courses[course.get_code()] = course

    def add_student(self, student: Student) -> None:
        self.students[student.get_id()] = student

    def search_course(self, query: str) -> List[Course]:
        result = []
        for course in self.courses.values():
            if query in course.get_code() or query in course.get_name():
                result.append(course)
        return result

    def register_course(self, student: Student, course: Course) -> bool:
        if course.get_enrolled_students() < course.get_max_capacity():
            registration = Registration(student, course, datetime.now())
            self.registrations.append(registration)

            student.get_registered_courses().append(course)
            course.get_enrolled_students(course.get_enrolled_students() + 1)

            self._notify_observers(course)
            return True

        return False

    def get_registered_courses(self, student: Student) -> List[Course]:
        return student.get_registered_courses()

    def _notify_observers(self, course: Course) -> None:
        pass

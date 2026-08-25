from course_registration_system import CourseRegistrationSystem
from course import Course
from student import Student

class CourseRegistrationDemo:
    @staticmethod
    def run() -> None:
        registration_system = CourseRegistrationSystem.get_instance()

        course1 = Course("cs101","Introduction to programming","john doe", 50, 0)
        course2 = Course("cs201", "data structures and Algorithms", "jana smith", 30, 0)

        registration_system.add_course(course1)
        registration_system.add_course(course2)

        student1 = Student(1, "Alice", "alice@example.com", [])
        student2 = Student(2, "John", "john@example.com", [])

        registration_system.add_student(student1)
        registration_system.add_student(student2)

        search_results =registration_system.search_course("Cs")
        print("search Results")
        for course in search_results:
            print(f"{course.get_code()} - {course.get_name()}")

        registered1 = registration_system.register_course(student1, course1)
        registered2 = registration_system.register_course(student2, course2)
        registered3 = registration_system.register_course(student1, course2)

        print("registration results")
        print(f"stundet 1 - Course 1 {registered1}")
        print(f"studnet2 - Course 1 {registered2}")
        print(f"Student 1 - Course {registered3}")

        registered_course = registration_system.get_registered_courses(student1)
        print("Registered Courses for student 1")
        for course in registered_course:
            print(f"{course.get_code()} - {course.get_name()}")

if __name__ == " __main__ ":
    CourseRegistrationDemo.run()

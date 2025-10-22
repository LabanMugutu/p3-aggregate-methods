from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}  # store {enrollment: grade}

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    #  Aggregate Method 1: Count total courses a student is enrolled in
    def course_count(self):
        return len(self._enrollments)

    #  Add grade to a specific enrollment
    def add_grade(self, enrollment, grade):
        if isinstance(enrollment, Enrollment) and isinstance(grade, (int, float)):
            self._grades[enrollment] = grade
        else:
            raise TypeError("Invalid grade or enrollment")

    #  Aggregate Method 2: Average grade across all courses
    def aggregate_average_grade(self):
        if len(self._grades) == 0:
            return 0
        total = sum(self._grades.values())
        avg = total / len(self._grades)
        return avg


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    #  Aggregate Method 3: Count how many students are enrolled
    def student_count(self):
        return len(self._enrollments)


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    #  Aggregate Method 4: Count enrollments per day (class method)
    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

from typing import List, Dict
from enum import Enum
import uuid


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.dob: str = dob
        self.alive = AliveStatus.Alive

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def update_first_name(self, first_name: str):
        self.first_name = first_name

    def update_last_name(self, last_name: str):
        self.last_name = last_name

    def update_dob(self, dob: str):
        self.dob = dob

    def update_status(self, alive: AliveStatus):
        self.alive = alive


class Instructor(Person):
    def __init__(self, first_name: str, last_name: str, dob: str):
        self.instructor_id = f"Instructor_ + {uuid.uuid4()}"
        Person.__init__(self, first_name, last_name, dob, alive)


class Student(Person):
    def __init__(self, first_name: str, last_name: str, dob: str):
        self.student_id = f"Student_ + {uuid.uuid4()}"
        Person.__init__(self, first_name, last_name, dob, alive)


class ZipCodeStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: str):
        Student.__init__(self, first_name, last_name, dob, alive)


class PerkStudent(Student):
    def __init__(self, first_name: str, last_name: str, dob: str):
        Student.__init__(self, first_name, last_name, dob, alive)


class ClassRoom:
    def __init__(self):
        self.student: Dict[Student] = {}
        self.instructor: Dict[Instructor] = {}

    def add_instructor(self, instructor: Instructor):
        self.instructor.instructor_id = instructor

    def remove_instructor(self, instructor: Instructor):
        if instructor.instructor_id in self.instructor:
            del self.instructor.instructor_id

    def add_student(self, student: Student):
        self.student.student_id = student

    def remove_student(self, student):
        if student.student_id in self.student:
            del self.student[student.student_id]

    def print_instructors(self):
        for key, value in self.instructor.items():
            print(f"{key}: {value}")

    def print_students(self):
        for key, value in self.student.items():
            print(f"{key}: {value}")

from enum import Enum
import uuid


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        sel.dob = dob
        self.alive = alive

    def update_first_name(self):
        return self.first_name

    def update_last_name(self):
        return self.last_name

    def update_dob(self):
        return self.dob

    def update_status(self):
        return self.alive

class Instructor():
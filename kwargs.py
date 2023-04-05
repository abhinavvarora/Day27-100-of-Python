from imp import init_builtin
from mimetypes import init
from os import name
from typing import Self


class Student:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.marks = kwargs.get("marks")
        self.health = kwargs.get("health")


shashank = Student(name="Shashank")
print(shashank.name)

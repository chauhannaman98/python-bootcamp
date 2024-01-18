from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        #                                                       ^ Don't use mutable types in deafult values
        self.name = name
        self.grades = grades or []
    
    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob") # None in grades
rolf = Student("Rolf") # None in grades
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
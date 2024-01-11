"""Student class with student name and grades."""


class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
        self.id = None
    
    def set_id(self, id: int):
        if self.id == None:
            self.id = id
        
    def get_id(self) -> int:
        return self.id
    
    def get_grades(self):
        return self.grades
    
    def get_average_grade(self):
        total = 0
        leng = len(self.grades)
        if leng > 0:
            for i in self.grades:
                total += i[1]
            return total / leng
        else:
            return -1
        
    def add_grade(self, course, grade):
        self.grades.append(tuple([course, grade]))
        
    def __repr__(self) -> str:
        return self.name
"""Course class with name and grades."""


class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
        
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
        
    def add_grade(self, student, grade):
        self.grades.append(tuple([student, grade]))
        
    def __repr__(self):
        return self.name
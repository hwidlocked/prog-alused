"""School class which stores information about courses and students."""


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        
    def add_course(self, course):
        if not course in self.courses:
            self.courses.append(course)
            
    def add_student(self, student):
        if not student in self.students:
            student.set_id(len(self.students) + 1)
            self.students.append(student)
        
    def add_student_grade(self, student, course, grade: int):
        if student in self.students:
            if course in self.courses:
                student.add_grade(course, grade)
                course.add_grade(student, grade)
        
        
    def get_students(self):
        return self.students
    
    def get_courses(self):
        return self.courses
        
    def get_students_ordered_by_average_grade(self):
        lis = []
        for i in self.students:
            print(i.get_average_grade())
            lis.append([i, i.get_average_grade()])
        
        so = []
        for i in sorted(lis, key= lambda elem : elem[1], reverse=True):
            so.append(i[0])
        return so
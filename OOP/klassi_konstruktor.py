"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0
    pass


class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    pass


if __name__ == '__main__':
    # empty usage
    EmptyObj = Empty()

    # 3 x person usage
    Person1 = Person()
    Person1.firstname = "John"
    Person1.lastname = "Kork"
    Person1.age = 83
    
    Person2 = Person()
    Person2.firstname = "Peter"
    Person2.lastname = "Puu"
    Person2.age = 6
    
    Person3 = Person()
    Person3.firstname = "Markus"
    Person3.lastname = "Palm"
    Person3.age = 16
    # 3 x student usage
    Student1 = Student("John", "Kork", 83)
    Student2 = Student("Peter", "Puu", 6)
    Student3 = Student("Markus", "Palm", 16)
    
    pass

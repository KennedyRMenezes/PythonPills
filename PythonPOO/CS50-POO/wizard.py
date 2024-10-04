

# Same name attribute and copy of verification

'''
class Student:
    if not name:
        raise ValueError("Missing name")
    self.name = name
    self.house = house


class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject
'''

# Remove redundancy from classes by inherintance

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus") #Not a professor and not a student
student = Student("Harry", "Gryffindor")
professor = Professor("Serverus", "Defense Against the Dark Arts")
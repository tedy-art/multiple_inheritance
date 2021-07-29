class student1:
    def __init__(self):
        self.name= "Nani"
        self.age= 19

    def getName(self):
        return self.name

class Student2:
    def __init__(self):
        self.name="Ram"
        self.id= "15"

    def getName(self):
        return self.name

class students(student1,Student2):
    def __init__(self):
        student1.__init__(self)
        Student2.__init__(self)

    def getName(self):
        return self.name

stud=students()
print(stud.getName())
print(stud.id)
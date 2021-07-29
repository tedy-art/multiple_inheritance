#Multiple inheritance
class Mother:
    mothername=input(print("Enter ur mother name :"))
    def mother(self):
        print(self.mothername)

class Father:
    fathername=input(print("Enter ur father name :"))
    def father(self):
        print(self.fathername)

class son(Father,Mother):
    def Parents(self):
        print("Father :",self.fathername)
        print("Mother :",self.mothername)

s1=son()

s1.Parents()
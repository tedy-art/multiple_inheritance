# Performing Addition,Multiplication,Division using Multiple Inheritance

class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b
d = Derived()
print(d.Summation(1,2))
print(d.Multiplication(1,2))
print(d.Divide(1,2))
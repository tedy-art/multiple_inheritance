class A:
    demo1=input(print("First number is :"))
    def fun1(self):
        print(self.demo1)

class B:
    demo2=input(print("Second number is :"))
    def fun2(self):
        print(self.demo2)

class c (A,B):
    def fun3(self):
        print("Hey there, you are in the child class.//\\")
        print("First number :",self.demo1)
        print("Second number :",self.demo2)
c=c()

c.fun3()
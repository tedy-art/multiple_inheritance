class Car():
    def Benz(self):
        print("This is a Banz Car..🚗/")

class Bus():
    def Volvo(self):
        print("This is a Volvo Bus..🚌/")

class Bike():
    def Bmw(self):
        print("This is a Bmw bike..🏍/")

class Truck():
    def Eicher(self):
        print("This is a Eicher Truck..🚚/")

class Plane():
    def Indigo(self):
        print("This is a Indigo plane..✈/")

class Transport(Car,Bus,Bike,Truck,Plane):
    def Main(self):
        print("This is the main class..🚦/")

B=Transport()
B.Benz()
B.Volvo()
B.Bmw()
B.Eicher()
B.Indigo()
B.Main()
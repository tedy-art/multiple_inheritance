class Cars:
    def __init__(self,CarName,CarModel):
        self.name=CarName
        self.model=CarModel

    def showName(self):
        print(self.name)

    def showModel(self):
        print(self.model)

class Ids:
    def __init__(self,CarId):
        self.CarId=CarId

    def getId(self):
        return self.CarId

class Main(Cars,Ids):
    def __init__(self,name,model,id):
        Cars.__init__(self,name,model)
        Ids.__init__(self,id)

Main1=Main("Swift",500,1)
Main1.showName()
Main1.showModel()
print(Main1.getId())
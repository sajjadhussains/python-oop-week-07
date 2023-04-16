class Bike:
    def __init__(self,driver,rate) -> None:
        self.rate=rate
        self.driver=driver
    def get_fare(self,distance):
        return self.rate*distance

class Car:
    def __init__(self,driver,rate) -> None:
        self.rate=rate
        self.driver=driver
    def get_fare(self,distance):
         return self.rate * distance

class Cng:
    def __init__(self,driver,rate) -> None:
        self.driver=driver
        self.rate=rate
    def get_fare(self,distance):
        return self.rate*distance
    
b1=Bike('masud',5)
c1=Car('mahbub',10)
g1=Cng('shovon',15)
customers=[14,18,26]

for distance in customers:
    print(b1.get_fare(distance))
    print(c1.get_fare(distance))
    print(g1.get_fare(distance))
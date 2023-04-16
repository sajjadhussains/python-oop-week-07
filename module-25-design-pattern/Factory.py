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
    
def Factory(vehicle_type):
    vehicle={
        'car':Car,
        'bike':Bike,
        'cng':Cng
    }
    return vehicle[vehicle_type]()
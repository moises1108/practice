class Parking():
    def __init__(self,pSize):
        self.pSize = pSize
        self.available = pSize
        self.cars = []

    def registerCar(self,car):
        if self.checkAvailability(car):
            if car.plate in self.cars:
                self.cars.remove(car.plate)
                self.available += car.cSize
                print(f"Thanks for your stay {car.plate}")
            else:
                self.available -= car.cSize
                self.cars.append(car.plate)
                print(f"Welcome to our parking {car.plate}")
                print(f"Remaining spots:{self.available}")
        else:
            print('Not enough space - please come later')
    
    def checkAvailability(self,car):
        if self.pSize < car.cSize:
            return False
        else:
            return True
    
class Car():
    def __init__(self, carType, plate):
        self.carType = carType
        self.plate = plate
        if self.carType == 'small':
            self.cSize = 1
        elif self.carType == 'medium':
            self.cSize = 2
        if self.carType == 'large':
            self.cSize = 3    
            
park = Parking(100)
car1 = Car('medium','AAA111')
car2 = Car('small','AAA112')
car3 = Car('medium','AAA113')
car4 = Car('medium','AAA114')
car5 = Car('large','AAA115')
car6 = Car('large','AAA116')
car7 = Car('medium','AAA17')

park.registerCar(car1)
print(park.cars)
park.registerCar(car2)
print(park.cars)
park.registerCar(car3)
print(park.cars)
park.registerCar(car4)
print(park.cars)
park.registerCar(car3)
print(park.cars)
park.registerCar(car2)
print(park.cars)
park.registerCar(car1)
print(park.cars)
park.registerCar(car5)
print(park.cars)
park.registerCar(car6)
print(park.cars)
park.registerCar(car6)
print(park.cars)
park.registerCar(car7)
print(park.cars)


    
    

        
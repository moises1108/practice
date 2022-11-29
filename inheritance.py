# class Bronze():
#     def __init__(self):
#         self.name = 'Bronze'
#         self.benefits = ['Free coffee']

#     def iAm(self):
#         return self.name
    
#     def listBenefits(self):
#         return self.benefits

# class Silver(Bronze):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Silver'

#     def iAm(self):
#         return self.name

# B1 = Bronze()
# S1 = Silver()

# print(B1.iAm())
# print(B1.listBenefits())
# print(S1.iAm())
# print(S1.listBenefits())


class Car():
    def __init__(self,capacity):
        self.capacity = capacity
        self.cType = 'Normal'
    
    def ride(self):
        return 'normal ride'
    

class Lux(Car):
    def __init__(self,capacity):
        super().__init__(capacity) #python 3
        # super(ChildB, self).__init__() # python2
        self.cType = 'Lux'
    
    def ride_style(self):
        return 'ride with style'

c1 = Car(4)
l1 = Lux(5)

print(c1.capacity)
print(c1.cType)
print(c1.ride())
print(l1.capacity)
print(l1.cType)
print(l1.ride())
print(l1.ride_style())
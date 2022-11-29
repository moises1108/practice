class Person():
    def __init__(self, name= "Empty name", age = 0):
        self.name = name
        self.age = age
        self.gender = "male"

    def action(self):
        print("HELLO I AM A PERSON")

class P2(Person):
    pass

class P3(Person):
    def __init__(self, name): #OVERRIDES the Parent INIT
        self.name = name

class P4(Person):
    def __init__(self):
        super().__init__()

# p1 = Person("PersonParent",10)
# print(p1.name, p1.age, p1.gender)
# p1.action()

# p2 = P2("P2")
# print(p2.name, p2.age, p2.gender)
# p2.action()

# p3 = P3("P3")
# print(p3.name)
# # print(p3.name, p3.age, p3.gender)
# # p3.action()

p4 = P4()
print(p4.name)
print(p4.name, p4.age, p4.gender)
p4.action()
    
    
    
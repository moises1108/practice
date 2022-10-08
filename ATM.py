# Class: Person, ATM
# Person (VIP and Normal) > Balance, if VIP when depositing get 10% extra
# ATM > Check Balance, Withdraw, Deposit, cross ATM check, Record transactions


class Person():
    def __init__(self, ID_P, isVIP):
        self.ID_P = ID_P
        self.isVIP = isVIP
    
class ATM():
    def __init__(self, ID_A):
        self.ID_A = ID_A
        self.history = {} # {[ID_P:['action': 200]]}
        self.balances = {} # {ID_P:xxxx}

    def log_decorator(func):
        def wrapper(self,*args, **kwargs): # Need to pass self, which is the instance
            # print(func.__name__) gives me the function name
            # print(self.history)
            if func.__name__ == 'checkBalance':
                self.history[args[0]] = self.history.get(args[0],[]) + [func.__name__]
            else:
                self.history[args[0]] = self.history.get(args[0],[]) + [(func.__name__,args[1])]
            return func(self,*args, **kwargs) # If I do not include 'return' the orig function returns NONE
            # print(self.history)
        return wrapper

    @log_decorator
    def deposit(self, ID_P, amount):
        self.balances[ID_P] = self.balances.get(ID_P,0) + amount
    
    @log_decorator
    def withdraw(self, ID_P, amount):
        self.balances[ID_P] = self.balances.get(ID_P,0) - amount

    @log_decorator
    def checkBalance(self, ID_P):
        return self.balances[ID_P]

    def checkHistory(self,ID_P):
        return self.history[ID_P]

    def checkAllHistory(self):
        return self.history

'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
'''

moises = Person(1,False)
testATM = ATM(5)
testATM.deposit(1,100)
testATM.deposit(1,200)
print(testATM.checkBalance(1))
testATM.withdraw(1,20)
print(testATM.checkBalance(1))
print(testATM.checkHistory(1))
print(testATM.checkAllHistory())
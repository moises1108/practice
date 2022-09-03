class Security():
    def __init__(self,ticker):
        self.ticker = ticker

class Wallet():
    # why was this causing moises to have the same portfolio as Joe?
    # def __init__(self, name, balance=0,portfolio={}):
    #     self.name = name
    #     self.balance = balance
    #     self.portfolio = portfolio
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.portfolio = {}


    
    # Initial Setup: deposit, withdraw, checkBalance independent to transaction
    def depositMoney(self, amount):
        self.balance += amount
        return print(f"Your balance is {self.balance}")
    def withdrawMoney(self,amount):
        if amount > self.balance:
            return print(f"Not enough balance. You need {amount-self.balance} more")
        self.balance -= amount
        return print(f"Sucessfully withdrawn: Remaining balance: {self.balance}")
    def checkBalance(self):
        return print(f"your balance is: {self.balance}")
    # Porfolio interaction
    def checkPortfolio(self):
        return print(f"Owner: {self.name} Portfolio:{self.portfolio}")

    def modifyPort(self, security, quantity):
        # print(f"LOGS: modifying portfolio before successfull trade. Current Port for {self.name} is {self.portfolio}")
        self.portfolio[security] = self.portfolio.get(security,0) + quantity
        # print(f"LOGS: modifying portfolio before successfull trade. Current Port for {self.name} is {self.portfolio}")

    
    def transactPort(self, action, security, exchange, quantity):
        exchange.transactExchange(self, action, security, quantity)        



class Exchange():
    def __init__(self, region): #{'AAPL':[[bids],[asks]]}
        self.region = region #EMEA, AMER, APAC
        self.securities = {}
        return print(f"Exchange created with region: {region}")
    
    def transactExchange(self, name, action, security, quantity):
        if action == 'buy' and not self.securityInExchange(security,action):
            self.securities[security][0].append(quantity)
            return print('You are trying to buy but there are no asks, so no transaction was made',self.securities)

        elif action == 'buy' and self.securityInExchange(security,action):
            toBeFilled = quantity
            while toBeFilled > 0 and len(self.securities[security][1])>0:
                lastAskQty = self.securities[security][1].pop()
                if lastAskQty <= toBeFilled:
                    toBeFilled -= lastAskQty
                    print(f"1 trade filled of qty{lastAskQty}.Remaining:{toBeFilled}")
                else:
                    remaining = lastAskQty - toBeFilled
                    toBeFilled = 0
                    # print(f"To be filled:{toBeFilled}, lastQty:{lastAskQty},Remaining appended:{remaining}")
                    self.securities[security][1].append(remaining)
            if toBeFilled != 0:
                print(f"filled:{quantity-toBeFilled}/{quantity}")
            else:
                print(f"Order of {quantity} completely filled")    
            name.modifyPort(security,quantity-toBeFilled)
        elif action == 'sell' and not self.securityInExchange(security,action):
            self.securities[security][1].append(quantity)
            return print('You are trying to sell but there are no bids',self.securities)

        elif action == 'sell' and self.securityInExchange(security,action):
            toBeFilled = quantity
            while toBeFilled > 0 and len(self.securities[security][0])>0:
                lastAskQty = self.securities[security][0].pop()
                if lastAskQty <= toBeFilled:
                    toBeFilled -= lastAskQty
                    print(f"1 trade filled of qty{lastAskQty}.Remaining:{toBeFilled}")
                else:
                    remaining = lastAskQty - toBeFilled
                    toBeFilled = 0
                    print(f"To be filled:{toBeFilled}, lastQty:{lastAskQty},Remaining appended:{remaining}")
                    self.securities[security][0].append(remaining)   
            name.modifyPort(security,quantity)
             
        else:
            return print("Please 'Buy' or 'Sell'")

    def securityInExchange(self,security,action):
        if security in self.securities:
            if action =='buy':
                return len(self.securities[security][1])>0
            else: #check for non buy/sells done on transactExchange()
                return len(self.securities[security][0])>0
        else:
            self.securities[security] = [[],[]] #initialise dictionary
            return False    



EMEA = Exchange('EMEA')
moises = Wallet('moises')
joe = Wallet('joe')
mike = Wallet('mike')
# moises.depositMoney(1000)
# moises.checkPortfolio()
moises.transactPort('sell','AAPL',EMEA,10)
moises.transactPort('sell','AAPL',EMEA,14)
moises.transactPort('sell','AAPL',EMEA,13)
joe.transactPort('buy','AAPL',EMEA,30)
joe.transactPort('buy','AAPL',EMEA,20)

moises.checkPortfolio()
joe.checkPortfolio()




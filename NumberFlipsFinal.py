a1 = [1,2,3,5] # 11
a2 = [2,3,7,3]
#    [1,1,4,2]
t1 = 16 #1 

# get cur sum of a1
# create a list of gains from flips
    # sort it in descending order
# main: while cursum < t flip

class minNumFlips():
    def __init__(self, a1, a2, t):
        self.a1 = a1
        self.a2 = a2
        self.t = t
        self.sumA1 = 0
        self.gains = []
        self.flips = 0
    
    def solveForFlips(self):
        self.sumOfa1()
        self.createGains()
        while self.sumA1 < self.t:
            self.sumA1 += self.gains.pop()
            self.flips += 1
        return self.flips

    
    def sumOfa1(self):
        self.sumA1 = sum(self.a1)
        
    def createGains(self):
        for i in range(len(self.a1)):
            self.gains.append(self.a2[i] - self.a1[i])
        self.gains.sort()

solution = minNumFlips(a1,a2,t1)
print(solution.solveForFlips())

    
    
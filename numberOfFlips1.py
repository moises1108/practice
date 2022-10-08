a1 = [1,2,3,5] # 11
a2 = [2,3,7,3]
t1 = 15 #1 

class minNumberOfFlips():
    def __init__(self,array1, array2, target):
        self.array1 = array1
        self.array2 = array2
        self.target = target
        self.gains = []
        self.sumArray = 0
        self.totalFlips = 0
    
    def findMinFlips(self):
        self.createGains(self.array1,self.array2,self.gains)
        self.sortArray(self.gains)
        self.sumArray = self.sumOfArray(self.array1)
        difference = self.target - self.sumArray
        while difference > 0:
            print(difference)
            difference -= self.gains.pop()
            self.totalFlips += 1
        return self.totalFlips
        
    def createGains(self,a1,a2,gains):
        for i in range(len(a1)):
            gains.append(a2[i] - a1[i])
            
    def sortArray(self,a):
        a.sort()

    def sumOfArray(self,a):
        return sum(a)

testing1 = minNumberOfFlips(a1,a2,t1)
print(testing1.findMinFlips())


# create an array with the gains for each index flipped
# sort the array
# check the sum of array a 
# start flipping from highest gain to lowest gain and check if I hit the target


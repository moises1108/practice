# Cinema - capacity, booking system

class Cinema():
    def __init__(self, rows, cols):
        self.capacity = rows*cols
        self.rows = rows
        self.cols = cols
        self.graph = []
        self.buildGraph(self.rows, self.cols)
    
    def buildGraph(self,rows,cols):
        self.graph = [[0 for i in range(cols)] for i in range(rows)]

    def checkGraph(self):
        for row in self.graph:
            print(row)

    def bookSeat(self,r,c):
        if self.graph[r][c] != 1:
            self.graph[r][c] = 1
            self.capacity -= 1
        else:
            return print('seat taken')


c = Cinema(5,4)
print(c.capacity)
c.bookSeat(1,2)
c.checkGraph()
c.bookSeat(1,2)
print(c.capacity)
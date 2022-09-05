class Tube():
    pass

class Underground():
    journeys = {} # (station1,station2):[4,5,2,3] key is a tuple, and time taken between 2 stations is a list of time taken
    onTube = {} # UUID: [StartingStation,startTime]
    def __init__(self):
        pass
    
    def journey(self, UUID, station, time):
        if UUID in Underground.onTube:
            self.endJourney(UUID,station,time)
        else:
            self.startJourney(UUID,station,time)
    
    def startJourney(self, UUID, startStation,startTime):
        Underground.onTube[UUID] = [startStation,startTime]

    def endJourney(self,UUID,endStation,endTime):
        journeysKey = (Underground.onTube[UUID][0],endStation)
        timeTaken = endTime - Underground.onTube[UUID][1]
        Underground.journeys[journeysKey] = Underground.journeys.get(journeysKey,[])+[timeTaken]
        del Underground.onTube[UUID]


TFL = Underground()
TFL.journey(100, 'Holborn', 1)
TFL.journey(101, 'Bank', 2)
TFL.journey(100, 'Paul',5)
TFL.journey(101, 'Mile', 10)

print(TFL.journeys)
print(TFL.onTube)





    

    


class Person():
    def __init__(self):
        pass



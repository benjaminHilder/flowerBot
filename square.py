class Square:
    def __init__(self):
        self.posInList = None
        self.realSquare = None

        self.name = ""
        self.ID = 0
        self.landType = ""
        self.harvestTime = 60
        self.harvestClock = 0

        self.height = 0
        self.width = 0

        self.centerPoint = [0,0]

        self.leftPoint = [0,0]
        self.topPoint = [0,0]
        self.rightPoint = [0,0]
        self.bottomPoint = [0,0]

        self.innerLeft = [0,0]
        self.innerTop = [0,0]
        self.innerRight = [0,0]
        self.innerBottom = [0,0]

        self.colour = (0,255,255)
        self.thickness = thickness=3

    def setPoints(self, point1, point2, point3, point4):

        self.leftPoint = point1
        self.topPoint = point2
        self.rightPoint = point3
        self.bottomPoint = point4

 
    #self determine which point is left, top, right or bottom
    """ def setPositioning(self, point1, point2, point3, point4):
        pointList = [point1, point2, point3, point4]

        

        self.lowestX = min(point1.x, point2.x, point3.x, point4.x)
        self.lowestY = min(point1.y, point2.y, point3.y, point4.y)
        self.highestX = max(point1.x, point2.x, point3.x, point4.x)
        self.highestY = max(point1.y, point2.y, point3.y, point4.y)

        #LowHighList = [lowestX, lowestY, highestX, highestY]
        getPoint(self.highestY)
        

        setPoint(self, pointList, lowestX, self.leftPoint)
        setPoint(self, pointList, highestY, self.topPoint)
        setPoint(self, pointList, highestX, self.rightPoint)
        setPoint(self, pointList, lowestY, self.bottomPoint)

    def returnMinXVar(pointList):
        minVal = min(pointList[0][0],pointList[1][0],
                     pointList[2][0],pointList[3][0])
        if 
    def returnMinYVar():
        pass
    def returnMaxXVar():
        pass
    def returnMaxYVar():
        pass
 """

""" def getPoint(self, point):
    if point == 1:
        return self.point1
    if point == 2:
        return self.point2
    if point == 3:
        return self.point3
    if point == 4:
        return self.point4
 """
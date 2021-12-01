from io import DEFAULT_BUFFER_SIZE
from sys import _debugmallocstats, exec_prefix, flags
from PyQt5.QtGui import QPainter
#from enb_bot.image_bot.recorder import OUTPUT_FILENAME
from square import Square
import pyautogui
import time
import win32api
from enum import Enum
import cv2 as cv
import numpy as np
from time import sleep
from PIL import Image
from math import sqrt
import os
import time
from threading import Timer

script_dir = os.path.dirname(__file__)

squareList = []
baseSquare = Square()
newSqaure = Square()
BLTR_BOARDER = 0
TLBR_BOARDER = 0




blank = np.zeros((1080,1920,3), dtype='uint8')

#wincap = WindowCapture()
class hudArea(Enum):
    bag    = 1
    select = 2
    shovel = 3
    plant  = 4
    water  = 5
    scissor= 6
class hudAction(Enum):
    selectLand = 1
    tillLand = 2
    plantFlower = 3
    waterLand = 4
    cutPlant = 5
class bagArea(Enum):
    map = 1
    inventory = 2
    flowers = 3
    exit = 4
class flowerArea(Enum):
    tile1 = 1
    tile2 = 2
    tile3 = 3
    tile4 = 4
    tile5 = 5
    tile6 = 6
    tile7 = 7
    tile8 = 8
    tile9 = 9
    tile10 = 10
    tile11 = 11
    tile12 = 12
    skipToStart = 13
    skipToEnd = 14
    skipForward = 15
    skipBackward= 16
    rarity = 17
    land = 18
    planted = 19
    network = 20
    sort = 21
    scending = 22
 
class SquarePos(Enum):
    top_left = 1
    top_right = 2
    bottom_right = 3
    bottom_left = 4

def main():
    countdownTimer()
    baseSquare.realSquare = True
    createDefaultSquare2(baseSquare)
    squareList.append(baseSquare)
    #squareList.append(newSqaure)
    #try:
        #while True:
            #checkForHarvests(60)
    #except KeyboardInterrupt:
        #pass



    #addSqaure(baseSquare, SquarePos.top_left, (255,0,255))

    #addSqaure(baseSquare, SquarePos.top_right, (255,0,255))

    #addSqaure(baseSquare, SquarePos.bottom_right, (255,0,255))

    #addSqaure(SquarePos.bottom_right, baseSquare,  baseSquare, True, (255,0,255))
    
    #addMultipleSqauresWithFakes(SquarePos.bottom_left, baseSquare, 10, (255,0,255))
    #addMultipleSqaures(SquarePos.bottom_right, baseSquare, 10, (255,0,255))
    #addMultipleSqauresWithFakes(SquarePos.top_right, baseSquare, 5, (255,0,255))
    #addMultipleSqauresWithFakes(SquarePos.top_right, baseSquare, 5, (255,0,255))

    
    #drawDebug
    #drawDiamonds(blank)
    #drawDiamond(blank, baseSquare.leftPoint, baseSquare.topPoint, baseSquare.rightPoint, baseSquare.bottomPoint,  (166, 107, 208), thickness=1)
    #drawDiamond(blank, newSqaure.leftPoint, newSqaure.topPoint, newSqaure.rightPoint, newSqaure.bottomPoint, (68,190,255),  thickness=1)
    #cv.imshow('1 sqaure', blank)
    #hudClick(hudArea.bag)
    #hudClick(hudArea.select,0.01)
    #hudClick(hudArea.shovel, 1)
    #hudClick(hudArea.plant, 0.0001)
    #hudClick(hudArea.water)
    #hudClick(hudArea.scissor)
#
    #bagClick(bagArea.map)
    #bagClick(bagArea.inventory)
#
    #bagClick(bagArea.flowers)
    #flowerMenuClick(flowerArea.tile1)
    #flowerMenuClick(flowerArea.tile2)
    #flowerMenuClick(flowerArea.tile3)
    #flowerMenuClick(flowerArea.tile4)
    #flowerMenuClick(flowerArea.tile5)
    #flowerMenuClick(flowerArea.tile6)
    #flowerMenuClick(flowerArea.tile7)
    #flowerMenuClick(flowerArea.tile8)
    #flowerMenuClick(flowerArea.tile9)
    #flowerMenuClick(flowerArea.tile10)
    #flowerMenuClick(flowerArea.tile11)
    #flowerMenuClick(flowerArea.tile12)
#
    #flowerMenuClick(flowerArea.rarity)
    #flowerMenuClick(flowerArea.land)
    #flowerMenuClick(flowerArea.planted)
    #flowerMenuClick(flowerArea.network)
    #flowerMenuClick(flowerArea.sort)
    #flowerMenuClick(flowerArea.scending)
#
    #flowerMenuClick(flowerArea.skipForward)
    #flowerMenuClick(flowerArea.skipBackward)
    #flowerMenuClick(flowerArea.skipToEnd)
    #flowerMenuClick(flowerArea.skipToStart)
    #bagClick(bagArea.exit)
    #
#
    #hudCommands(hudAction.selectLand, baseSquare, 1)
    #hudCommands(hudAction.tillLand, baseSquare, 1)
    ##hudCommands(hudAction.plantFlower, baseSquare, flowerArea.tile1, 2)
    #hudCommands(hudAction.waterLand, baseSquare, 1)
    #hudCommands(hudAction.cutPlant, baseSquare, 1)
    

    #bagClick(bagArea.exit)
    

    #print (squareList[0].leftPoint[0])
    cv.waitKey(0)
    #for i, sqaure in enumerate(squareList):
        #if squareList[i].realSquare == True:
                #moveClickSquare(squareList[i], 1)
    #for i, sqaure in enumerate(squareList):
         #moveClick(squareList[i].rightPoint[0],squareList[i].rightPoint[1], 1)
         #moveClick(squareList[i].topPoint[0],squareList[i].topPoint[1], 1)
         #moveClick(squareList[i].leftPoint[0],squareList[i].leftPoint[1], 1)
        # moveClick(squareList[i].bottomPoint[0],squareList[i].bottomPoint[1], 1)
    #moveClick(squareList[0].rightPoint[0],squareList[0].rightPoint[1], 1) 
    #moveClick(squareList[0].topPoint[0],squareList[0].topPoint[1], 1)
    #moveClick(squareList[0].leftPoint[0],squareList[0].leftPoint[1], 1)
    #moveClick(squareList[0].bottomPoint[0],squareList[0].bottomPoint[1], 1)

    #if cv.waitKey(1) == ord('q'):
        #cv.destroyAllWindows
        #break


def hudClick(hudCommand, time=0.2):
    #bag    = w 120 h 970
    if hudCommand == hudArea.bag:
        moveClick(120, 970, time)
    #select = w 620 h 970
    elif hudCommand == hudArea.select:
        moveClick(620, 970, time)
    #shovel = w 720 h 970
    elif hudCommand == hudArea.shovel:
        moveClick(720, 970, time)
    #plant  = w 810 h 970
    elif hudCommand == hudArea.plant:
        moveClick(810, 970, time)
    #water  = w 910 h 970
    elif hudCommand == hudArea.water:
        moveClick(910, 970, time)
    #cut    = w 990 h 970
    elif hudCommand == hudArea.scissor:
        moveClick(990, 970, time)

def hudCommands(hudOrder, square=None, flower=None, time =0.2):
    if hudOrder == hudAction.selectLand:
        hudClick(hudArea.select)
        moveClickSquare(square, time)
    if hudOrder == hudAction.tillLand:
        hudClick(hudArea.shovel)
        moveClickSquare(square, time)

    if hudOrder == hudAction.plantFlower:
        hudClick(hudArea.plant)
        moveClickSquare(square)
        plantingMenuClick(flower,time)

        moveClickSquare(square)
    if hudOrder == hudAction.waterLand:
        hudClick(hudArea.water)
        moveClickSquare(square, time)
    if hudOrder == hudAction.cutPlant:
        hudClick(hudArea.scissor)
        moveClickSquare(square, time)


def bagClick(bagCommand, time=0.2):
    if bagCommand == bagArea.map:
        moveClick(725, 317, time)
    if bagCommand == bagArea.inventory:
        moveClick(935, 316, time)
    if bagCommand == bagArea.flowers:
        moveClick(1148, 318, time)
    if bagCommand == bagArea.exit:
        moveClick(1277, 319, time)

def flowerMenuClick(flowerCommand, time=0.2):
    if flowerCommand == flowerArea.tile1:
        moveClick(720, 420, time)
    if flowerCommand == flowerArea.tile2:
        moveClick(920, 420, time)
    if flowerCommand == flowerArea.tile3:
        moveClick(1220, 420, time)

    if flowerCommand == flowerArea.tile4:
        moveClick(720, 520, time)
    if flowerCommand == flowerArea.tile5:
        moveClick(920, 520, time)
    if flowerCommand == flowerArea.tile6:
        moveClick(1220, 520, time)

    if flowerCommand == flowerArea.tile7:
        moveClick(720, 620, time)
    if flowerCommand == flowerArea.tile8:
        moveClick(920, 620, time)
    if flowerCommand == flowerArea.tile9:
        moveClick(1220, 620, time)

    if flowerCommand == flowerArea.tile10:
        moveClick(720, 720, time)
    if flowerCommand == flowerArea.tile11:
        moveClick(920, 720, time)
    if flowerCommand == flowerArea.tile12:
        moveClick(1220, 720, time)

    if flowerCommand == flowerArea.skipToStart:
        moveClick(635, 787, time)
    if flowerCommand == flowerArea.skipForward:
        moveClick(1260, 787, time)
    if flowerCommand == flowerArea.skipBackward:
        moveClick(653, 787, time)
    if flowerCommand == flowerArea.skipToEnd:
        moveClick(1288, 787, time)

    if flowerCommand == flowerArea.rarity:
        moveClick(660, 360, time)
    if flowerCommand == flowerArea.land:
        moveClick(760, 360, time)
    if flowerCommand == flowerArea.planted:
        moveClick(860, 360, time)
    if flowerCommand == flowerArea.network:
        moveClick(960, 360, time)
    if flowerCommand == flowerArea.sort:
        moveClick(1130, 360, time)
    if flowerCommand == flowerArea.scending:
        moveClick(1230, 360, time)

def plantingMenuClick(plantingCommand, time):
    if plantingCommand == flowerArea.tile1:
        moveClick(690, 470, time)
    if plantingCommand == flowerArea.tile2:
        moveClick(880, 470, time)
    if plantingCommand == flowerArea.tile3:
        moveClick(1049, 470, time)
    if plantingCommand == flowerArea.tile4:
        moveClick(1195, 470, time)

    if plantingCommand == flowerArea.tile5:
        moveClick(690, 562, time)
    if plantingCommand == flowerArea.tile6:
        moveClick(880, 562, time)
    if plantingCommand == flowerArea.tile7:
        moveClick(1049, 562, time)
    if plantingCommand == flowerArea.tile8:
        moveClick(1195, 562, time)

    if plantingCommand == flowerArea.tile9:
        moveClick(690, 640, time)
    if plantingCommand == flowerArea.tile9:
        moveClick(880, 640, time)
    if plantingCommand == flowerArea.tile9:
        moveClick(1049, 640, time)
    if plantingCommand == flowerArea.tile9:
        moveClick(1195, 640, time)

def checkForHarvests(timeBeforeCheck = 60):
    #every minute check go through square list to see if any squares harvestClocks are at 1
    #have a clock that counts down every 60 seconds
    def timeout():
        searchSquaresForTime()
    
    t = Timer(timeBeforeCheck, timeout)
    t.start()
    #if so harvest land function
    #replantFlower (which resets the stats from plantFlower function)
    #if curr

def harvestFlower(square):
    #click scissors
    hudClick(hudArea.scissor)
    #click square that needs to be harvest
    moveClick(SqCenterPoint(square))
    #wait to see if pop up comes up
    #if it does click harvest
    if checkForPixels((814,452),20,20, (255,255,255)) == True:
        #green harvest button is at x900, y574
        moveClick(900, 574)
    square.needsHarvest = False
    #done         

def plantFlower(square, tile):
    #click hud shovel
    hudClick(hudArea.shovel)
    #till land
    moveClick(SqCenterPoint(square))
    #click hud plant
    hudClick(hudArea.plant)
    #click land
    moveClick(SqCenterPoint(square))
    #click tile
    plantingMenuClick(tile)
    #check id
    #apply stats to land
    #if cannot find ID or get stats default to 1 hour for harvest clock
    square.harvestTime = 60
    square.harvestClock = square.harvestTime
    #click water icon
    hudClick(hudArea.water)
    #click sqaure
    moveClick(SqCenterPoint(square))

def searchSquaresForTime():
    for i in range(len(squareList)):
        if squareList[i].harvestClock == 1:
            harvestFlower(squareList[i])
            squareList[i].harvestClock = squareList[i].harvestTime
            plantFlower(squareList[i])
        else:
            squareList[i].harvestClock - 1

def checkForPixels(center, xFar, yFar, pixelRGB = (255, 255, 255)):
    screenshot = pyautogui.screenshot()
    pyautogui.moveTo(center[0],center[1], 0.2)
    for x in range(pyautogui.position()[0] - xFar, 
                   pyautogui.position()[0] + xFar ):

        for y in range(pyautogui.position()[1] - yFar, 
                       pyautogui.position()[1] + yFar):

            if screenshot.getpixel((x, y)) == pixelRGB:
                return True


def moveClick(x, y, time=0.2):
    pyautogui.click(x,y,duration=time)

def moveClickSquare(square, time=0.2):
    pyautogui.click(SqCenterPoint(square)[0], 
                    SqCenterPoint(square)[1], 
                    duration=time)

#def MoveClickToSquare(square):
    #moveClick(SqCenterPoint(squareList[0])[0],
    #SqCenterPoint(squareList[0])[1], 1)

def SqCenterPoint(square):
    xDifference = square.rightPoint[0] - square.leftPoint[0]
    xDifferenceHalf = xDifference/2

    yDifference = square.topPoint[1] - square.bottomPoint[1]
    yDifferenceHalf = yDifference/2

    centerPoint = (square.leftPoint[0] + xDifferenceHalf, 
                   square.bottomPoint[1] + yDifferenceHalf)

    return centerPoint

def drawDiamonds(canvas):
    drawAllDiamonds(blank)
    cv.imshow('1 sqaure', blank)

def createDefaultSquare2(square):
    #BGR 68, 190, 255
    #pixelBGR = (68, 190, 255)
    pixelRGB = (255, 190, 68)
    innerArray = []
    outerArray = []
    endPointsArray = []
    columnArray = []
    
    innerMinX = None
    innerMaxX = None
    innerMinY = None
    innerMaxY = None
    

    innerLeft = None
    innerTop = None
    innerRight = None
    innerBottom = None
    #user places cursor he wants to be scanned
    #program saves position of mouse
    savedMousePos = [pyautogui.position()[0],pyautogui.position()[1]]
    #moves the mouse off of the sqaure (far away)
    pyautogui.move(543,1911)

    #screenshot
    screenshot = pyautogui.screenshot()

    #scans the area (smallish distance) for yellow bars
    #creates a sqaure within yellow bars as the clickable square

    
    
    
    #bottom right row
    i = 0
    j = 0
    firstRun = True
    while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] + j)) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) != pixelRGB):
            innerArray.append((savedMousePos[0]+i,savedMousePos[1] + j))  
            i += 1
            firstRun = False
    
    #bottom right column    
    i = 0 #i
    j = 0 #j
    firstRun = True
    while (screenshot.getpixel((savedMousePos[0] + j, savedMousePos[1])) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] + j, savedMousePos[1] + i)) != pixelRGB):
            if (savedMousePos[0]+j,savedMousePos[1] + i) not in innerArray:
                columnArray.append((savedMousePos[0]+j,savedMousePos[1] + i))
                if firstRun:
                    columnArray.append((savedMousePos[0]+j,savedMousePos[1] + i))  
            i += 1
            firstRun = False

    #bottom left           
    i = 0
    j = 0
    firstRun = True
    while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] + j)) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] - i, savedMousePos[1] + j)) != pixelRGB):
            innerArray.append((savedMousePos[0]-i,savedMousePos[1] + j))
            firstRun = False
            i += 1

    #bottom left column    
    i = 0 #i
    j = 0 #j
    firstRun = True
    while (screenshot.getpixel((savedMousePos[0] + j, savedMousePos[1])) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] - j, savedMousePos[1] + i)) != pixelRGB):
            if (savedMousePos[0]-j,savedMousePos[1] + i) not in innerArray:
                columnArray.append((savedMousePos[0]-j,savedMousePos[1] + i))
                if firstRun:
                    columnArray.append((savedMousePos[0]-j,savedMousePos[1] + i))  
            i += 1
            firstRun = False
    #top left     
    i = 0
    j = 0
    firstRun = True

    while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] - j)) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] - i, savedMousePos[1] - j)) != pixelRGB):
            innerArray.append((savedMousePos[0]-i,savedMousePos[1] - j))
            firstRun = False
            i += 1
    #top right
    i = 0
    j = 0
    firstRun = True
    #
    while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] - j)) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] - j)) != pixelRGB):
            innerArray.append((savedMousePos[0]+i,savedMousePos[1] - j))
            firstRun = False
            i += 1


    #sorting inner list 
    yMin2Max = lambda y: y[1]
    innerArray.sort(key=yMin2Max)
    #print (innerArray[0])
    #innerArray.pop(0)
    #innerArray.insert(0, (innerArray[0]-1, innerArray[1]))
    #print (innerArray[0])

    #print(innerArray[0])

    
    ##top column    
    #i = 0 #i
    #j = 0 #j
    #firstRun = True
    #while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] - j)) != pixelRGB):
    #    i = 0
    #    if firstRun == False:
    #        j += 1
    #    while (screenshot.getpixel((savedMousePos[0] - i, savedMousePos[1] - j)) != pixelRGB):
    #        if (savedMousePos[0]-i,savedMousePos[1] -j) not in innerArray:
    #            columnArray.append((savedMousePos[0]-i,savedMousePos[1]-j))  
    # 
    #        i += 1
    #        firstRun = False
            


    newImg = Image.new('RGB', (1920,1080))
    for i in range (len(innerArray)):
        if i == 0:
            continue
        newImg.putpixel((innerArray[i]), (255,0,255))
        newImg.save

    #firstX = 0
    #secondX = 0
    #lines = 0
    ##get the last x position of line 1 and 2 that will be drawn
    #for i in range(len(innerArray)):
    #    if lines < 2:
    #        if innerArray[i][1] != innerArray[i+1][1]:
    #            if firstX == 0:
    #                firstX = innerArray[i][0]
    #                lines = 1
    #            elif secondX == 0:
    #                secondX = innerArray[i][0]
    #                lines = 2
    #    if lines >= 2:
    #        break
    #trend = 0
    #find the difference of the last X positions to find trend
    #trend = secondX - firstX
    #print("Trend: ", trend)

    #find the non clickable outer edge, using trend to find the half way point
    #find end points
    #use it to find the trend (trend is the difference for the last x of the first and second lines of pixels)
    #also use the end points array to create the outer edge without checking over the inner square
    for i in range(len(innerArray)):
        try:
            if innerArray[i][1] != innerArray[i+1][1]:
                endPointsArray.append(innerArray[i])  

        except:
            pass
    print (len(innerArray))

    trend = endPointsArray[1][0]- endPointsArray[0][0]

    #creating the outer edge
    for i in range(len(endPointsArray)):
        j = 1

        x = endPointsArray[i][0]
        y = endPointsArray[i][1]
   
        while screenshot.getpixel((x + j, y)) == pixelRGB:
            j+=1
            outerArray.append((x + j, y))
    
    lastMax_X = 0
    breaking = False
    #find the side center and cut everything else under in the outer array
    new_outerArray = []
    deleteNumber = 0
    for i in range(len(outerArray)):
        if lastMax_X != 0:
        #    try:
        #        if outerArray[i][0] - lastMax_X and lastMax_X != 0:
        #            deleteNumber = i
        #            print("i equals: ", i)
        #            break
        #        if outerArray[i][0] - lastMax_X > trend and lastMax_X != 0:
        #            print("yes")
        #    except:
        #        pass
            if outerArray[i][0] - lastMax_X > trend:
                deleteNumber = i
                break
                #print("lastmax: ",  lastMax_X, "outerArray[i][0]: ",  outerArray[i][0])

        try:
            if outerArray[i][1] != outerArray[i+1][1]:
                lastMax_X = outerArray[i][0]
                #print("lastMax_x :", lastMax_X)
        except:
            pass

        
    



    for i in range(len(outerArray)):
        if i < deleteNumber:
            new_outerArray.append(outerArray[i])
    
    outerArray = new_outerArray
    


    #for i in range(len(outerArray)):
    #    if breaking == True:
    #        print("break")
    #        break
    #    j = 1
    #    it = 0
    #    try:
    #        if outerArray[i][1] != outerArray[i+1][1]:
    #            lastMax_X = outerArray[i][0]
    #            #print(lastMax_X)
    #    except:
    #        pass
    #    try:
    #        if outerArray[i][0] - lastMax_X > trend and lastMax_X != 0:
    #        
    #            print("outerArray: ", outerArray[i][0])
    #            print("last Max: ", lastMax_X)
    #        #print ("before deletion", len(outerArray))
    #            lastRemove = 0
    #            lastRemoveK = 0
    #            for item in outerArray[:]):
    #                print 
    #                new_outerArray.remove(outerArray[i+k])
    #                
    #    except:
    #        pass



    #debug display square
    #open_cv_image = np.array(newImg) 
    #open_cv_image = open_cv_image[:, :, ::-1].copy()
    #cv.imshow("newImg", open_cv_image)
    #cv.waitKey(0)

    #for the outer
    #for left and right sides
    #bottom right
#bottom right
   # i = 0
    #j = 0
  
   #while (True):
   #    i = 0
   #    
   #    if firstRun == False:
   #        j += 1
   #    while (screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) != pixelRGB):
   #        i += 1
   #        firstRun = False
   #        
   #    while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] + j)) == pixelRGB):
   #        if doneInner == False:
   #            doneInner = True
   #            outerArray.append((savedMousePos[0]+i,savedMousePos[1] + j))
   #    break
##left side
#    for val in range(len(innerArray)):
#        try:
#            if innerArray[val][1] != innerArray[val+1][1]:
#                #print ("before: ",innerArray[val][0])
#                #print ("after: ",innerArray[val][0]+1)
#
#                i = 1
#
#                while screenshot.getpixel((innerArray[val][0]-i, innerArray[val][1])) == pixelRGB:
#                    #print("yay")
#                    outerArray.append((innerArray[val][0]-i, innerArray[val][1]))
#                    i += 1
#        except:
#            print (len(outerArray))
#            break

#corner right side 
    #go the inner array 
    #run = 1
    #trend = 0
    #t1 = 0
    #t2 = 0
#    for val in range(len(innerArray)):
#        if run < 3:
#            #need i to reset here so it resets every line (y)
#            i = 1
#            #check if the next x in the array has the colour we are looking for (boarder)
#            #while it equals that colour
#            while screenshot.getpixel((innerArray[val][0]+i, innerArray[val][1])) == pixelRGB:
#                #add this value to our outerArray so we know the boarders
#                outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
#                print("append")
#                #this is for the extra number on the x
#                i += 1
#            if screenshot.getpixel((innerArray[val][0]+i-1, innerArray[val][1])) == pixelRGB and screenshot.getpixel((innerArray[val][0]+i, innerArray[val][1])) != pixelRGB:
#                print("called, run")
#                run +=1
#           
#            if run > 2:
#                print('run > 2 inside')
#                print(len(outerArray))
#                #creates trend
#                for trendVal in range(len(outerArray)):
#                    
#                    if trendVal == 0:
#                        continue
#                    if outerArray[trendVal-1][1] != outerArray[trendVal][1]:
#                        if t1 != 0:
#                            t2 = outerArray[trendVal-1][0]
#                            trend = t1 - t2
#                            print ('t1: ', t1, ' t2: ', t2)
#                            break
#                        if t1 == 0:
#                            t1 = outerArray[trendVal-1][0]
#            
#        elif run > 2:
#            i = 1
#            #check if the next x in the array has the colour we are looking for (boarder)
#            #while it equals that colour
#            while screenshot.getpixel((innerArray[val][0]+i, innerArray[val][1])) == pixelRGB:
#                #add this value to our outerArray so we know the boarders
#                outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
#                #this is for the extra number on the x
#                i += 1
#            run +=1
   
    
   # for val in range(len(innerArray)):
   #     i = 1
            #check if the next x in the array has the colour we are looking for (boarder)
   #         #while it equals that colour
        
   ##     while screenshot.getpixel((innerArray[val][0]+i, innerArray[val][1])) == pixelRGB:
                    #add this value to our outerArray so we know the boarders
    #        #print("append")
    #        #print (innerArray[val][1])
            
   #         outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
   #        
    #        called = True
#
    #            #this is for the extra number on the x
    #        i += 1




    #trend = 0
    #t1 = 0
    #t2 = 0
    #previousMax_X = 0
    #runCounter = 1
    #trendCounter = 0
    #trendVal = 0
    #for val in range(len(innerArray)):
    #    i = 1
    #    if runCounter < 3:
    #        while screenshot.getpixel((innerArray[val][0]+i, innerArray[val][1])) == pixelRGB:
    #            outerArray.append((innerArray[val][0]+i, innerArray[val][1]))    
    #            i += 1
    #            
#
    #            
    #        #creates trend
    #        for val in range(len(outerArray)):
    #            if val == 0:
    #                continue
    #            if outerArray[val-1][1] != outerArray[val][1]:
    #                if t1 != 0:
    #                    t2 = outerArray[val-1][0]
    #                    trend = t1 - t2
    #                    print (t1, t2)
    #                    break
    #                if t1 == 0:
    #                    t1 = outerArray[val-1][0]
#
    #       # runCounter += 1 
    #    if runCounter > 2:
    #        #print ("trend: ", trend)
    #        while screenshot.getpixel((innerArray[val][0]+i, innerArray[val][1])) == pixelRGB:
    #            
    #            #outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
    #            for val in range(len(outerArray)):
    #                if outerArray[val-1][1] != outerArray[val][1]:
    #                    previousMax_X = outerArray[val-1][0]
#
    #                if innerArray[val][0]+i < previousMax_X:
    #                    outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
    #                    i += 1
    #                    runCounter += 1
    #                    continue
#
    #                if innerArray[val][0]+i > previousMax_X and innerArray[val][0]+i < trend+1:
    #                    outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
    #                    i += 1
    #                    runCounter += 1
    #                    continue
#
    #                if innerArray[val][0]+i < previousMax_X and innerArray[val][0]+i < trend+1:
    #                    outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
    #                    i += 1
    #                    runCounter += 1
    #                    continue
            
        

                    


    ##DISTANCES FOR OUTTA EDGE
    #BLTR_BOARDER = 0
    #for val in range(len(outerArray)):
    #    #if BLTR_BOARDER == 0:
    #    #    BLTR_BOARDER = 1
    #    #    continue
    #    if outerArray[val][1] == outerArray[val+1][1]:
    #        #print(outerArray[val][1])
    #        BLTR_BOARDER += 1
    #    if outerArray[val][1] != outerArray[val+1][1]:
    #        BLTR_BOARDER += 1
    #        BLTR_BOARDER -= 1
    #       # print("size is: ", BLTR_BOARDER)
    #        print('break')
    #        break
    

    #TLBR_BOARDER = 0
    ##startOfLine = True
    ##Loop over the inner array
    #halfWay = False
    #for i in range(len(innerArray)):
    #    
    #    if halfWay == False:
    #        #if next pixel's Y is not the same as last, its on a new line
    #        try:
    #            if innerArray[i][1] != innerArray[i+1][1]:
    #                #print("First Check: ", "Inner1Y: ", innerArray[i][1], " Inner2Y: ",innerArray[i+1][1] )
    #                #loop over again as now we are checking to see if the X's values are the same
    #                #loop over and find when the next one isn;t the same
    #                firstCheckX = innerArray[i][0]
    #                
    #                #print ("firstCheckX: ", firstCheckX )
    #                for k in range(innerArray[i+1][1]):
    #                    
    #                    #last x on next row
    #                    if innerArray[i+1][1] != innerArray[i+2][1]:
#
    #                    #check X values
    #                    #if the x are the same, that means we have hit half way
    #                        if firstCheckX == innerArray[i+1][0]:
    #                            #print("found") 
    #                            pass
    #                        elif firstCheckX != innerArray[i+1][0]:
    #                            #print("not same firstCheckX: ", firstCheckX , " +1: ", innerArray[i+1][0])
    #                            pass
    #        except:
    #            print("done")
    #    elif halfWay == True:
    #        pass


#
        #    if innerArray[val][1] != innerArray[val+1][1]:
        #        #print ("before: ",innerArray[val][0])
        #        #print ("after: ",innerArray[val][0]+1)
#
        #        i = 1
#
        #        while screenshot.getpixel((innerArray[val][0]+i, innerArray[val][1])) == pixelRGB:
        #            #print("yay")
        #            outerArray.append((innerArray[val][0]+i, innerArray[val][1]))
        #            
        #            i += 1
        #except:
        #    print (len(outerArray))
        #    break

    for val in range(len(columnArray)):    
            try:
                if columnArray[val][1] != columnArray[val+1][1]:
                    #print ("before: ",innerArray[val][0])
                    #print ("after: ",innerArray[val][0]+1)

                    i = 1

                    while screenshot.getpixel((columnArray[val][0]+i, columnArray[val][1])) == pixelRGB:
                        #print("yay")
                        #outerArray.append((columnArray[val][0]+i, columnArray[val][1]))

                        i += 1
            except:

                break
        


#while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] - j)) != pixelRGB and onOuter == False or
#           screenshot.getpixel((savedMousePos[0], savedMousePos[1] - j)) == pixelRGB):

    #i = 0
    #j = 0
#
    #firstRun = True
    #onOuter = False
    #finishedLine = False
    #lastRun = False
    #while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] - j)) != pixelRGB):
    #    i = 0
    #    if firstRun == False:
    #        j += 1
    #    if finishedLine == False:
    #        print("finsihed line was false")
    #        while screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) != pixelRGB:
    #            #if we go on non colour after colour
    #            if onOuter == True:
    #                finishedLine = True
    #                print("finsihed line = True")
    #                break
    #            i += 1
    #            firstRun = False
    #        while screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) == pixelRGB:
    #            onOuter = True
    #            outerArray.append((savedMousePos[0]+i,savedMousePos[1] + j))
    #            print("outer append")
    #            i += 1
#
    #            break
    #    if finishedLine == True:
    #        print("finsihed line was true")
    #        
    #        print("lastRun = True")
    #        if screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) == pixelRGB:
    #            lastRun = True
    #            while screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) == pixelRGB:
    #                outerArray.append((savedMousePos[0]+i,savedMousePos[1] + j))
    #                print("outer append 2")
    #                i += 1
    #    if screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) != pixelRGB and lastRun == True:
    #        print("break")
    #        break

    
    #newImg = Image.new('RGB', (1920,1080))
    for i in range (len(outerArray)):
        if i == 0:
            continue
        newImg.putpixel((outerArray[i]), (0,0,255))
        newImg.save

    for i in range (len(columnArray)):
        if i == 0:
            continue
        newImg.putpixel((columnArray[i]), (255,0,0))
        newImg.save

    #debug display square
    
    open_cv_image = np.array(newImg) 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    cv.imshow("newImg", open_cv_image)
    cv.waitKey(0)
        

    #divide the x pos, that the no clickable left and right side
    
    #for top and bottom sides
    #find the next square above or below
    #get the inbetween distance again but for the y
    #devide that y by 2 and these are the non clickable areas
    #finds the inner
    #saves the outer and inner positions
    #when placeing squares, outer must overlap
    square.setPoints(innerLeft, innerTop, innerRight, innerBottom)


def getMax_X_ValueInY(RGB, listOfPixels):
    for i in range (len(listOfPixels)):
        print ("rgb: ",listOfPixels[i])         

def createDefaultSquare(square):
    #purple colour code
    #RGB - 166, 107, 208
    #HSV - 183, 124, 148
    pixelRGB = (166, 107, 208)
    posArray = []
    
    lowestX = None
    lowestY = None
    highestX = None
    highestY = None

    innerLeft = None
    innerTop = None
    innerRight = None
    innerBottom = None

    #bufferBottomLeft = None
    #bufferBottomRight = None
    buffer = None

    screenshot = pyautogui.screenshot()
    for x in range(pyautogui.position()[0] - 125, 
                   pyautogui.position()[0] + 125 ):

        for y in range(pyautogui.position()[1] - 110, 
                       pyautogui.position()[1] + 110):

            if screenshot.getpixel((x, y)) == pixelRGB:
                posArray.append((x,y))  
                #pyautogui.moveTo(x,y)

    for i in range(len(posArray)):
        if lowestX == None:
            lowestX = posArray[i]
        if lowestY == None:
            lowestY = posArray[i]
        if highestX == None:
            highestX = posArray[i]
        if highestY == None:
            highestY = posArray[i]

        #find lowest X pos tuple
        #print(lowestY[1])
        #print(posArray[i][1])
    #found outer of each edge
        #find lowest X pos tuple
        if lowestX[0] > posArray[i][0]:  
            lowestX = posArray[i]
            continue

        #find lowest Y pos tuple

        if lowestY[1] > posArray[i][1]:
            lowestY = posArray[i]
            continue

        #find highest X pos tuple

        if highestX[0] < posArray[i][0]:
            highestX = posArray[i]
            continue

        #find highest Y pos tuple

        if highestY[1] < posArray[i][1]:
            highestY = posArray[i]
            continue

    #square.setPoints(lowestX, highestY, highestX, lowestY)

    #use outer edge to now find the inner for consistancy 
    #innerLeft
    for pix in range (15):
        if screenshot.getpixel((lowestX[0] + pix + 1, lowestX[1])) != pixelRGB:
            innerLeft = [lowestX[0] + pix + 1, lowestX[1]]
            break

    #innerTop
    for pix in range (15):
        if screenshot.getpixel((highestY[0], highestY[1] - pix - 1)) != pixelRGB:
            innerTop = [highestY[0], highestY[1] - pix - 1]
            break
   
    #innerRight
    for pix in range (15):
        print("highestX: ",highestX[0] - pix - 1,highestX[1] - pix - 1 )
        #if screenshot.getpixel((highestX[0] - pix - 1,)) != pixelRGB:
            #innerRight = [highestX[0] - pix - 1, highestX[1] - pix - 1]
            #print("HighestX: ", highestX)
            #print("innerRight: ", innerRight)
            #break
    
    #innerBottoms
    for pix in range (15):
        if screenshot.getpixel((lowestY[0], lowestY[1] + pix +1)) != pixelRGB:
            innerBottom = [lowestY[0], lowestY[1] + pix +1]
            break

    #find buffers
    #rightBuffer
    #sbuffer = innerBottom[1]- lowestY[1] 
    
    #rightBuffer = [innerRight[0] - highestX[0], innerRight[1] - highestX[1]]
    #print(rightBuffer)
    #innerRight = [innerRight[0] - rightBuffer[0], innerRight[1] - rightBuffer[1]]
    #innerLeft = [innerLeft[0]  + buffer, innerLeft[1]  + buffer]
    #innerBottom = [innerBottom[0] + buffer,innerBottom[1] + buffer]

    square.setPoints(innerLeft, innerTop, innerRight, innerBottom)

def addMultipleSqaures (posDir, baseSquare, multiple, colour):
    for i in range(multiple):
        addSqaure(posDir, baseSquare, True, colour)
        

def addMultipleSqauresWithFakes(posDir, baseSquare, multiple, colour):
    for i in range(multiple):
        if i+1 != multiple:
            addSqaure(posDir, baseSquare, False, (232,162,0))
        if i+1 == multiple:
            addSqaure(posDir, baseSquare, True, colour)

def addSqaure(posDir, baseSquare, realSquare = True, squareColour = baseSquare.colour,
              thickness = baseSquare.thickness):
    square = Square()
    if realSquare == True:
        square.realSquare = True
        square.colour = squareColour
        square.thickness = thickness
    else:
        square.realSquare = False
        square.colour = squareColour
        square.thickness = thickness
    squareList.append(square)

    positionNextSquare(square, posDir, baseSquare)



def positionNextSquare(square, posDir, baseSquare):
    
    previousPos = squareList[-2]
    if (posDir == SquarePos.bottom_left):
        LTXdifference = previousPos.leftPoint[0] - previousPos.topPoint[0]
        TLYdifference = previousPos.topPoint[1] - previousPos.leftPoint[1]

        #setSquarePosFull(square, previousSquare, LTXdifference, TLYdifference)
        square.rightPoint = previousPos.topPoint
        square.bottomPoint = previousPos.leftPoint
        
        #topPoint
        #LTXdifference = previousSquare.leftPoint[0] - previousSquare.topPoint[0]
        #TLYdifference = previousSquare.topPoint[1] - previousSquare.leftPoint[1]

        #x
        square.topPoint[0] = previousPos.topPoint[0] + LTXdifference
        #y
        square.topPoint[1] = previousPos.topPoint[1] + TLYdifference

        #leftPoint
        #x
        square.leftPoint[0] = previousPos.leftPoint[0] + LTXdifference
        #y
        square.leftPoint[1] = previousPos.leftPoint[1] + TLYdifference

    if (posDir == SquarePos.bottom_right):
        RTXdifference = previousPos.rightPoint[0] - previousPos.topPoint[0]
        TRYdifference = previousPos.topPoint[1] - previousPos.rightPoint[1]


        #setSquarePosFull(square, posDir, previousSquare, RTXdifference, TRYdifference)
        square.leftPoint = previousPos.topPoint
        square.bottomPoint = previousPos.rightPoint
    
        #rightPoint

       # x
        square.rightPoint[0] = previousPos.rightPoint[0] + RTXdifference
       # y
        square.rightPoint[1] = previousPos.rightPoint[1] + TRYdifference 

        #topPoint
        #x
        square.topPoint[0] = previousPos.topPoint[0] + RTXdifference 
       # y
        square.topPoint[1] = previousPos.topPoint[1] + TRYdifference


    if (posDir == SquarePos.top_right):
       square.topPoint = previousPos.rightPoint
       square.leftPoint = previousPos.bottomPoint
       
       #rightPoint
       RTXdifference = previousPos.rightPoint[0] - previousPos.topPoint[0]
       TLYdifference = previousPos.topPoint[1] - previousPos.leftPoint[1]

       #x
       square.rightPoint[0] = previousPos.rightPoint[0] + RTXdifference
       #y
       square.rightPoint[1] = previousPos.bottomPoint[1]

       #bottomPoint
       #x
       square.bottomPoint[0] = previousPos.bottomPoint[0] + RTXdifference
       #y
       square.bottomPoint[1] = previousPos.bottomPoint[1] - TLYdifference

    if (posDir == SquarePos.top_left):
       square.topPoint = previousPos.leftPoint
       square.rightPoint = previousPos.bottomPoint
       
       #leftPoint
       LBXdifference = previousPos.leftPoint[0] - previousPos.bottomPoint[0]
       LBYdifference = previousPos.leftPoint[1] - previousPos.bottomPoint[1]

       #x
       square.leftPoint[0] = previousPos.leftPoint[0] + LBXdifference
       #y
       square.leftPoint[1] = previousPos.bottomPoint[1]

       #bottomPoint
       #x
       square.bottomPoint[0] = previousPos.bottomPoint[0] + LBXdifference
       #y
       square.bottomPoint[1] = previousPos.bottomPoint[1] - LBYdifference

#def setSquarePosFull(square, posDir, prevPos, diff1, diff2):
#    pos1 = None
#    pos2 = None
#    pos3 = None
#    pos4 = None
#
#    prevPos1 = None
#    prevPos2 = None
#    prevPos3 = None
#    prevPos4 = None
#    
#    if posDir == SquarePos.bottom_right:
#        pos1 = square.leftPoint
#        pos2 = square.topPoint
#        pos3 = square.bottomPoint
#        pos4 = square.rightPoint
#
#        prevPos1 = prevPos.topPoint
#        prevPos2 = prevPos.rightPoint
#    
#    #left               top
#    pos1 = prevPos1
#    #bot                right
#    pos3 = prevPos2
#    #rightPoint
#    #RTXdifference = prevPos.rightPoint[0] - prevPos.topPoint[0]
#    #TRYdifference = prevPos.topPoint[1] - prevPos.rightPoint[1]
#    #x
#    pos4[0] = prevPos2[0] + diff1
#    #y
#    pos4[1] = prevPos2[1] + diff2 
#    #topPoint
#    #x
#    pos2[0] = prevPos1[0] + diff1
#    #y
#    pos2[1] = prevPos1[1] + diff2    


def drawDiamond(img, leftPoint, topPoint, rightPoint, bottomPoint, colour, thickness):
    cv.line(img, leftPoint, topPoint, colour, thickness)
    cv.line(img, topPoint, rightPoint, colour, thickness)
    cv.line(img, rightPoint, bottomPoint, colour, thickness)
    cv.line(img, bottomPoint, leftPoint, colour, thickness)

def drawAllDiamonds(img):
    for i, sqaure in enumerate(squareList):
        #print (squareList[i].leftPoint)
        drawDiamond(img, squareList[i].leftPoint, squareList[i].topPoint, 
                         squareList[i].rightPoint, squareList[i].bottomPoint,
                         squareList[i].colour,
                         squareList[i].thickness)
        #print(squareList[i].realSquare)
        

def countdownTimer():

    #Countdown Timer
    print("Starting", end="")
    for i in range(0,6):
        print(".", end="")
        sleep(1)
    print("Go")


if __name__ == "__main__":
    main()
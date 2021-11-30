from io import DEFAULT_BUFFER_SIZE
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
    posArray = []

    innerLeft = None
    innerTop = None
    innerRight = None
    innerBottom = None
    #user places cursor he wants to be scanned
    #program saves position of mouse
    savedMousePos = pyautogui.position()
    #moves the mouse off of the sqaure (far away)
    pyautogui.move(543,1911)

    #screenshot
    screenshot = pyautogui.screenshot()

    #scans the area (smallish distance) for yellow bars
    #creates a sqaure within yellow bars as the clickable square
    
    #bottom right
    i = 0
    j = 0
    firstRun = True
    while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] + j)) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] + i, savedMousePos[1] + j)) != pixelRGB):
            posArray.append((savedMousePos[0]+i,savedMousePos[1] + j))  
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
            posArray.append((savedMousePos[0]-i,savedMousePos[1] + j))
            firstRun = False
            i += 1

    #top left     
    i = 0
    j = 0
    firstRun = True

    while (screenshot.getpixel((savedMousePos[0], savedMousePos[1] - j)) != pixelRGB):
        i = 0
        if firstRun == False:
            j += 1
        while (screenshot.getpixel((savedMousePos[0] - i, savedMousePos[1] - j)) != pixelRGB):
            posArray.append((savedMousePos[0]-i,savedMousePos[1] - j))
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
            posArray.append((savedMousePos[0]+i,savedMousePos[1] - j))
            firstRun = False
            i += 1
            
      

    newImg = Image.new('RGB', (1920,1080))
    for i in range (len(posArray)):
        if i == 0:
            continue
        newImg.putpixel((posArray[i]), (255,0,255))
        newImg.save



    # Convert RGB to BGR 


   #for i in range(len(posArray)):
   #    if innerLeft == None:
   #        innerLeft = posArray[i]
   #    if innerTop == None:
   #        innerTop = posArray[i]
   #    if innerRight == None:
   #        innerRight = posArray[i]
   #    if innerBottom == None:
   #        innerBottom = posArray[i]

   #        #if screenshot.getpixel((lowestY[0], lowestY[1] + pix +1)) != pixelRGB:
   #    #find lowest X pos tuple
   #    if innerLeft[0] > posArray[i][0]:  
   #        innerLeft = posArray[i]
   #        continue
   #    
   #    #find lowest Y pos tuple

   #    if innerBottom[1] > posArray[i][1]:
   #        innerBottom = posArray[i]
   #        continue
   #    
   #    #find highest X pos tuple

   #    if innerRight[0] < posArray[i][0]:
   #        innerRight = posArray[i]
   #        continue
   #    
   #    #find highest Y pos tuple

   #    if innerTop [1] < posArray[i][1]:
   #        innerTop  = posArray[i]
   #        continue

        
    #newImg.putpixel((innerLeft), (255,0,255))
    #newImg.save
#
    #newImg.putpixel((innerBottom), (255,0,255))
    #newImg.save
#
    #newImg.putpixel((innerRight), (255,0,255))
    #newImg.save
#
    #newImg.putpixel((innerTop), (255,0,255))
    #newImg.save

    open_cv_image = np.array(newImg) 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    cv.imshow("newImg", open_cv_image)
    cv.waitKey(0)

    square.setPoints(innerLeft, innerTop, innerRight, innerBottom)

    #for the outer
    #for left and right sides
    #find the left point or right point
    #find the next inner across from the current clickable square (so inbetween)
    #divide the x pos, that the no clickable left and right side
    
    #for top and bottom sides
    #find the next square above or below
    #get the inbetween distance again but for the y
    #devide that y by 2 and these are the non clickable areas
    #finds the inner
    #saves the outer and inner positions
    #when placeing squares, outer must overlap

    
    pass

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
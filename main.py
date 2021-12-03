from io import DEFAULT_BUFFER_SIZE
from sys import _debugmallocstats, exec_prefix, flags
from PyQt5.QtGui import QPainter
from numpy.core.numeric import outer
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
import math

script_dir = os.path.dirname(__file__)

squareList = []
baseSquare = Square()
newSqaure = Square()

squareBoarderX = 0
squareBoarderY = 0

innerSqaureCornerLeft  = 0
innerSqaureCornerRight = 0
innerSqaureCornerUpper = 0
innerSqaureCornerLower = 0

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
    createDefaultSquare(baseSquare)
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
    
    addMultipleSqauresWithFakes(SquarePos.bottom_left, baseSquare, 10, (255,0,255))
    addMultipleSqaures(SquarePos.bottom_right, baseSquare, 10, (255,0,255))
    #addMultipleSqauresWithFakes(SquarePos.top_right, baseSquare, 5, (255,0,255))
    #addMultipleSqauresWithFakes(SquarePos.top_right, baseSquare, 5, (255,0,255))

    
    #drawDebug
    drawDiamonds(blank)
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
    #    if squareList[i].realSquare == True:
    #            moveClickSquare(squareList[i], 1)
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
def createDefaultSquare(square):
    currentLeftSide = [0,0]
    currentTopSide = [0,0]
    currentRightSide = [0,0]
    currentBottomSide = [0,0]

    innerLeftSide = [0,0]
    innerTopSide = [0,0]
    innerRightSide = [0,0]
    innerBottomSide = [0,0]

    currentOuterLeft = [0,0]
    currentOuterTop = [0,0]
    currentOuterRight = [0,0]
    currentOuterBottom = [0,0]

    finalLeftSide = [0,0]
    finalTopSide = [0,0]
    finalRightSide = [0,0]
    finalBottomSide = [0,0]

    boarderRGB = (255, 190, 68)

    savedMousePositon = pyautogui.position()
    pyautogui.moveTo(543,1911)
    
    screenshot = pyautogui.screenshot()

    #from saved mouse pos search for right side

    for i in range(9999):
        if screenshot.getpixel((savedMousePositon[0] + i, savedMousePositon[1])) != boarderRGB:
            currentRightSide = [savedMousePositon[0] + i, savedMousePositon[1]]
        else:
            break

    #once at far right side
    pyautogui.moveTo(currentRightSide[0],currentRightSide[1] , 2)

  
        #check where the the colour is above and below

    above = [currentRightSide[0], currentRightSide[1]]
    below = [currentRightSide[0], currentRightSide[1]]

    #above
    for i in range(9999):
        if screenshot.getpixel((currentRightSide[0], currentRightSide[1]-i)) != boarderRGB:
            above = [currentRightSide[0], currentRightSide[1]-i]
        else: 
            break
    #below        
    for i in range(9999):
        if screenshot.getpixel((currentRightSide[0], currentRightSide[1]+i)) != boarderRGB:
            below = [currentRightSide[0], currentRightSide[1]+i]
        else: 
            break

    aboveCheck = currentRightSide[1] - above[1]
    belowCheck =  below[1] - currentRightSide[1]


    #if boarder is above, try 1 down 2 right
    if aboveCheck < belowCheck:
        for i in range(9999):
            for k in range(9999):
                
                if screenshot.getpixel((currentRightSide[0]+1, currentRightSide[1])) == boarderRGB and screenshot.getpixel((currentRightSide[0],currentRightSide[1]+1 )) != boarderRGB:
                    currentRightSide[1] += 1
                    #pyautogui.moveTo(currentRightSide[0],currentRightSide[1], 0.001)
                    #print(1)
                else: 
                    break
            for j in range(9999):
                if screenshot.getpixel((currentRightSide[0] + 1, currentRightSide[1])) != boarderRGB:
                    currentRightSide[0] += 1
                    #pyautogui.moveTo(currentRightSide[0],currentRightSide[1], 0.001)
                    #print(2)
                else:
                    break

    #put in parking spot
        for j in range(9999):
            if screenshot.getpixel((currentRightSide[0],currentRightSide[1]-1 )) !=boarderRGB:
                currentRightSide[1]-=1

                #pyautogui.moveTo(currentRightSide[0],currentRightSide[1], 0.001)
            else:
                break
    innerRightSide = currentRightSide
    #if boarder is below, try 1 up and 2 right 
    if belowCheck < aboveCheck:
        for i in range(9999):
            for k in range(9999):
                
                if screenshot.getpixel((currentRightSide[0]+1, currentRightSide[1])) == boarderRGB and screenshot.getpixel((currentRightSide[0],currentRightSide[1]-1 )) != boarderRGB:
                    currentRightSide[1] -= 1
                    #pyautogui.moveTo(currentRightSide[0],currentRightSide[1], 0.001)
                    #print(1)
                else: 
                    break
            for j in range(9999):
                if screenshot.getpixel((currentRightSide[0] + 1, currentRightSide[1])) != boarderRGB:
                    currentRightSide[0] += 1
                    #pyautogui.moveTo(currentRightSide[0],currentRightSide[1], 0.001)
                    #print(2)
                else:
                    break
    #put in parking spot
        for j in range(9999):
            if screenshot.getpixel((currentRightSide[0],currentRightSide[1]+1 )) !=boarderRGB:
                currentRightSide[1]+=1
                #pyautogui.moveTo(currentRightSide[0],currentRightSide[1], 0.001)
            else:
                break
    innerRightSide = currentRightSide
    #if boarder is under or above this is then this is the right side
        #sorted with parking 

    #once right side is complete
    #from right side, travel backwards on the x to find left side
    currentLeftSide = currentRightSide
    for i in range(9999):
        if screenshot.getpixel((currentLeftSide[0]-1, currentLeftSide[1])) != boarderRGB:
            currentLeftSide = [currentLeftSide[0]-1, currentLeftSide[1]]
            #pyautogui.moveTo(currentLeftSide[0], currentLeftSide[1], 0.001)
        else:
            break
    #pyautogui.moveTo(currentLeftSide[0], currentLeftSide[1], 0.001)
    #once you hit the boarder this is left side
    innerLeftSide = currentLeftSide
    #divide the distance between rightside x and leftside x by 2
    distXRL = innerRightSide[0] - innerLeftSide[0]
    print("distXRL: ", distXRL)
    divXRL = distXRL/2

    print("divXRL: ", math.floor(divXRL))
    #pyautogui.moveTo(innerLeftSide[0] + divXRL, currentLeftSide[1], 0.001)

    #from here travel the y up and down until you reach the boarder
    #Top
    currentTopSide = [innerLeftSide[0] + divXRL, currentLeftSide[1]]

    for i in range(9999):
        if screenshot.getpixel((currentTopSide[0],currentTopSide[1] -1)) != boarderRGB:
            currentTopSide[1] -= 1
            #pyautogui.moveTo(currentTopSide[0], currentTopSide[1], 0.001)
        else:
            break
    #put in parking spot
    for j in range(9999):
        if screenshot.getpixel((currentTopSide[0]-1,currentTopSide[1])) !=boarderRGB:
            currentTopSide[0]-=1

        else:
            break
    innerTopSide = currentTopSide
    #pyautogui.moveTo(innerTopSide[0],innerTopSide[1], 0.001)

    currentBottomSide = [innerLeftSide[0] + divXRL, currentLeftSide[1]]
    #Bottom
    for i in range(9999):
        if screenshot.getpixel((currentBottomSide[0], currentBottomSide[1] + 1)) != boarderRGB:
            currentBottomSide[1] += 1
            #pyautogui.moveTo(currentBottomSide[0], currentBottomSide[1], 0.001)
        else:
            break
    #put in parking spot
    for j in range(9999):
        if screenshot.getpixel((currentBottomSide[0]-1,currentBottomSide[1])) !=boarderRGB:
            currentBottomSide[0]-=1

        else:
            break   
    innerBottomSide = currentBottomSide
    #pyautogui.moveTo(innerBottomSide[0],innerBottomSide[1], 0.001)
    
    #once reached these are the up and down pos of the sqaure
    #check if there is any space next to the up and down positions

    #for the boarders
    #go from these positions and find all the pixels of the boarder 
    # (for example, on the rightside check x+, leftside check x-)
    currentOuterLeft = [innerLeftSide[0]-1, innerLeftSide[1]]
    currentOuterTop = [innerTopSide[0], innerTopSide[1]-1]
    currentOuterRight = [innerRightSide[0]+1, innerRightSide[1]]
    currentOuterBottom = [innerBottomSide[0], innerBottomSide[1]+1]
    #pyautogui.moveTo(currentOuterLeft[0], currentOuterLeft[1], 0.001)
    #Left
    for i in range(9999):
        if screenshot.getpixel((currentOuterLeft[0]-1,currentOuterLeft[1])) == boarderRGB:
            currentOuterLeft[0] -= 1
            #pyautogui.moveTo(currentOuterLeft[0], currentOuterLeft[1], 0.001)
        else:
            break
    
    #Top
    for i in range(9999):
        if screenshot.getpixel((currentOuterTop[0],currentOuterTop[1]-1)) == boarderRGB:
            currentOuterTop[1] -= 1
            #pyautogui.moveTo(currentOuterTop[0], currentOuterTop[1], 0.001)
        else:
            break
    
    #Right
    for i in range(9999):
        if screenshot.getpixel((currentOuterRight[0]+1,currentOuterRight[1])) == boarderRGB:
            currentOuterRight[0] += 1
            #pyautogui.moveTo(currentOuterRight[0], currentOuterRight[1], 0.001)
        else:
            break
    
    #Bottom
    for i in range(9999):
        if screenshot.getpixel((currentOuterBottom[0],currentOuterBottom[1]+1)) == boarderRGB:
            currentOuterBottom[1] += 1
            #pyautogui.moveTo(currentOuterBottom[0], currentOuterBottom[1], 0.001)
        else:
            break

    distLeft = innerLeftSide[0] - currentOuterLeft[0]
    distTop = innerTopSide[1] - currentOuterTop[1]
    distRight = currentOuterRight[0] - innerRightSide[0]
    distBottom = currentOuterBottom[1] - innerBottomSide[1]


    # divide by 2 and thats the boarder number
    distLeft = round(distLeft/2)
    distTop = round(distTop/2)
    distRight = round(distRight/2)
    distBottom = round(distBottom/2)

    #add this with the correct side and this is the total number, create a sqaure with this
    finalLeftSide = [innerLeftSide[0] - distLeft, innerLeftSide[1]]
    finalTopSide = [innerTopSide[0], innerTopSide[1] - distTop]
    finalRightSide = [innerRightSide[0] + distRight, innerRightSide[1]]
    finalBottomSide = [innerBottomSide[0], innerBottomSide[1] + distBottom]

    #pyautogui.moveTo(finalLeftSide[0], finalLeftSide[1], 5)
    #pyautogui.moveTo(finalTopSide[0], finalTopSide[1], 5)
    #pyautogui.moveTo(finalRightSide[0], finalRightSide[1], 5)
    #pyautogui.moveTo(finalBottomSide[0], finalBottomSide[1], 5)

    print("finaltopside: ", finalTopSide)
    square.setPoints(finalLeftSide, finalTopSide, finalRightSide, finalBottomSide)


def getMax_X_ValueInY(RGB, listOfPixels):
    for i in range (len(listOfPixels)):
        print ("rgb: ",listOfPixels[i])         


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
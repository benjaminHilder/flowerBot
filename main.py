from io import DEFAULT_BUFFER_SIZE
from sys import _debugmallocstats, exec_prefix, flags
from typing import final
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
from threading import TIMEOUT_MAX, Timer
import math
import keyboard
import mouseinfo
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import sys
import timerThread
from pynput import mouse, keyboard
from time import time
import recorder
import json
import cv2

from pytesseract import pytesseract
from pytesseract import Output

script_dir = os.path.dirname(__file__)

quittingApp = False

firstRun = True
nextRun = False
squareList = []
baseSquare = Square()
#newSqaure = Square()

squareBoarderX = 0
squareBoarderY = 0

innerSqaureCornerLeft  = 0
innerSqaureCornerRight = 0
innerSqaureCornerUpper = 0
innerSqaureCornerLower = 0

harvestQueue = []
plantingQueue = []
waterCount = 0

waterPos = [0,0]

refreshIMG = None

landXPos = 0
landYPos = 0
landType = ""
blank = np.zeros((1080,1920,3), dtype='uint8')

consoleActive = False

topLeftCenterPointDistance = [0,0]
topRightCenterPointDistance = [0,0]
bottomLeftCenterPointDistance = [0,0]
bottomRightCenterPointDistance = [0,0]

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
    false_position = 5
class landKind(Enum):
    soil = 1
    stone = 2
    sand = 3
    lava = 4
    water = 5
    ice = 6
    false = 7

class openCloseConsole(Enum):
    open = 1
    close = 2

def main():
    
    #getIngamePos_and_landType()
    
    #while quittingApp == False:
    countdownTimer()
    #recenterNewSquare(baseSquare)
    #water doesnt bring any menus up on good or bad clicks
    hudClick(hudArea.water)
    openCloseInspectConsole(openCloseConsole.open)
    #to prevent typing in console
    hudClick(hudArea.water)
    setUp()
    print("to call create farming squares")
    createFarmingSquares()
    checkForHarvests(600)



def hudClick(hudCommand, time=0.2):
    if hudCommand == hudArea.bag:
        moveClick(120, 970, time)
    if consoleActive == False:
        if hudCommand == hudArea.select:
            moveClick(620, 970, time)
        elif hudCommand == hudArea.shovel:
            moveClick(720, 970, time)
        elif hudCommand == hudArea.plant:
            moveClick(810, 970, time)
        elif hudCommand == hudArea.water:
            moveClick(910, 970, time)
        elif hudCommand == hudArea.scissor:
            moveClick(990, 970, time)
    elif consoleActive == True:
        if hudCommand == hudArea.select:
            moveClick(340, 970, time)
        elif hudCommand == hudArea.shovel:
            moveClick(440, 970, time)
        elif hudCommand == hudArea.plant:
            moveClick(530, 970, time)
        elif hudCommand == hudArea.water:
            moveClick(630, 970, time)
        elif hudCommand == hudArea.scissor:
            moveClick(730, 970, time)

def hudCommands(hudOrder, square=None, flower=None, time =0.2):
    if consoleActive == False:
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
    elif consoleActive == True:
        if hudOrder == hudAction.selectLand:
            hudClick(hudArea.select, True)
            moveClickSquare(square, time)

        if hudOrder == hudAction.tillLand:
            hudClick(hudArea.shovel, True)
            moveClickSquare(square, time)
            
        if hudOrder == hudAction.plantFlower:
            hudClick(hudArea.plant, True)
            moveClickSquare(square)
            plantingMenuClick(flower,time)
            moveClickSquare(square)

        if hudOrder == hudAction.waterLand:
            hudClick(hudArea.water, True)
            moveClickSquare(square, time)

        if hudOrder == hudAction.cutPlant:
            hudClick(hudArea.scissor, True)
            moveClickSquare(square, time)

def bagClick(bagCommand, time=0.2):
    if consoleActive == False:
        if bagCommand == bagArea.map:
            moveClick(725, 317, time)
        if bagCommand == bagArea.inventory:
            moveClick(935, 316, time)
        if bagCommand == bagArea.flowers:
            moveClick(1148, 318, time)
        if bagCommand == bagArea.exit:
            moveClick(1277, 319, time)
    elif consoleActive == True:
        if bagCommand == bagArea.map:
            moveClick(444, 317, time)
        if bagCommand == bagArea.inventory:
            moveClick(658, 316, time)
        if bagCommand == bagArea.flowers:
            moveClick(858, 318, time)
        if bagCommand == bagArea.exit:
            moveClick(1000, 319, time)


def flowerMenuClick(flowerCommand, time=0.2):
    if consoleActive == False:
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
    elif consoleActive == True:
        if flowerCommand == flowerArea.tile1:
            moveClick(420, 420, time)
        if flowerCommand == flowerArea.tile2:
            moveClick(680, 420, time)
        if flowerCommand == flowerArea.tile3:
            moveClick(920, 420, time)

        if flowerCommand == flowerArea.tile4:
            moveClick(420, 520, time)
        if flowerCommand == flowerArea.tile5:
            moveClick(680, 520, time)
        if flowerCommand == flowerArea.tile6:
            moveClick(920, 520, time)

        if flowerCommand == flowerArea.tile7:
            moveClick(420, 620, time)
        if flowerCommand == flowerArea.tile8:
            moveClick(680, 620, time)
        if flowerCommand == flowerArea.tile9:
            moveClick(920, 620, time)

        if flowerCommand == flowerArea.tile10:
            moveClick(420, 720, time)
        if flowerCommand == flowerArea.tile11:
            moveClick(680, 720, time)
        if flowerCommand == flowerArea.tile12:
            moveClick(920, 720, time)

        if flowerCommand == flowerArea.skipToStart:
            moveClick(352, 787, time)
        if flowerCommand == flowerArea.skipForward:
            moveClick(985, 787, time)
        if flowerCommand == flowerArea.skipBackward:
            moveClick(376, 787, time)
        if flowerCommand == flowerArea.skipToEnd:
            moveClick(1010, 787, time)

        if flowerCommand == flowerArea.rarity:
            moveClick(394, 360, time)
        if flowerCommand == flowerArea.land:
            moveClick(500, 360, time)
        if flowerCommand == flowerArea.planted:
            moveClick(574, 360, time)
        if flowerCommand == flowerArea.network:
            moveClick(680, 360, time)
        if flowerCommand == flowerArea.sort:
            moveClick(866, 360, time)
        if flowerCommand == flowerArea.scending:
            moveClick(938, 360, time)

def plantingMenuClick(plantingCommand, time = 0.2):
    if consoleActive == False:
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
        if plantingCommand == flowerArea.tile10:
            moveClick(880, 640, time)
        if plantingCommand == flowerArea.tile11:
            moveClick(1049, 640, time)
        if plantingCommand == flowerArea.tile12:
            moveClick(1195, 640, time)

        if plantingCommand == bagArea.exit:
            moveClick(1316,333, time)
    if consoleActive == True:
        if plantingCommand == flowerArea.tile1:
            moveClick(395, 470, time)
        if plantingCommand == flowerArea.tile2:
            moveClick(585, 470, time)
        if plantingCommand == flowerArea.tile3:
            moveClick(763, 470, time)
        if plantingCommand == flowerArea.tile4:
            moveClick(930, 470, time)

        if plantingCommand == flowerArea.tile5:
            moveClick(395, 562, time)
        if plantingCommand == flowerArea.tile6:
            moveClick(585, 562, time)
        if plantingCommand == flowerArea.tile7:
            moveClick(763, 562, time)
        if plantingCommand == flowerArea.tile8:
            moveClick(930, 562, time)

        if plantingCommand == flowerArea.tile9:
            moveClick(690, 640, time)
        if plantingCommand == flowerArea.tile10:
            moveClick(585, 640, time)
        if plantingCommand == flowerArea.tile11:
            moveClick(763, 640, time)
        if plantingCommand == flowerArea.tile12:
            moveClick(930, 640, time)

        if plantingCommand == bagArea.exit:
            moveClick(1090,333, time)   
def setUp():

    moveClick(1682, 141, 0.3)
    pyautogui.write('[board click]')
    hudClick(hudArea.water)
    #0x53 == S key
    print("setting up water position...")
    print("press s key on the position of refill water")

    while True:

        if win32api.GetKeyState(0x53) < 0:
            setupWaterPosition()
            break
        #if win32api.GetKeyState(0x1B) < 0:
        #    quittingApp = True
        #    break
    print("setting up default square...")
    print("find a square you own that has a yellow boarder (typically Smoldering Ground)")
    print("where its corners aren't obstructed from view")
    print(" ")
    print("press s key on this area")

    while True:

        #if win32api.GetKeyState(0x53) < 0 and quittingApp == False:
        if win32api.GetKeyState(0x53) < 0:
            createDefaultSquare()
            #positionToPurpleTop(squareList[1],pyautogui.position()[0], pyautogui.position()[1], squareList[1].height, squareList[1].width, squareList[1].topDiff)
            break

        #if win32api.GetKeyState(0x1B) < 0:
        #    quittingApp = True
        #    break
        #elif quittingApp == True:
            break
def startUp():
    #refresh page
    pyautogui.keyDown("ctrl")
    pyautogui.press("r")
    pyautogui.keyUp("ctrl")
#
    ##save what the refresh IMG looks like
    #refreshIMG = pyautogui.screenshot()
    recordingRefresh()

    #playbackRefresh("refresh_positioning.json")

def openCloseInspectConsole(interaction):
    global consoleActive
    print("called")
    if interaction == openCloseConsole.open:
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("j")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
        
        consoleActive = True
        print("consoleActive bool = true")
    elif interaction == openCloseConsole.close:
        if pyautogui.position()[0] > 100:
            moveClick(pyautogui.position()[0] - 100,pyautogui.position()[1])
        else:
            moveClick(pyautogui.position()[0] + 300,pyautogui.position()[1])
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("j")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
        consoleActive = False
        print("consoleActive bool = False")
def getIngamePos_and_landType():
    pytesseract.tesseract_cmd = "E:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    x_start_point = 1560
    y_start_point = 150
    x_howFar = 39
    y_howFar = 922
    xString = ""
    yString = ""
    landString = ""
    xInt = 0
    yInt = 0

    landString = None
    landEnum = None
    #print("Taking a screenshot...")
    screenshot = pyautogui.screenshot(region=(x_start_point, y_start_point, x_howFar, y_howFar))
    #converting pyautogui screenshot into one that cv2 can read
    open_cv_image = np.array(screenshot) 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    d = pytesseract.image_to_data(open_cv_image, output_type=Output.DICT)
    n_boxes = len(d['level'])
    (x, y, w, h) = (d['left'][-1], d['top'][-1], d['width'][-1], d['height'][-1])
    cv2.rectangle(open_cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #print (x, y, w, h)
    newScreenshot = pyautogui.screenshot(region=(x_start_point, y_start_point + y-2, 170, h+4))
    open_cv_image2 = np.array(newScreenshot) 
     #Convert RGB to BGR 
    open_cv_image2 = open_cv_image2[:, :, ::-1].copy()

    words_in_image = pytesseract.image_to_string(open_cv_image2)
    word_list = words_in_image.split()

    for i in range(len(word_list)):
        if word_list[i] == 'Tile':
            xString = word_list[i + 1]
            yString = word_list[i + 2]
            #landString = word_list[i + 4]

    xClean1 = xString.replace('(', '')
    xClean2 = xClean1.replace(',', '')
    yClean1 = yString.replace(')', '')
    xInt = int(xClean2)
    yInt = int(yClean1)


    if landString == "soil":
        landEnum = landKind.soil
    elif landString == "stone":
        landEnum = landKind.stone
    elif landString == "sand":
        landEnum = landKind.sand
    elif landString == "lava":
        landEnum = landKind.lava
    elif landString == "water":
        landEnum = landKind.water
    elif landString == "ice":
        landEnum = landKind.ice

    print(xInt)
    print(yInt)
    #print(landEnum)
    falseLandEnum = landKind.false

    return xInt, yInt, falseLandEnum

def recordingRefresh():
    recorder.runListeners()
    print("Recording duration: {} seconds".format(recorder.elapsed_time()))

    print(json.dumps(recorder.input_events))

    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 
                            'recordings', 
                            '{}.json'.format(recorder.OUTPUT_FILENAME))
    with open(filepath, 'w') as outfile:
        json.dump(recorder.input_events, outfile, indent=4)
        

def playbackRefresh(filename):
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 
                            'recordings', 
                            filename)
    with open(filepath, 'r') as jsonfile:
        # parse the json
        data = json.load(jsonfile)
        
        #loop over each action
        for index, action in enumerate(data):
            action_start_time = time()
            #loop for escape input to exit
            if action['button'] == 'Key.esc':
                break
            
            #perform the action
            if action['type'] == 'keyDown':
                key = convertKey(action['button'])
                pyautogui.keyDown(key)
            elif action['type'] == 'keyUp':
                key = convertKey(action['button'])
                pyautogui.keyUp(key)
            elif action['type'] == 'clickDown':
                if action['button'] == "Button.left":

                    #move to click down pos
                    pyautogui.moveTo(action['pos'][0], action['pos'][1])

                    #find the clickUp in the actions forward
                    for i in range(9999):
                        #once found
                        try:
                            if data[index + i]['type'] == 'clickUp' and data[index + i]['button'] == 'Button.left':
                                #set it to next action
                                next_action = data[index + i]
                                break
                        except:
                            break
                    #get the amount of time we need to drag ause it
                    elapsed_time = next_action['time'] - action['time']

                    pyautogui.dragTo(next_action['pos'][0], next_action['pos'][1], elapsed_time, button='left')
                elif action['button'] == 'Button.right':
                    #move to click down pos
                    pyautogui.moveTo(action['pos'][0], action['pos'][1])
                    #find the clickUp in the actions forward
                    for i in range(9999):
                        #once found
                        try:
                            if data[index + i]['type'] == 'clickUp' and data[index + i]['button'] == 'Button.right':
                                #set it to next action
                                next_action = data[index + i]
                                break
                        except:
                            break
                    #get the amount of time we need to drag ause it
                    elapsed_time = next_action['time'] - action['time']
                    pyautogui.dragTo(next_action['pos'][0], next_action['pos'][1], elapsed_time, button='right')

                
            
            # then sleep until next action should occur
            try:
                next_action = data[index + 1]
            except IndexError:
                break
            elapsed_time = next_action['time'] - action['time']
            if elapsed_time < 0:
                raise Exception('Unexpected action ordering.')
  
            elapsed_time -=(time() - action_start_time)
            if elapsed_time < 0:
                elapsed_time = 0
            print('sleeping for {}'.format(elapsed_time))
            sleep(elapsed_time)



def convertKey(button):
    PYNPUT_SPECIAL_CASE_MAP = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'caps_lock': 'capslock',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'num_lock': 'numlock',
        'print_screen': 'printscreen',
        'scroll_lock': 'scrolllock',

    }

    # example: 'Key.F9' should return 'F9', 'w' should return as 'w'
    cleaned_key = button.replace('Key.', '')

    if cleaned_key in PYNPUT_SPECIAL_CASE_MAP:
        return PYNPUT_SPECIAL_CASE_MAP[cleaned_key]

    return cleaned_key
def getIngamePosition():
    #take screenshot
    #analyse useful area for last click position text
    #return that position
    pass
def setupWaterPosition():
    pyautogui.click()
    waterSquare = Square
    waterSquare.waterRefillPos = [pyautogui.position()[0],pyautogui.position()[1]]

    ingameX, ingameY, land = getIngamePos_and_landType()
    waterSquare.ingamePos = [ingameX, ingameY]
    waterSquare.landType = land
    waterSquare.isWaterRefill = True
    squareList.append(waterSquare)

    refillWater()

    
def minusWaterCount(num):
    waterCount -num

def resetWaterCount():
    waterCount = 10

def getWaterCount():
    return waterCount

def refillWater(time = 0.5):
    for square in squareList:
        if square.isWaterRefill == True:
            moveClick(square.waterRefillPos[0], square.waterRefillPos[1], time)
            resetWaterCount()

#def checkFirstSquarePos():
#    pyautogui.moveTo(squareList[0].centerPoint)
#    oldCenterPoint = squareList[0].centerPoint
#    #get pos of purple select
#    positionToPurpleTop(squareList[0], pyautogui.position()[0],pyautogui.position()[1],squareList[0].height,squareList[0].width, squareList[0].topDiff)
#    if squareList[0].centerPoint != oldCenterPoint:
#        xDiff = squareList[0].centerPoint[0] - oldCenterPoint[0]
#        yDiff = squareList[0].centerPoint[1] - oldCenterPoint[1]
#
#        for i in range (len(squareList)):
#            if i == 0: continue
#            #set new positions for each squares
#
#            try:
#                squareList[i].centerPoint[0] += xDiff
#                squareList[i].centerPoint[1] += yDiff
#            except:
#                pass
def waitTillPlantsAreLoaded():
    while (True):
        print("waiting for plants to load")
        screenshot = pyautogui.screenshot()
        hudClick(hudArea.select)
        moveClick(squareList[1].centerPoint[0], squareList[1].centerPoint[1])
        if screenshot.getpixel((1635, 404)) == (255,255,255):
            break
    pass

def checkForHarvests(timeBeforeCheck = 60):
    #while win32api.GetKeyState(0x51) > -1:
    #print("checking for harvest")
    #refresh the page to avoid memory crash of web browerser
    #print("harvestCheck")
    #pyautogui.keyDown("ctrl")
    #pyautogui.press("r")
    #pyautogui.keyUp("ctrl")
    #sleep to wait for the game to load
    #sleep(20)
    #move back to where we were 
    #hudClick(hudArea.water)
    #waitTillPlantsAreLoaded()
    #onRefreshFindFarm()
    
    print("Doing farming checks")
    for i in range(len(squareList)):
        if i == 0: continue
        if squareList[i].harvestClock == 0:
            harvestQueue.append(squareList[i])
            
        print("harvest queue: (just added)",len(harvestQueue))
    currentHarvestQueue = harvestQueue
    currentPlantingQueue = plantingQueue
    harvestQueue.clear
    plantingQueue.clear
    for i in range (len(currentHarvestQueue)):
        harvestFlower(currentHarvestQueue[i])
        #print("harvesting ", i)
    print("harvest queue: (done)",len(currentHarvestQueue))
    print("planting queue: (just added)",len(currentPlantingQueue))
    currentHarvestQueue.clear
    for i in range (len(currentPlantingQueue)):
        plantFlower(currentPlantingQueue[i])
        #print("planting ", i)
    print("planting queue: (done)",len(currentPlantingQueue))
    currentPlantingQueue.clear
    Timer(timeBeforeCheck, checkForHarvests, args=[timeBeforeCheck]).start()


        #callCheckHarvest(timeBeforeCheck)
    #if win32api.GetKeyState(0x1B) < 0:
        #print("bot is now closing")

def onRefreshFindFarm():
    print("on refresh find farm")
    #click on square
    hudClick(hudArea.water)
    openCloseConsole(openCloseConsole.open)
    hudClick(hudArea.water)
    addNewSquare = Square()
    moveClick(500, 500)
    

    #look at in game pos
    checkingX, checkingY, checkingLand = getIngamePos_and_landType()
    foundMatch = False
    foundMatchSquare = None
    #random first click
    if bottomRightCenterPointDistance == [0,0]:
        print("bottomRightCenterPointDistance")
    if bottomLeftCenterPointDistance == [0,0]:
        print("bottomLeftCenterPointDistance")
    if topRightCenterPointDistance == [0,0]:
        print("topRightCenterPointDistance")
    if topLeftCenterPointDistance == [0,0]:
        print("topLeftCenterPointDistance")
    while True:
        harvestRelignIfSideHit()

        if [checkingX, checkingY] == squareList[2].ingamePos:
            foundMatch = True
            foundMatchSquare = squareList[2]

        if foundMatch == True:
            pyautogui.dragTo(squareList[2].centerPoint[0], squareList[2].centerPoint[1], 1)
            break
        
        else:
            print("to find square")

            

            #top left x is less and y is less
            if checkingX < squareList[2].ingamePos[0] and checkingY < squareList[2].ingamePos[1]:
                moveClick(pyautogui.position()[0] + bottomRightCenterPointDistance[0], pyautogui.position()[1] + bottomRightCenterPointDistance[1])
                pyautogui.click()
                checkingX, checkingY, checkingLand = getIngamePos_and_landType()
            
            #top right x is greater y is less
            if checkingX > squareList[2].ingamePos[0] and checkingY < squareList[2].ingamePos[1]:
                moveClick(pyautogui.position()[0] + bottomLeftCenterPointDistance[0], pyautogui.position()[1] + bottomLeftCenterPointDistance[1])
                pyautogui.click()
                checkingX, checkingY, checkingLand = getIngamePos_and_landType()
            #bottom left x is less and y is greater
            if checkingX < squareList[2].ingamePos[0] and checkingY > squareList[2].ingamePos[1]:
                moveClick(pyautogui.position()[0] + topRightCenterPointDistance[0], pyautogui.position()[1] + topRightCenterPointDistance[1])
                pyautogui.click()
                checkingX, checkingY, checkingLand = getIngamePos_and_landType()
            #bottom right x is greater y is greater
            if checkingX > squareList[2].ingamePos[0] and checkingY > squareList[2].ingamePos[1]:
                moveClick(pyautogui.position()[0] + topLeftCenterPointDistance[0], pyautogui.position()[1] + topLeftCenterPointDistance[1])
                pyautogui.click()
                checkingX, checkingY, checkingLand = getIngamePos_and_landType()

def harvestRelignIfSideHit():
    print("checking relign side hit")
        #if left side
    if pyautogui.position()[0] < 127:
        #if top left
        if pyautogui.position()[1] <= 530:
            pyautogui.dragTo(1187,849, 2)
        #if bottom left
        if pyautogui.position()[1] > 530:
            pyautogui.dragTo(1315, 207, 2)
    #if right side
    if pyautogui.position()[0] > 1385: 
        # if top right
        if pyautogui.position()[1] <= 530:
            pyautogui.dragTo(250, 927, 2)
        # if bottom right
        elif pyautogui.position()[1] > 530:
            pyautogui.dragTo(213, 221, 2)
    #if top side
    if pyautogui.position()[1] < 127:
        #if top left
        if pyautogui.position()[0] <= 717:
            pyautogui.dragTo(1165, 951, 2)
        #if top right
        elif pyautogui.position()[0] > 717:
            pyautogui.dragTo(250, 927, 2)
            
    #if bottom side
    if pyautogui.position()[1] > 970 :
        #if bottom left
        if pyautogui.position()[0] <= 717:
            pyautogui.dragTo(1315, 207, 2)
        #if bottom right
        elif pyautogui.position()[0] > 717:
            pyautogui.dragTo(213, 221, 2)
    
def harvesting():
    if len(harvestQueue) != 0:
        harvestFlower(harvestQueue[0])

def removeLastHarvestedFromQueue():
    print("removing from harvesting queue")
    del harvestQueue[0]
def removeLastPlantedFromQueue():
    print("removing from planting queue")
    del plantingQueue[0]

def harvestFlower(square):

    #click scissors
    hudClick(hudArea.scissor)
    #click square that needs to be harvest
    #moveClick(SqCenterPoint(square))
    moveClick(square.centerPoint[0], square.centerPoint[1])
    #wait to see if pop up comes up
    #if it does click harvest
    screenshot = pyautogui.screenshot()
    #green harvest button is at x900, y574
    sleep(0.5)
    if consoleActive:
        if screenshot.getpixel((647,578)) == (120,210,130):
            moveClick(647,578)
        elif screenshot.getpixel((677,496)) == (120,210,130):
            moveClick(761,567)
        
    elif consoleActive == False:
        if screenshot.getpixel((874,572)) == (120,210,130):
            print("called click harvest")
            moveClick(900, 574)
        #if clear land comes up
        elif screenshot.getpixel((888, 574)) == (120,210,130):
            print("called cancel clear land")
            moveClick(1000, 572)

 
    
    square.needsHarvest = False
    print("adding to planting queue from harvestFlower")
    plantingQueue.append(square)


    #removeLastHarvestedFromQueue
    #done         

def plantFlower(square, tile = flowerArea.tile1):
    haveWater = False
    moveToWater = False
    #click hud shovel
    
    hudClick(hudArea.shovel)
    #till land
    moveClick(square.centerPoint[0], square.centerPoint[1])
    #click hud plant

    hudClick(hudArea.plant)
    #click land
    moveClick(square.centerPoint[0], square.centerPoint[1], 1)

    print("check for pixels")
    #check if area menu screen to select plant is present
    sleep(1.5)
    screenshot = pyautogui.screenshot()

    if screenshot.getpixel((732,365)) == (255,255,255):
        while(True):
            screenshot = pyautogui.screenshot()
        
            #if no flowers (vist flower market button pops up)
            if consoleActive:
                if screenshot.getpixel((657,686)) == (120, 210, 130):
                    plantingMenuClick(bagArea.exit, 0.2)
                    moveToWater = True
                elif screenshot.getpixel((405,466)) != (255,255,255):
                    #click tile
                    plantingMenuClick(tile)
                    #check id
                    #apply stats to lands
                    #if cannot find ID or get stats default to 1 hour for harvest clock
                    square.harvestTime = 60
                    square.harvestClock = square.harvestTime
                    thread = timerThread.myThread(square)
                    thread.start()
                    #thread.join()
                    #check for harvest cutscene
                    seconds = 5
                

                    for i in range(seconds):
                        screenshot = pyautogui.screenshot()

                        if screenshot.getpixel((204,105)) == (0,23,59) and screenshot.getpixel((1143,114)) == (0,23,10):
                            moveClick(345,271)

                        sleep(1)
                moveToWater = True
            if consoleActive == False:
                if screenshot.getpixel((878, 700)) == (120, 210, 130):
                    plantingMenuClick(bagArea.exit, 0.2)
                    moveToWater = True
                elif screenshot.getpixel((680, 492)) != (255,255,255):
                    plantingMenuClick(tile)

                    square.harvestTime = 60
                    square.harvestClock = square.harvestTime

                    thread = timerThread.myThread(square)
                    thread.start()
                    #thread.join()
    
                    seconds = 5

                    for i in range(seconds):
                        screenshot = pyautogui.screenshot()

                        if screenshot.getpixel((579, 103)) == (90,207,148) and screenshot.getpixel((1725, 248)) == (166,212,105):
                            moveClick(345,271)

                        sleep(1)
                    moveToWater = True

            if(moveToWater):
                #click water icon
                hudClick(hudArea.water)
                #click sqaure
                moveClick(square.centerPoint[0], square.centerPoint[1])
                minusWaterCount(1)
                if getWaterCount() <= 0:
                    refillWater()
                    resetWaterCount()
                    haveWater = True
            
            if moveToWater and haveWater:
                break

def checkForPixels(center, xFar, yFar, pixelRGB = (255, 255, 255)):

    screenshot = pyautogui.screenshot()
    #pyautogui.moveTo(center[0],center[1], 0.2)
    for x in range(pyautogui.position()[0] - xFar, 
                   pyautogui.position()[0] + xFar ):

        for y in range(pyautogui.position()[1] - yFar, 
                       pyautogui.position()[1] + yFar):

            if screenshot.getpixel((x, y)) == pixelRGB:
                #print("pixel colours of x and y = ", screenshot.getpixel((x, y)))
                return True
            else:
                return False


def moveClick(x, y, time=0.2):
    print("in move click")
    print(x,y)
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

def createDefaultSquare():
    #must left click then call this function to work
    newDefaultSquare = Square()

    calculateOutgameDefaultSquarePos(newDefaultSquare)
    pyautogui.click()
    landXPos, landYPos, landType = getIngamePos_and_landType()
    newDefaultSquare.ingamePos = [landXPos, landYPos]
    newDefaultSquare.landType = landType
    newDefaultSquare.centerPoint = SqCenterPoint(newDefaultSquare)
    squareList.append(newDefaultSquare)

    #print('left side: ', newDefaultSquare.leftPoint)
    #print('top side: ', newDefaultSquare.topPoint)
    #print('right side: ', newDefaultSquare.rightPoint)
    #print('bottom side: ', newDefaultSquare.bottomPoint)
#
    #print ('newDefaultSquare ingame pos: ', newDefaultSquare.ingamePos)
    #print ('newDefaultSquare landType: ', newDefaultSquare.landType)

           
def calculateOutgameDefaultSquarePos(square):
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
    pyautogui.mouseUp(button='left')
    pyautogui.moveTo(543,1060)
    screenshot = pyautogui.screenshot()

    #from saved mouse pos search for right side

    for i in range(9999):
        if screenshot.getpixel((savedMousePositon[0] + i, savedMousePositon[1])) != boarderRGB:
            currentRightSide = [savedMousePositon[0] + i, savedMousePositon[1]]
            #pyautogui.moveTo(currentRightSide)
        else:
            break


    above = [currentRightSide[0], currentRightSide[1]]
    below = [currentRightSide[0], currentRightSide[1]]

    #above
    for i in range(9999):
        if screenshot.getpixel((currentRightSide[0], currentRightSide[1]-i)) != boarderRGB:
            above = [currentRightSide[0], currentRightSide[1]-i]
            #pyautogui.moveTo(above)
        else: 
            break
    #below        
    for i in range(9999):
        if screenshot.getpixel((currentRightSide[0], currentRightSide[1]+i)) != boarderRGB:
            below = [currentRightSide[0], currentRightSide[1]+i]
           # pyautogui.moveTo(below)
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
   # print("distXRL: ", distXRL)
    divXRL = distXRL/2

    #print("divXRL: ", math.floor(divXRL))
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
    #for j in range(9999):
        #if screenshot.getpixel((currentTopSide[0]-1,currentTopSide[1])) !=boarderRGB:
            #currentTopSide[0]-=1

        #else:
            #break
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
            #pyautogui.moveTo(currentBottomSide[0], currentBottomSide[1], 0.001)
        else:
            break   
    innerBottomSide = currentBottomSide
    #print("innerLeft: ", innerLeftSide)
    square.innerLeft = innerLeftSide
    square.innerTop = innerTopSide
    square.innerRight = innerRightSide
    square.innerBottom = innerBottomSide
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
            #pyautogui.moveTo(currentOuterTop[0], currentOuterTop[1], 2)
            
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
            pyautogui.moveTo(currentOuterBottom[0], currentOuterBottom[1], 0.001)
        else:
            break
    #finalBottomSide = currentOuterBottom
    #pyautogui.moveTo(currentOuterBottom[0],currentOuterBottom[1])
    distLeft = innerLeftSide[0] - currentOuterLeft[0] 
    distTop = innerTopSide[1] - currentOuterTop[1] 
    distRight = currentOuterRight[0] - innerRightSide[0] 
    distBottom = currentOuterBottom[1] - innerBottomSide[1] 

    #print("distLeft: ", distLeft)
    #print("distTop: ", distTop)
    #print("distRight: ", distRight)
    #print("distBottom: ", distBottom)
    # divide by 2 and thats the boarder number
    distLeft = distLeft/2
    distTop = distTop/2
    distRight = distRight/2
    distBottom = distBottom/2

    
    #add this with the correct side and this is the total number, create a sqaure with this
    finalLeftSide = [innerLeftSide[0] - distLeft, innerLeftSide[1]]
    finalTopSide = [innerTopSide[0], innerTopSide[1] - distTop]
    finalRightSide = [innerRightSide[0] + distRight, innerRightSide[1]]
    finalBottomSide = [innerBottomSide[0], innerBottomSide[1] + distBottom]

    #pyautogui.moveTo(finalTopSide)
    #finalLeftSide[0] = round(finalLeftSide[0])
    #finalTopSide[0] = round(finalTopSide[0])
    #finalBottomSide[0] = round(finalBottomSide[0])

    #pyautogui.moveTo(finalLeftSide[0], finalLeftSide[1], 5)
    #pyautogui.moveTo(finalTopSide[0], finalTopSide[1], 5)
    #pyautogui.moveTo(finalRightSide[0], finalRightSide[1], 5)
    #pyautogui.moveTo(finalBottomSide[0], finalBottomSide[1], 5)
    #pyautogui.moveTo(finalBottomSide[0], finalBottomSide[1], 0.001)

    #print("finalRight before", finalRightSide)

    #height = finalLeftSide[1] - finalTopSide[1]
    #square.height = height * 2
###
    #width = finalTopSide[0] = finalLeftSide[0]
    #square.width = width * 2

    #print("finalRight after", finalRightSide)
    pyautogui.moveTo(savedMousePositon)
    square.setPoints(finalLeftSide, finalTopSide, finalRightSide, finalBottomSide)
    
def createFarmingSquares():
    canPlace = True
    while True:
        #s key
        if win32api.GetKeyState(0x53) < 0 and canPlace == True:
            canPlace = False
            #if mouse is next to i square get dir
            for i in range(len(squareList)):
                if i == 0: continue

                squarePosEnum, testSquare = isMouseInNewSquarePos(pyautogui.position()[0], pyautogui.position()[1], squareList[i])
                if squarePosEnum != SquarePos.false_position:

                    #print (squarePosEnum)

                    print(i)
                    addNewSquare(squareList[i], testSquare, squarePosEnum)
                    break   

        if win32api.GetKeyState(0x53) > -1 and canPlace == False:
            print("center: ", squareList[-i].centerPoint)
            print("leftside: ", squareList[-i].leftPoint)
            cv.destroyAllWindows()
            drawDiamonds(blank)
            cv.waitKey(1)
            canPlace = True   
            
        #q key
        if win32api.GetKeyState(0x51) < 0: 
            print('finished setting up farming positions')
            break  
        
        #if win32api.GetKeyState(0x1B) < 0:
        #    quittingApp = True
        #    break

        #break

def testIngamePos(oldSquare, newSquare):
    outCome = [0,0]

    moveClick(oldSquare.centerPoint[0], oldSquare.centerPoint[1], 0)
    oldX, oldY, oldLand = getIngamePos_and_landType()


    moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1], 0)
    newX, newY, newLand = getIngamePos_and_landType()
    
    outCome = [oldX - newX, oldY - newY]
    #print("outcome: ", outCome)
    return outCome, newX, newY, newLand


def addNewSquare(oldSquare, newSquare, squarePosEnum):
    #if squarePosEnum == desiredEnum:
    newSquare.centerPoint = SqCenterPoint(newSquare)
    ingameCompare, newX, newY, newLand = testIngamePos(oldSquare, newSquare)

    leftDist = squareList[1].innerLeft[0] - squareList[1].innerLeft[0]
    topDist = squareList[1].innerTop[1] - squareList[1].topPoint[1]
    rightDist = squareList[1].rightPoint[0] - squareList[1].innerRight[0]
    bottomDist = squareList[1].bottomPoint[1] - squareList[1].innerBottom[1]
    
    newSquare.innerLeft = [newSquare.leftPoint[0] - leftDist, newSquare.leftPoint[1]]
    newSquare.innerTop = [newSquare.topPoint[0], newSquare.topPoint[1] - topDist]
    newSquare.innerRight = [newSquare.rightPoint[0] - rightDist, newSquare.rightPoint[1]]
    newSquare.innerBottom = [newSquare.bottomPoint[0], newSquare.bottomPoint[1] - bottomDist]

    
    #heightT = newSquare.rightPoint[1] - newSquare.topPoint[1]
    #topDiffT = heightT
    #heightT = heightT * 2
    ##
####
    #widthT = newSquare.topPoint[0] = newSquare.rightPoint[0]
    #widthT = widthT * 2
    #positionToPurpleTop(newSquare, pyautogui.position()[0], pyautogui.position()[1], height, width,topDiff)

    if squarePosEnum == SquarePos.top_left or squarePosEnum == SquarePos.top_right:
        correctIngameDif = 1
    elif squarePosEnum == SquarePos.bottom_left or squarePosEnum == SquarePos.bottom_right:
        correctIngameDif = -1
    
    if ingameCompare[1] == correctIngameDif:

        newSquare.ingamePos = [newX, newY]
        newSquare.landType = newLand

        #height = newSquare.leftPoint[1] - newSquare.topPoint[1]
        #newSquare.height = height * 2
##
        #width = newSquare.topPoint[0] = newSquare.leftPoint[0]
        #newSquare.width = width * 2
        
        #positionToPurpleTop(newSquare, topDist, pyautogui.position()[0], pyautogui.position()[1])
        #testHeightWidth(newSquare)
        
        #have a function that finds the top of the inner with purple outline
        #by how much we move the squares inner, move the other points
        #using the distance between the inner and outer for each point
        #add the other points based on that

        #recenterNewSquare(newSquare)
        #SqCenterPoint(newSquare)
        #pyautogui.moveTo(newSquare.centerPoint)
        squareList.append(newSquare)
        #print("Sqaure has been appened")
        global topLeftCenterPointDistance
        global topRightCenterPointDistance
        global bottomLeftCenterPointDistance
        global bottomRightCenterPointDistance
        
        if squarePosEnum == SquarePos.top_left and topLeftCenterPointDistance == [0,0]:
            topLeftCenterPointDistance = [oldSquare.centerPoint[0] - newSquare.centerPoint[0], oldSquare.centerPoint[1] - newSquare.centerPoint[1]]
        
        elif squarePosEnum == SquarePos.top_right and topRightCenterPointDistance == [0,0]:
            topRightCenterPointDistance = [oldSquare.centerPoint[0] - newSquare.centerPoint[0], oldSquare.centerPoint[1] - newSquare.centerPoint[1]]
        
        elif squarePosEnum == SquarePos.bottom_left and bottomLeftCenterPointDistance == [0,0]:
            bottomLeftCenterPointDistance = [oldSquare.centerPoint[0] - newSquare.centerPoint[0], oldSquare.centerPoint[1] - newSquare.centerPoint[1]]
        
        elif squarePosEnum == SquarePos.bottom_right and bottomRightCenterPointDistance == [0,0]:
            bottomRightCenterPointDistance = [oldSquare.centerPoint[0] - newSquare.centerPoint[0], oldSquare.centerPoint[1] - newSquare.centerPoint[1]]

def recenterNewSquare(square):
    screenshot = pyautogui.screenshot()
    purpleRGB = (166, 107, 208)

    newMouseX = pyautogui.position()[0]
    newMouseY = pyautogui.position()[1]

    #move up until we hit purple
    for i in range(9999):
        if screenshot.getpixel((newMouseX, newMouseY-1)) != purpleRGB:
            newMouseY -=1
            #print(1)
            #pyautogui.moveTo(newMouseX, newMouseY, 0.001)

    #decide what side we are one 
        if screenshot.getpixel((newMouseX, newMouseY-1)) == purpleRGB:
            beforeX = newMouseX
            beforeY = newMouseY
            parkX1 = 0
            parkX2 = 0
            parkXSize = 0
            rightSide = pyautogui.position()[0]
            leftSide = pyautogui.position()[0]
            for i in range(9999):
                if screenshot.getpixel((rightSide+1, newMouseY)) != purpleRGB:
                    rightSide += 1
                    #pyautogui.moveTo(rightSide,newMouseY, 0.001)
                if screenshot.getpixel((rightSide+1, newMouseY)) == purpleRGB:
                    break
            for i in range(9999):
                if screenshot.getpixel((leftSide-1, newMouseY)) != purpleRGB:
                    leftSide -= 1
                    #pyautogui.moveTo(leftSide,newMouseY, 0.001)
                if screenshot.getpixel((leftSide-1, newMouseY)) == purpleRGB:
                    break
            
            leftCheck = newMouseX - leftSide
            rightCheck = rightSide - newMouseX

            print("leftside: ", leftSide)
            print("rightside: ", rightSide)

            print("leftcheck: ", leftCheck)
            print("rightCheck :", rightCheck)
            break
    
    if leftCheck < rightCheck:
        for i in range(9999):
            for k in range(9999):
                if screenshot.getpixel((newMouseX, newMouseY-1)) == purpleRGB and screenshot.getpixel((newMouseX+1, newMouseY )) != purpleRGB:
                    newMouseX += 1

                    #pyautogui.moveTo(newMouseX,newMouseY, 0.001)
                    
                else: 
                    break
            for j in range(9999):
                if screenshot.getpixel((newMouseX, newMouseY-1)) != purpleRGB:
                    newMouseY -= 1

                    #pyautogui.moveTo(newMouseX,newMouseY, 0.001)

                else:
                    break
    #put in parking spot (center position)
    parkX1 = newMouseX
    parkX2 = newMouseX
    for i in range(9999):
            if screenshot.getpixel((parkX1-1, newMouseY)) != purpleRGB:
                parkX1 -= 1

            if screenshot.getpixel((parkX1-1, newMouseY)) == purpleRGB:
 
                break
    for i in range(9999):
            if screenshot.getpixel((parkX2+1, newMouseY)) != purpleRGB:

                parkX2 += 1
            if screenshot.getpixel((parkX2+1, newMouseY)) == purpleRGB:

                break
    parkXSize = parkX2 - parkX1
    if (parkXSize % 2) == 0:
        newMouseX = (parkXSize / 2) + parkX1
    else:
        newMouseX = parkX1 + math.floor(parkXSize / 2)

    #pyautogui.moveTo((newMouseX, newMouseY))

    if rightCheck < leftCheck:
        for i in range(9999):
            for k in range(9999):
                if screenshot.getpixel((newMouseX, newMouseY-1)) == purpleRGB and screenshot.getpixel((newMouseX-1, newMouseY )) != purpleRGB:
                    newMouseX -= 1
                    #pyautogui.moveTo(newMouseX,newMouseY, 0.001)
                else: 
                    break
            for j in range(9999):
                try:
                    if screenshot.getpixel((newMouseX, newMouseY-1)) != purpleRGB:
                        newMouseY -= 1
                        #pyautogui.moveTo(newMouseX,newMouseY, 0.001)
                except:
                    pass
                else:
                    break
    #put in parking spot (center position)
    parkX1 = newMouseX
    parkX2 = newMouseX
    for i in range(9999):
            if screenshot.getpixel((parkX1-1, newMouseY)) != purpleRGB:
                parkX1 -= 1
            if screenshot.getpixel((parkX1-1, newMouseY)) == purpleRGB:
                break
    for i in range(9999):
            if screenshot.getpixel((parkX2+1, newMouseY)) != purpleRGB:
                parkX2 += 1
            
            if screenshot.getpixel((parkX2+1, newMouseY)) == purpleRGB:
                break
    parkXSize = parkX2 - parkX1
    if (parkXSize % 2) == 0:

        newMouseX = (parkXSize / 2) + parkX1
    else:
        newMouseX = parkX1 + math.floor(parkXSize / 2)

        #pyautogui.moveTo((newMouseX, newMouseY))

    xDiff = square.innerTop[0] - newMouseX
    yDiff = square.innerTop[1] - newMouseY

    square.innerLeft = [square.innerLeft[0] + xDiff, square.innerLeft[1] + yDiff]
    square.innerTop = [square.innerTop[0] + xDiff, square.innerTop[1] + yDiff]
    square.innerRight = [square.innerRight[0] + xDiff, square.innerRight[1] + yDiff]
    square.innerBottom = [square.innerBottom[0] + xDiff, square.innerBottom[1] + yDiff]
       
def isMouseInNewSquarePos(x, y, oldSquare):
    testSquare = Square()
    #print ("testSquare right point", testSquare.rightPoint)
    #testSquare.realSquare = True
    #squareList.append(testSquare)
#top right
    squarePosition = SquarePos.false_position
    
    #print (x)
#top right
    if x > oldSquare.topPoint[0] and y < oldSquare.rightPoint[1]:
        squarePosition = testIfMouseIsWithinLogic(x, y, testSquare, oldSquare, SquarePos.top_right)
#top left
    elif x < oldSquare.topPoint[0] and y < oldSquare.rightPoint[1]:
        squarePosition = testIfMouseIsWithinLogic(x, y, testSquare, oldSquare, SquarePos.top_left)
        pass
    #bottom right
    elif x > oldSquare.topPoint[0] and y > oldSquare.rightPoint[1]:
        squarePosition = testIfMouseIsWithinLogic(x, y, testSquare, oldSquare, SquarePos.bottom_right)
        
    #bottom left
    elif x < oldSquare.topPoint[0] and y > oldSquare.rightPoint[1]:
        squarePosition = testIfMouseIsWithinLogic(x, y, testSquare, oldSquare, SquarePos.bottom_left)

    return squarePosition, testSquare

def testIfMouseIsWithinLogic(x, y, testSquare, oldSquare, squarePos):
        positionNextSquare(testSquare, oldSquare, squarePos)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point):
            return squarePos
        else:
            return SquarePos.false_position
def calculateHowManyFakeSqaures(posDir, x, y):
    howMany = 0
    #testSquare = Square
    point = Point(x,y)
    pass
    #addSqaure(posDir, baseSquare, False, (120, 255, 72))
    shapelySquare = Polygon([squareList[-1].leftPoint, squareList[-1].topPoint, squareList[-1].rightPoint, squareList[-1].bottomPoint])
    for i in range(99):
        
        howMany +=1 
        #print ("howmany: ", howMany)
        if shapelySquare.contains(point):
            for i in range (howMany):
                squareList.pop()
                print(len(squareList))
            break
        elif howMany >= 20:
            #print("how many hit 20")
            #addSqaure(posDir, baseSquare, False, (120, 255, 72))
            #shapelySquare = Polygon([squareList[-1].leftPoint, squareList[-1].topPoint, squareList[-1].rightPoint, squareList[-1].bottomPoint])
            break
        else:
            pass
            #addSqaure(posDir, baseSquare, False, (120, 255, 72))
            shapelySquare = Polygon([squareList[-1].leftPoint, squareList[-1].topPoint, squareList[-1].rightPoint, squareList[-1].bottomPoint])
        

    #print (len(squareList))
    return howMany
def isNextSquareNextToLast(x,y):
    #top right
    testSquare = Square()
    testSquare.realSquare = True
    squareList.append(testSquare)
    squarePosition = None
    
    #print(len(squareList))
    if x > squareList[-2].topPoint[0] and y < squareList[-2].rightPoint[1]:
        squarePosition = SquarePos.top_right
        positionNextSquareEnd(testSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point):
            #print(shapelySquare.contains(point), squarePosition) 
            squareList.pop()           
            return shapelySquare.contains(point), squarePosition


    #top left
    if x < squareList[-2].topPoint[0] and y < squareList[-2].rightPoint[1]:
        squarePosition = SquarePos.top_left
        positionNextSquareEnd(testSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point):
            #print(shapelySquare.contains(point), squarePosition)
            squareList.pop()
            return shapelySquare.contains(point), squarePosition
        
    #bottom right
    if x > squareList[-2].topPoint[0] and y > squareList[-2].rightPoint[1]:
        squarePosition = SquarePos.bottom_right
        positionNextSquareEnd(testSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point):      
            #print(shapelySquare.contains(point), squarePosition) 
            squareList.pop() 
            return shapelySquare.contains(point), squarePosition
        
    #bottom left
    if x < squareList[-2].topPoint[0] and y > squareList[-2].rightPoint[1]:
        squarePosition = SquarePos.bottom_left
        positionNextSquareEnd(testSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point): 
            #print(shapelySquare.contains(point), squarePosition)
            squareList.pop()
            return shapelySquare.contains(point), squarePosition

    else:
        #print(False, squarePosition)
        squareList.pop()
        return False, squarePosition
        
def drawDiamonds(canvas):
    drawAllDiamonds(blank)
    cv.imshow('1 sqaure', blank)


def getMax_X_ValueInY(RGB, listOfPixels):
    for i in range (len(listOfPixels)):
        print ("rgb: ",listOfPixels[i])         


def addMultipleSqaures (posDir, baseSquare, multiple, colour):
    for i in range(multiple):
        pass
        #addSqaure(posDir, baseSquare, True, colour)
        

def addMultipleSqauresWithFakes(posDir, baseSquare, multiple, colour):
    for i in range(multiple):
        if i+1 != multiple:
            pass
            #addSqaure(posDir, baseSquare, False, (232,162,0))
        if i+1 == multiple:
            pass
            #addSqaure(posDir, baseSquare, True, colour)
    #for i in range (len(squareList)):
    #    if squareList[i-1].realSquare == False:
    #        squareList.pop(i-1)


def positionToPurpleTop(square, topDiff, mouseX, mouseY, howFast = 0.6):
    #print("in posiiton to purple")
    height = square.leftPoint[1] - square.topPoint[1]
   
    height = height * 2

    print("topdiff before ", topDiff)
    print("innertop square 2", squareList[1].innerTop)
    print ("Top point: ", square.topPoint)
    print ("inner top: ", square.innerTop)
    #topDiff = [square.innerTop[0] - square.topPoint]
 ###,
    width = square.topPoint[0] - square.leftPoint[0]
    square.width = width * 2

    pyautogui.moveTo(mouseX, mouseY, howFast)
    screenshot = pyautogui.screenshot()
    purpleRGB = (166, 107, 208)

    leftDist = square.innerLeft[0] - square.leftPoint[0]
    topDist = square.innerTop[1] - square.topPoint[1]
    rightDist = square.rightPoint[0] - square.innerRight[0]
    bottomDist = square.bottomPoint[1] - square.innerBottom[1]

    topLeftDist = square.topPoint[0] - square.leftPoint[0]

    #mouseX, mouseY = pyautogui.position()

    for i in range(9999):
        if screenshot.getpixel((mouseX, mouseY-1)) != purpleRGB:
            mouseY -=1
            print(1)
            #pyautogui.moveTo(mouseX, mouseY, 0.001)

        if screenshot.getpixel((mouseX, mouseY-1)) == purpleRGB:
            beforeX = mouseX
            beforeY = mouseY
            parkX1 = 0
            parkX2 = 0
            parkXSize = 0
            rightSide = 0
            leftSide = 0
            for i in range(9999):
                if screenshot.getpixel((mouseX+1, mouseY)) != purpleRGB:
                    mouseX + 1
                if screenshot.getpixel((mouseX+1, mouseY)) == purpleRGB:
                    rightSide == mouseX
                    break
            for i in range(9999):
                if screenshot.getpixel((mouseX-1, mouseY)) != purpleRGB:
                        mouseX - 1
                if screenshot.getpixel((mouseX+1, mouseY)) == purpleRGB:
                    leftSide == mouseX
                    break
            
            leftCheck = mouseX - leftSide
            rightCheck = rightSide - mouseX
            break

    if leftCheck < rightCheck:
        for i in range(9999):
            for k in range(9999):
                if screenshot.getpixel((mouseX, mouseY-1)) == purpleRGB and screenshot.getpixel((mouseX+1, mouseY )) != purpleRGB:
                    mouseX += 1
                    print(2)
                    #pyautogui.moveTo(mouseX,mouseY, 0.001)
                    #print(1)
                else: 
                    break
            for j in range(9999):
                if screenshot.getpixel((mouseX, mouseY-1)) != purpleRGB:
                    mouseY -= 1
                    print(3)
                    #pyautogui.moveTo(mouseX,mouseY, 0.001)
                    #print(2)
                else:
                    break
    #put in parking spot
        parkX1 = mouseX
        parkX2 = mouseX
        for i in range(9999):
                if screenshot.getpixel((parkX1-1, mouseY)) != purpleRGB:
                    parkX1 -= 1
                if screenshot.getpixel((parkX1-1, mouseY)) == purpleRGB:
                    break
        for i in range(9999):
                if screenshot.getpixel((parkX2+1, mouseY)) != purpleRGB:
                    parkX2 += 1
                if screenshot.getpixel((parkX2+1, mouseY)) == purpleRGB:
                    break
        parkXSize = parkX2 - parkX1

        if (parkXSize % 2) == 0:
            mouseX = (parkXSize / 2) + parkX1
        else:
            mouseX = parkX1 + math.floor(parkXSize / 2)

        print(4)
        pyautogui.moveTo((mouseX, mouseY))
    
    if rightCheck < leftCheck:
        for i in range(9999):
            for k in range(9999):
                if screenshot.getpixel((mouseX, mouseY-1)) == purpleRGB and screenshot.getpixel((mouseX-1, mouseY )) != purpleRGB:
                    mouseX -= 1
                    print(5)
                    #pyautogui.moveTo(mouseX,mouseY, 0.001)
                    #print(1)
                else: 
                    break
            for j in range(9999):
                try:
                    if screenshot.getpixel((mouseX, mouseY-1)) != purpleRGB:
                        mouseY -= 1
                        print(6)
                        #pyautogui.moveTo(mouseX,mouseY, 0.001)
                        #print(2)
                except:
                    pass
                else:
                    break
    #put in parking spot
        parkX1 = mouseX
        parkX2 = mouseX
        for i in range(9999):
                if screenshot.getpixel((parkX1-1, mouseY)) != purpleRGB:
                    parkX1 -= 1
                if screenshot.getpixel((parkX1-1, mouseY)) == purpleRGB:
                    break
        for i in range(9999):
                if screenshot.getpixel((parkX2+1, mouseY)) != purpleRGB:
                    parkX2 += 1
                    
                if screenshot.getpixel((parkX2+1, mouseY)) == purpleRGB:
                    break

        parkXSize = parkX2 - parkX1

        if (parkXSize % 2) == 0:
            mouseX = (parkXSize / 2) + parkX1
        else:
            mouseX = parkX1 + math.floor(parkXSize / 2)
            print(7)
            #pyautogui.moveTo((mouseX, mouseY))


    if screenshot.getpixel((mouseX, mouseY-1)) != purpleRGB:
        mouseY -=1
        print(8)
        #pyautogui.moveTo(mouseX, mouseY, 0.001)

    square.height = height
    square.width = width
    halfHeight = height/2
    halfWidth = width/2

    topBoarder = mouseY - topDiff
    print ("topdiff after: ",topDiff)
  
    square.topPoint = [mouseX, topBoarder]
    #pyautogui.moveTo(mouseX, topBoarder)
    ##print(9)
    ##pyautogui.moveTo(mouseX, topBoarder + halfHeight)
#
    #square.leftPoint = [mouseX - halfWidth, topBoarder+halfHeight]
    #square.rightPoint = [mouseX + halfWidth, topBoarder+halfHeight]
    #square.bottomPoint = [mouseX, topBoarder+height]
    #print("setting centerpoint to ", [mouseX, topBoarder + halfHeight])
    square.centerPoint = [mouseX, topBoarder + halfHeight]
    
    print("centerPoint is now ", square.centerPoint)

def testHeightWidth(newSquare):
    #height = newSquare.leftPoint[1] - newSquare.topPoint[1]
   #
    #height = height * 2
    #topDiff = [newSquare.innerTop[0] - newSquare.topPoint[0], newSquare.innerTop[1] - newSquare.topPoint[1]]
##
    #
    #width = newSquare.topPoint[0] - newSquare.leftPoint[0]
    #width = width * 2
    #height = 0
    height = newSquare.leftPoint[1]
    #topDiff = [0,0]
#
    #width = 0
    #print("height", height)

def positionNextSquare(square, prevSquare, posDir, baseSquare = None):

    if (posDir == SquarePos.top_left):
        LTXdifference = prevSquare.leftPoint[0] - prevSquare.topPoint[0]
        TLYdifference = prevSquare.topPoint[1] - prevSquare.leftPoint[1]

        #setSquarePosFull(square, previousSquare, LTXdifference, TLYdifference)
        square.rightPoint = prevSquare.topPoint
        square.bottomPoint = prevSquare.leftPoint
        
        #topPoint
        #LTXdifference = previousSquare.leftPoint[0] - previousSquare.topPoint[0]
        #TLYdifference = previousSquare.topPoint[1] - previousSquare.leftPoint[1]


        #x
        square.topPoint[0] = prevSquare.topPoint[0] + LTXdifference
        #y
        square.topPoint[1] = prevSquare.topPoint[1] + TLYdifference

        #leftPoint
        #x
        square.leftPoint[0] = prevSquare.leftPoint[0] + LTXdifference
        #y
        square.leftPoint[1] = prevSquare.leftPoint[1] + TLYdifference

    #top right
    if (posDir == SquarePos.top_right):
        RTXdifference = prevSquare.rightPoint[0] - prevSquare.topPoint[0]
        TRYdifference = prevSquare.topPoint[1] - prevSquare.rightPoint[1]


        #setSquarePosFull(square, posDir, previousSquare, RTXdifference, TRYdifference)
        square.leftPoint = prevSquare.topPoint
        square.bottomPoint = prevSquare.rightPoint
    
        #rightPoint

       # x
        square.rightPoint[0] = prevSquare.rightPoint[0] + RTXdifference
       # y
        square.rightPoint[1] = prevSquare.rightPoint[1] + TRYdifference 

        #topPoint
        #x
        square.topPoint[0] = prevSquare.topPoint[0] + RTXdifference 
       # y
        square.topPoint[1] = prevSquare.topPoint[1] + TRYdifference


    #bottom right
    if (posDir == SquarePos.bottom_right):
       square.topPoint = prevSquare.rightPoint
       square.leftPoint = prevSquare.bottomPoint
       
       #rightPoint
       RTXdifference = prevSquare.rightPoint[0] - prevSquare.topPoint[0]
       TLYdifference = prevSquare.topPoint[1] - prevSquare.leftPoint[1]

       #x
       square.rightPoint[0] = prevSquare.rightPoint[0] + RTXdifference
       #y
       square.rightPoint[1] = prevSquare.bottomPoint[1]

       #bottomPoint
       #x
       square.bottomPoint[0] = prevSquare.bottomPoint[0] + RTXdifference
       #y
       square.bottomPoint[1] = prevSquare.bottomPoint[1] - TLYdifference

    #bottom left
    if (posDir == SquarePos.bottom_left):
       square.topPoint = prevSquare.leftPoint
       square.rightPoint = prevSquare.bottomPoint
       
       #leftPoint
       LBXdifference = prevSquare.leftPoint[0] - prevSquare.bottomPoint[0]
       LBYdifference = prevSquare.leftPoint[1] - prevSquare.bottomPoint[1]

       #x
       square.leftPoint[0] = prevSquare.leftPoint[0] + LBXdifference
       #y
       square.leftPoint[1] = prevSquare.bottomPoint[1]

       #bottomPoint
       #x
       square.bottomPoint[0] = prevSquare.bottomPoint[0] + LBXdifference
       #y
       square.bottomPoint[1] = prevSquare.bottomPoint[1] - LBYdifference 

    #pyautogui.moveTo(square.rightPoint[0], square.rightPoint[1], 5)

def positionNextSquareEnd(square, posDir, baseSquare = None):
    previousPos = squareList[1]
    #print ("length", len(squareList))
    #print("prev left", previousPos.leftPoint)
    #print("prev top", previousPos.topPoint)
    #print("prev right", previousPos.rightPoint)
    #print("prev bottom", previousPos.bottomPoint)
    #top left
    if (posDir == SquarePos.top_left):
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

    #top right
    if (posDir == SquarePos.top_right):
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


    #bottom right
    if (posDir == SquarePos.bottom_right):
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

    #bottom left
    if (posDir == SquarePos.bottom_left):
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

    #pyautogui.moveTo(square.rightPoint[0], square.rightPoint[1], 5)

def drawDiamond(img, leftPoint, topPoint, rightPoint, bottomPoint, colour, thickness):

    leftPoint[0] = math.floor(leftPoint[0])
    leftPoint[1] = math.floor(leftPoint[1])

    topPoint[0] = math.floor(topPoint[0])
    topPoint[1] = math.floor(topPoint[1])

    rightPoint[0] = math.floor(rightPoint[0])
    rightPoint[1] = math.floor(rightPoint[1])

    bottomPoint[0] = math.floor(bottomPoint[0])
    bottomPoint[1] = math.floor(bottomPoint[1])

    cv.line(img, leftPoint, topPoint, colour, thickness)
    cv.line(img, topPoint, rightPoint, colour, thickness)
    cv.line(img, rightPoint, bottomPoint, colour, thickness)
    cv.line(img, bottomPoint, leftPoint, colour, thickness)

def drawAllDiamonds(img):
    
    for i, sqaure in enumerate(squareList):
        if i == 0: continue
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
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
class landKind(Enum):
    soil = 1
    stone = 2
    sand = 3
    lava = 4
    water = 5
    ice = 6

class openCloseConsole(Enum):
    open = 1
    close = 2


def main():
    countdownTimer()
    #water doesnt bring any menus up on good or bad clicks
    hudClick(hudArea.water)
    openCloseInspectConsole(openCloseConsole.open)
    #to prevent typing in console
    hudClick(hudArea.water)
    setUp()
    print("to call create farming squares")
    createFarmingSquares()
    #while True:
    #    if win32api.GetKeyState(0x01) < 0:
    #        #sleep(0.3)
    #        #landXPos, landYPos, landType = getIngamePos_and_landType()
    #        #print(landXPos, landYPos, landType)
    #        #pass
    #    if win32api.GetKeyState(0X02) < 0:
    #        openCloseInspectConsole(openCloseConsole.close)
    #        break

#

#
    #print("press s to set default square position")
    #createDefaultSquare(baseSquare)
    #baseSquare.realSquare = True
    #squareList.append(baseSquare)
#
    #createSquarePlan()
#
    #checkForHarvests(600)


def hudClick(hudCommand, time=0.2):
    global consoleActive
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
    global consoleActive
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
    global consoleActive
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
    global consoleActive
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
    global consoleActive
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
            moveClick(1044,305, time)   
def setUp():

    moveClick(1682, 109, 0.3)
    pyautogui.write('[board click]')
    hudClick(hudArea.water)
    #0x53 == S key
    print("setting up water position...")
    print("press s key on the position of refill water")

    while True:
        if win32api.GetKeyState(0x53) < 0:
            setupWaterPosition()
            break
    print("setting up default square...")
    print("find a square you own that has a yellow boarder (typically Smoldering Ground)")
    print("where its corners aren't obstructed from view")
    print(" ")
    print("press s key on this area")

    while True:
        if win32api.GetKeyState(0x53) < 0:

            createDefaultSquare()
            #positionToPurpleTop(squareList[1],pyautogui.position()[0], pyautogui.position()[1], squareList[1].height, squareList[1].width, squareList[1].topDiff)
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
    print("called")
    if interaction == openCloseConsole.open:
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("j")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
        consoleActive = True
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
def getIngamePos_and_landType():
    x_start_point = 1564
    y_start_point = 146

    x_howFar = 39
    y_howFar = 900


    xString = ""
    yString = ""
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
    cv2.imshow("new", open_cv_image2)
    cv2.waitKey(0)

    words_in_image = pytesseract.image_to_string(open_cv_image2)
    word_list = words_in_image.split()
    xString = word_list[1]
    yString = word_list[2]
    landString = word_list[4]

    #print(xString)
    #print(yString)
    #print(landString)

    xClean1 = xString.replace('(', '')
    xClean2 = xClean1.replace(',', '')

    yClean1 = yString.replace(')', '')

    xInt = int(xClean2)
    yInt = int(yClean1)

    print(xInt)
    print(yInt)
    print(landString)

    return xInt, yInt, landString

    
def getIngamePos_and_landTypeOld():
    x = 0
    y = 0

    xInt = 0
    yInt = 0

    landString = None
    landEnum = None
    #print("Taking a screenshot...")
    screenshot = pyautogui.screenshot(region=(1565, 146, 190, 900))

    #converting pyautogui screenshot into one that cv2 can read
    open_cv_image = np.array(screenshot) 
     #Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    #cv2.imshow("s", open_cv_image)
    #cv2.waitKey(0)
    words_in_image = pytesseract.image_to_string(open_cv_image)
    word_list = words_in_image.split()
    print ("words in image")
    print(words_in_image)

    #for i in range(len(words_in_image)):
        #if word_list[i] == ()

    for i in range (len(word_list)):
        
        if word_list[i] == "Tile":
            x = word_list[i+1]
            #print("raw x ", x)
            xClean1 =x.replace('(', '')
            xClean2 = xClean1.replace(' ', '')

            xFullyClean = xClean2.replace(',', '')
            
            xInt = int(xFullyClean)
           
            #print("cleaned x ", xClean3)

            y = word_list[i+2]
            #print("raw y ", y)
            yClean1 = y.replace(' ', '')

            yFullyClean = yClean1.replace(')', '')

            yInt = int(yFullyClean)
            #print("cleaned y ",yClean2)

            try:
                landString = word_list[i+4] 
            except:
                pass
        if landString != None:
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
    print("xInt: ", xInt, " yInt: ", yInt, " landEnum: ", landEnum)
    return xInt, yInt, landEnum    

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

def checkFirstSquarePos():
    pyautogui.moveTo(squareList[0].centerPoint)
    oldCenterPoint = squareList[0].centerPoint
    #get pos of purple select
    positionToPurpleTop(squareList[0], pyautogui.position()[0],pyautogui.position()[1],squareList[0].height,squareList[0].width, squareList[0].topDiff)
    if squareList[0].centerPoint != oldCenterPoint:
        xDiff = squareList[0].centerPoint[0] - oldCenterPoint[0]
        yDiff = squareList[0].centerPoint[1] - oldCenterPoint[1]

        for i in range (len(squareList)):
            if i == 0: continue
            #set new positions for each squares

            try:
                squareList[i].centerPoint[0] += xDiff
                squareList[i].centerPoint[1] += yDiff
            except:
                pass
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
    #print("checking for harvest")

    #refresh the page to avoid memory crash of web browerser
    pyautogui.keyDown("ctrl")
    pyautogui.press("r")
    pyautogui.keyUp("ctrl")
    #sleep to wait for the game to load
    sleep(20)
    #move back to where we were 
    hudClick(hudArea.select)
    playbackRefresh("refresh_positioning.json")
    waitTillPlantsAreLoaded()
    checkFirstSquarePos()
    

    for i in range(len(squareList)):
        if i == 0: continue
        
        if squareList[i].harvestClock == 0:

            harvestQueue.append(squareList[i])
  
    currentHarvestQueue = harvestQueue
    currentPlantingQueue = plantingQueue
    
    harvestQueue.clear
    plantingQueue.clear
    
    for i in range (len(currentHarvestQueue)):
        harvestFlower(currentHarvestQueue[i])
        #print("harvesting ", i)

    currentHarvestQueue.clear

    for i in range (len(currentPlantingQueue)):
        plantFlower(currentPlantingQueue[i])
        #print("planting ", i)
        
    currentPlantingQueue.clear
    Timer(timeBeforeCheck, checkForHarvests, args=[timeBeforeCheck]).start()


    #callCheckHarvest(timeBeforeCheck)

    
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
    sleep(0.5)
    screenshot = pyautogui.screenshot()
    print("pixel colour = ", screenshot.getpixel((732,365)))
    if screenshot.getpixel((732,365)) == (255,255,255):
        print("pixels found")
        while(True):
            screenshot = pyautogui.screenshot()
            print("in loop finding flowers")
            
            #if no flowers (vist flower market button pops up)
            if screenshot.getpixel((878, 700)) == (120, 210, 130):
                print("no flowers")
                plantingMenuClick(bagArea.exit, 0.2)
                moveToWater = True

            elif screenshot.getpixel((680, 492)) != (255,255,255):
                print("found flower")
                #click tile
                plantingMenuClick(tile)
                #check id
                #apply stats to lands
                #if cannot find ID or get stats default to 1 hour for harvest clock

                square.harvestTime = 60
                square.harvestClock = square.harvestTime
                print ("setting timer thread for square")
                thread = timerThread.myThread(square)
                thread.start()
                #thread.join()

                #check for harvest cutscene
                seconds = 4
                
                print("checking for harvest cutscene")
                for i in range(seconds):
                    screenshot = pyautogui.screenshot()
                    print("rgb colour1 ", screenshot.getpixel((579, 103)), " rgb colour2 ",screenshot.getpixel((1725, 248)))
                    if screenshot.getpixel((579, 103)) == (90,207,148) and screenshot.getpixel((1725, 248)) == (166,212,105):
                        moveClick(345,271)
                
                    time.sleep(1)
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
            #pyautogui.moveTo(currentOuterBottom[0], currentOuterBottom[1], 0.001)
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


    #print("finalRight after", finalRightSide)
    pyautogui.moveTo(savedMousePositon)
    square.setPoints(finalLeftSide, finalTopSide, finalRightSide, finalBottomSide)

def createFarmingSquares():
    #while place key is down
    while True:
    #s key
        if win32api.GetKeyState(0x53) < 0:

            for i in range (len(squareList)):
                if i == 0: continue
                try:
                    #print("Length: ", len(squareList))
                    isNextTo, squarePos = isMouseInNewSquarePos(pyautogui.position()[0], pyautogui.position()[1], squareList[i])

                except:
                    pass
                #if mouse position is outside of squares position
                #detect what direction that is
                if isNextTo:
                    if squarePos == squarePos.top_left:
                        #if centerpoint distance hasn't been created for this distance
                        #add square based on the default square

                        if topLeftCenterPointDistance == [0,0]:
                            newSquare = Square()
                            positionNextSquare(newSquare, squareList[i], squarePos.top_left)
                            newSquare.centerPoint = SqCenterPoint(newSquare)


                            moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                            print("top left center == 0,0")
                            ingameX, ingameY, land = getIngamePos_and_landType()

                            newSquare.ingamePos = [ingameX, ingameY]
                            newSquare.landType = land
                            
                            squareList.append(newSquare)
                            


                            topLeftCenterPointDistance[0] = squareList[i].centerPoint[0] - newSquare.centerPoint[0]
                            topLeftCenterPointDistance[1] = squareList[i].centerPoint[1] - newSquare.centerPoint[1]

                            print("success")
                            
                        elif topLeftCenterPointDistance != [0,0]:

                            #confirm with in game pos if its correct

                            potentialOutX = squareList[i].centerPoint[0] - topLeftCenterPointDistance[0]
                            potentialOutY = squareList[i].centerPoint[1] - topLeftCenterPointDistance[1]
                            moveClick(potentialOutX, potentialOutY)
                            print("top left center != 0,0")
                            potentialInX, potentialInY, land = getIngamePos_and_landType()

                            #if so 
                            # add it to the list
                            print("potential in y: ", potentialInY)
                            print("squareList[i].ingamePos[1]-1 ", squareList[i].ingamePos[1]-1)
                            if potentialInY == squareList[i].ingamePos[1]-1:

                                newSquare = Square()
                                positionNextSquare(newSquare, squareList[i], squarePos.top_left)

                                #newSquare.centerPoint = [potentialOutX, potentialOutY]
                                newSquare.centerPoint = SqCenterPoint(newSquare)
                                moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                                ingameX, ingameY, land = getIngamePos_and_landType()
                                

                                newSquare.ingamePos = [ingameX, ingameY]
                                #newSquare.landType = land

                                squareList.append(newSquare)
                                print("success")
                            #if not
                            # move the cursor in a position that would be correct
                            #for example if we are too much to the left side, check right side
                            #keep checking until we find desired ingame pos
                            elif potentialInY != squareList[i].ingamePos[1]-1:
                                expectedIngamePos = [squareList[1].ingamePos[0] + topRightCenterPointDistance[0],squareList[1].ingamePos[1] + topRightCenterPointDistance[1]]
                                print ("Incorrect ingamepos")
                                
                    if squarePos == squarePos.top_right:
                        #if centerpoint distance hasn't been created for this distance
                        #add square based on the default square

                        if topRightCenterPointDistance == [0,0]:
                            newSquare = Square()
                            positionNextSquare(newSquare, squareList[i], squarePos.top_right)
                            newSquare.centerPoint = SqCenterPoint(newSquare)


                            moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                            ingameX, ingameY, land = getIngamePos_and_landType()

                            newSquare.ingamePos = [ingameX, ingameY]
                            newSquare.landType = land
                            
                            squareList.append(newSquare)
                            
                            topRightCenterPointDistance[0] = squareList[i].centerPoint[0] - newSquare.centerPoint[0]
                            topRightCenterPointDistance[1] = squareList[i].centerPoint[1] - newSquare.centerPoint[1]

                            print("success")
                            
                        elif topRightCenterPointDistance != [0,0]:

                            #confirm with in game pos if its correct

                            potentialOutX = squareList[i].centerPoint[0] - topRightCenterPointDistance[0]
                            potentialOutY = squareList[i].centerPoint[1] - topRightCenterPointDistance[1]
                            moveClick(potentialOutX, potentialOutY)
                            potentialInX, potentialInY, land = getIngamePos_and_landType()

                            #if so 
                            # add it to the list
                            if potentialInY == squareList[i].ingamePos[1]-1:

                                newSquare = Square()
                                positionNextSquare(newSquare, squareList[i], squarePos.top_right)

                                #newSquare.centerPoint = [potentialOutX, potentialOutY]
                                newSquare.centerPoint = SqCenterPoint(newSquare)
                                moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                                ingameX, ingameY, land = getIngamePos_and_landType()
                                

                                newSquare.ingamePos = [ingameX, ingameY]
                                #newSquare.landType = land

                                squareList.append(newSquare)
                                print("success")
                            #if not
                            # move the cursor in a position that would be correct
                            #for example if we are too much to the left side, check right side
                            #keep checking until we find desired ingame pos
                            elif potentialInY != squareList[i].ingamePos[1]-1:
                                expectedIngamePos = [squareList[1].ingamePos[0] + topLeftCenterPointDistance[0],squareList[1].ingamePos[1] + topLeftCenterPointDistance[1]]
                                print ("Incorrect ingamepos")
                            
                    if squarePos == squarePos.bottom_left:
                        #if centerpoint distance hasn't been created for this distance
                        #add square based on the default square

                        if bottomLeftCenterPointDistance == [0,0]:
                            newSquare = Square()
                            positionNextSquare(newSquare, squareList[i], squarePos.bottom_left)
                            newSquare.centerPoint = SqCenterPoint(newSquare)



                            moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                            ingameX, ingameY, land = getIngamePos_and_landType()

                            newSquare.ingamePos = [ingameX, ingameY]
                            newSquare.landType = land
                            
                            squareList.append(newSquare)
                            
                            print("squareList[i].centerPoint[0]: ", squareList[i].centerPoint[0])
                            print("newSquare.centerPoint[0]: ", newSquare.centerPoint[0])
                            print("squareList[i].centerPoint[1]: ", squareList[i].centerPoint[1])
                            print("newSquare.centerPoint[1]: ", newSquare.centerPoint[1])

                            bottomLeftCenterPointDistance[0] = squareList[i].centerPoint[0] - newSquare.centerPoint[0]
                            bottomLeftCenterPointDistance[1] = newSquare.centerPoint[1] - squareList[i].centerPoint[1]

                            print("bottomLeftCenterPointDistance[0]: ", bottomLeftCenterPointDistance[0])
                            print("bottomLeftCenterPointDistance[1]: ", bottomLeftCenterPointDistance[1])
                            print("success")
                            
                        elif bottomLeftCenterPointDistance != [0,0]:

                            #confirm with in game pos if its correct

                            potentialOutX = squareList[i+1].centerPoint[0] - bottomLeftCenterPointDistance[0]
                            potentialOutY = squareList[i+1].centerPoint[1] + bottomLeftCenterPointDistance[1]
                            #moveClick(potentialOutX, potentialOutY)

                            moveClick(squareList[i+1].centerPoint[0], squareList[i].centerPoint[1])
                            potentialInX, potentialInY, land = getIngamePos_and_landType()

                            #if so 
                            # add it to the list
                            print("portentialInY: ", potentialInY)
                            print("squareList[i].ingamePos[1]+1: ", squareList[i].ingamePos[1]+1)

                            if potentialInY == squareList[i].ingamePos[1]+1:

                                newSquare = Square()
                                positionNextSquare(newSquare, squareList[i], squarePos.bottom_left)

                                #newSquare.centerPoint = [potentialOutX, potentialOutY]
                                newSquare.centerPoint = SqCenterPoint(newSquare)
                                moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                                ingameX, ingameY, land = getIngamePos_and_landType()
                                

                                newSquare.ingamePos = [ingameX, ingameY]
                                #newSquare.landType = land

                                squareList.append(newSquare)
                                print("success")
                            #if not
                            # move the cursor in a position that would be correct
                            #for example if we are too much to the left side, check right side
                            #keep checking until we find desired ingame pos
                            elif potentialInY != squareList[i].ingamePos[1]-1:
                                expectedIngamePos = [squareList[1].ingamePos[0] + bottomLeftCenterPointDistance[0],squareList[1].ingamePos[1] + bottomLeftCenterPointDistance[1]]
                                print ("Incorrect ingamepos")
                    if squarePos == squarePos.bottom_right:
                        #if centerpoint distance hasn't been created for this distance
                        #add square based on the default square

                        if bottomRightCenterPointDistance == [0,0]:
                            newSquare = Square()
                            positionNextSquare(newSquare, squareList[i], squarePos.bottom_right)
                            newSquare.centerPoint = SqCenterPoint(newSquare)


                            moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                            ingameX, ingameY, land = getIngamePos_and_landType()

                            newSquare.ingamePos = [ingameX, ingameY]
                            newSquare.landType = land
                            
                            squareList.append(newSquare)
                            
                            bottomRightCenterPointDistance[0] = squareList[i].centerPoint[0] - newSquare.centerPoint[0]
                            bottomRightCenterPointDistance[1] = squareList[i].centerPoint[1] - newSquare.centerPoint[1]

                            print("success")
                            
                        elif bottomRightCenterPointDistance != [0,0]:

                            #confirm with in game pos if its correct

                            potentialOutX = squareList[i].centerPoint[0] - bottomRightCenterPointDistance[0]
                            potentialOutY = squareList[i].centerPoint[1] - bottomRightCenterPointDistance[1]
                            moveClick(potentialOutX, potentialOutY)
                            potentialInX, potentialInY, land = getIngamePos_and_landType()

                            #if so 
                            # add it to the list
                            if potentialInY == squareList[i].ingamePos[1]+1:

                                newSquare = Square()
                                positionNextSquare(newSquare, squareList[i], squarePos.bottom_right)

                                #newSquare.centerPoint = [potentialOutX, potentialOutY]
                                newSquare.centerPoint = SqCenterPoint(newSquare)
                                moveClick(newSquare.centerPoint[0], newSquare.centerPoint[1])
                                ingameX, ingameY, land = getIngamePos_and_landType()
                                

                                newSquare.ingamePos = [ingameX, ingameY]
                                #newSquare.landType = land

                                squareList.append(newSquare)
                                print("success")
                            #if not
                            # move the cursor in a position that would be correct
                            #for example if we are too much to the left side, check right side
                            #keep checking until we find desired ingame pos
                            elif potentialInY != squareList[i].ingamePos[1]-1:
                                expectedIngamePos = [squareList[1].ingamePos[0] + bottomRightCenterPointDistance[0],squareList[1].ingamePos[1] + bottomRightCenterPointDistance[1]]
                                print ("Incorrect ingamepos")

                    

        

            #if centerpoint distance has been created for this distance
                #add square based on centerpoint distance
                #confirm with in game pos if its correct

        #q key
        if win32api.GetKeyState(0x51) < 0: 
            print('finished setting up farming positions')
            break  
        #break
             
def isMouseInNewSquarePos(x, y, oldSquare):
    testSquare = Square()
    #print ("testSquare right point", testSquare.rightPoint)
    #testSquare.realSquare = True
    #squareList.append(testSquare)
#top right
    squarePosition = None
    #print (x)
    #print (y)
    if x > oldSquare.topPoint[0] and y < oldSquare.rightPoint[1]:
        squarePosition = SquarePos.top_right
        positionNextSquare(testSquare, oldSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point):
            #print(shapelySquare.contains(point), squarePosition) 
           
            return shapelySquare.contains(point), squarePosition
#top left
    if x < oldSquare.topPoint[0] and y < oldSquare.rightPoint[1]:
        squarePosition = SquarePos.top_left
        
        positionNextSquare(testSquare, oldSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point):
            #print(shapelySquare.contains(point), squarePosition)
            
            return shapelySquare.contains(point), squarePosition
        
    #bottom right
    if x > oldSquare.topPoint[0] and y > oldSquare.rightPoint[1]:
        squarePosition = SquarePos.bottom_right
        positionNextSquare(testSquare, oldSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point):      
            #print(shapelySquare.contains(point), squarePosition) 
            
            return shapelySquare.contains(point), squarePosition
        
    #bottom left
    if x < oldSquare.topPoint[0] and y > oldSquare.rightPoint[1]:
        squarePosition = SquarePos.bottom_left
        positionNextSquare(testSquare, oldSquare, squarePosition)

        point = Point(x,y)
        shapelySquare = Polygon([testSquare.leftPoint, testSquare.topPoint, testSquare.rightPoint, testSquare.bottomPoint])
        if shapelySquare.contains(point): 
            #print(shapelySquare.contains(point), squarePosition)
            
            return shapelySquare.contains(point), squarePosition
    else:
        #print(False, squarePosition)
        
        return False, squarePosition

def createSquarePlanOld():
    canPlace = True
    side = None
    isNextTo = None
    i = 0
    while True:
        leftButtonState = win32api.GetKeyState(0x01)
        rightButtonState = win32api.GetKeyState(0x02)
        keyS_State = win32api.GetKeyState(0x53)
        keyQ_State = win32api.GetKeyState(0x51)
        mouseX, mouseY = pyautogui.position()
        #createSquarePlan(mouseX, mouseY)

        if keyS_State < 0 and canPlace == True:

            canPlace = False
            try:
                isNextTo, side = isNextSquareNextToLast(mouseX,mouseY)
            except:
                pass
            #print(isNextTo)

            
            if isNextTo == True:
                i += 1

                print("next to ", i)

                #print("adding square")
                #side = SqusarePos.top_left
                #print("side: ", side)
                addSqaure(side, baseSquare, True, (255,0,255))
                #spyautogui.moveTo(squareList[-1].bottomPoint[0], squareList[-1].bottomPoint[1], 2)
                #drawDiamonds(blank)
                #cv.waitKey(1)
            
            if isNextTo == False:
                print("would of called fakes")
                #addMultipleSqauresWithFakes(side, baseSquare,calculateHowManyFakeSqaures(side ,mouseX, mouseY),(255,0,255))
                #pyautogui.moveTo(squareList[-1].bottomPoint[0], squareList[-1].bottomPoint[1], 2)
                #pyautogui.moveTo(currentOuterBottom[0],currentOuterBottom[1])
                #print("side: ", side)
        if keyS_State > -1 and canPlace == False:
            cv.destroyAllWindows()
            drawDiamonds(blank)
            cv.waitKey(1)
            
        if keyS_State > -1:
            canPlace = True

        if keyQ_State < 0:  # if key 'q' is pressed 
            print('finished setting up!')
            #for i in range (len(squareList)):
            #    print ("i = ", i+1," this numbers centerPoint is ", squareList[i+1].centerPoint)
            #    pyautogui.moveTo(squareList[i+1].centerPoint[0], squareList[i+1].centerPoint[1], 1)
            break  # finishing the loop

    # when left click

    
    #if left click would be in a space that is next to the last place square

    #add square

    #if left click would be in a space that is not next to the last place sqaure
    #add square with fakes
def calculateHowManyFakeSqaures(posDir, x, y):
    howMany = 0
    #testSquare = Square
    point = Point(x,y)
    addSqaure(posDir, baseSquare, False, (120, 255, 72))
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
            addSqaure(posDir, baseSquare, False, (120, 255, 72))
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
def createDefaultSquareOld(square):

    while (True):
        #when the s key is pressed run the rest of code
        if win32api.GetKeyState(0x53) < 0:
            break
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
                    pyautogui.moveTo(currentRightSide[0],currentRightSide[1], 0.001)
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
            #pyautogui.moveTo(currentOuterBottom[0], currentOuterBottom[1], 0.001)
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


    #print("finalRight after", finalRightSide)
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
    #for i in range (len(squareList)):
    #    if squareList[i-1].realSquare == False:
    #        squareList.pop(i-1)

def addSqaure(posDir, baseSquare, settingWithMouse = False, realSquare = True, squareColour = baseSquare.colour,
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
    #print("append square")
    squareList.append(square)

    positionNextSquare2(square, posDir, settingWithMouse)

def positionNextSquare2(square, posDir, settingWithMouse = True):
    #get width and high of outer
    if settingWithMouse:
        howFast = 0
    else:
        howFast = 0.6

    leftDiff = squareList[0].innerLeft[0] - squareList[0].leftPoint[0]
    topDiff = squareList[0].innerTop[1] - squareList[0].topPoint[1]
    rightDiff = squareList[0].rightPoint[0] - squareList[0].innerRight[0]
    bottomDiff = squareList[0].bottomPoint[1] - squareList[0].innerBottom[1]
    
    square.topDiff = topDiff

    previousSquare = squareList[-2]
    #print ("index of prev: ", squareList.index(previousSquare))
    previousHeight = previousSquare.bottomPoint[1] - previousSquare.topPoint[1]
    previousWidth = previousSquare.rightPoint[0] - previousSquare.leftPoint[0]

    #print("prev height: ", previousHeight,"prev width: ", previousWidth)
    #get the next pos
    if posDir == SquarePos.top_left:
        square.leftPoint = [previousSquare.topPoint[0] - previousWidth, previousSquare.topPoint[1]]
        square.topPoint = [previousSquare.leftPoint[0], previousSquare.leftPoint[1] - previousHeight]
        square.rightPoint = [previousSquare.bottomPoint[0], previousSquare.bottomPoint[1]- previousHeight]
        square.bottomPoint = [previousSquare.rightPoint[0] - previousWidth, previousSquare.rightPoint[1]]
        
        #pyautogui.moveTo(previousSquare.leftPoint[0], previousSquare.topPoint[1])
        x = previousSquare.leftPoint[0]+1
        y = previousSquare.topPoint[1]
        positionToPurpleTop(square,x,y, previousHeight, previousWidth, topDiff, howFast)
        #print("move")

    if posDir == SquarePos.top_right:
        square.leftPoint = [previousSquare.bottomPoint[0], previousSquare.bottomPoint[1] - previousHeight]
        square.topPoint = [previousSquare.rightPoint[0], previousSquare.rightPoint[1] - previousHeight]
        square.rightPoint = [previousSquare.topPoint[0] + previousWidth, previousSquare.topPoint[1]]
        square.bottomPoint = [previousSquare.leftPoint[0] + previousWidth, previousSquare.leftPoint[1]]
        
        
        #pyautogui.moveTo(previousSquare.rightPoint[0]+1, previousSquare.topPoint[1], 1)
        x = previousSquare.rightPoint[0]+1
        y = previousSquare.topPoint[1]
        #print("move")
        positionToPurpleTop(square,x,y, previousHeight, previousWidth, topDiff, howFast)
    if posDir == SquarePos.bottom_left:
        square.leftPoint = [previousSquare.bottomPoint[0] - previousWidth, previousSquare.bottomPoint[1]]
        square.topPoint = [previousSquare.rightPoint[0] - previousWidth, previousSquare.rightPoint[1]]
        square.rightPoint = [previousSquare.topPoint[0], previousSquare.topPoint[1] + previousHeight]
        square.bottomPoint = [previousSquare.leftPoint[0], previousSquare.leftPoint[1] + previousHeight]

        #pyautogui.moveTo(previousSquare.leftPoint[0]+1, previousSquare.bottomPoint[1], 1)
        x = previousSquare.leftPoint[0]+1
        y = previousSquare.bottomPoint[1]
        positionToPurpleTop(square,x,y, previousHeight, previousWidth, topDiff, howFast)

    if posDir == SquarePos.bottom_right:
        square.leftPoint = [previousSquare.topPoint[0], previousSquare.topPoint[1] - previousHeight]
        square.topPoint = [previousSquare.leftPoint[0] + previousWidth, previousSquare.leftPoint[1]]
        square.rightPoint = [previousSquare.bottomPoint[0] + previousWidth, previousSquare.bottomPoint[1]]
        square.bottompoint = [previousSquare.rightPoint[0], previousSquare.rightPoint[1] + previousHeight]

        #pyautogui.moveTo(previousSquare.rightPoint[0], previousSquare.bottomPoint[1], 1)
        x = previousSquare.rightPoint[0]+1
        y = previousSquare.bottomPoint[1]
        positionToPurpleTop(square,x,y, previousHeight, previousWidth, topDiff, howFast)

    pass
def positionToPurpleTop(square, mouseX, mouseY, height, width, topDiff, howFast = 0.6):
    #print("in posiiton to purple")
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
                    #pyautogui.moveTo(mouseX,mouseY, 0.001)
                    #print(1)
                else: 
                    break
            for j in range(9999):
                if screenshot.getpixel((mouseX, mouseY-1)) != purpleRGB:
                    mouseY -= 1
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
  
        #pyautogui.moveTo((mouseX, mouseY))
    
    if rightCheck < leftCheck:
        for i in range(9999):
            for k in range(9999):
                if screenshot.getpixel((mouseX, mouseY-1)) == purpleRGB and screenshot.getpixel((mouseX-1, mouseY )) != purpleRGB:
                    mouseX -= 1
                    #pyautogui.moveTo(mouseX,mouseY, 0.001)
                    #print(1)
                else: 
                    break
            for j in range(9999):
                try:
                    if screenshot.getpixel((mouseX, mouseY-1)) != purpleRGB:
                        mouseY -= 1
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
  
        #pyautogui.moveTo((mouseX, mouseY))


    if screenshot.getpixel((mouseX, mouseY-1)) != purpleRGB:
        mouseY -=1
    #pyautogui.moveTo(mouseX, mouseY, 0.001)

    square.height = height
    square.width = width
    halfHeight = height/2
    halfWidth = width/2

    topBoarder = mouseY - topDiff[1]
    square.topPoint = [mouseX, topBoarder]
    pyautogui.moveTo(mouseX, topBoarder + halfHeight)

    square.leftPoint = [mouseX - halfWidth, topBoarder+halfHeight]
    square.rightPoint = [mouseX + halfWidth, topBoarder+halfHeight]
    square.bottomPoint = [mouseX, topBoarder+height]
    print("setting centerpoint to ", [mouseX, topBoarder + halfHeight])
    square.centerPoint = [mouseX, topBoarder + halfHeight]

    print("centerPoint is now ", square.centerPoint)
    
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
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
def runListeners():
    #collect keyboard inputs until released

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        #stop listener
        return False

while (True):
    try:
        runListeners()
    except:
        break
    


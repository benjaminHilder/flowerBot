import cv2
from pytesseract import pytesseract
import pyautogui
import datetime
import sys
import time
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import easyocr
from IPython.display import Image
from time import sleep

pytesseract.tesseract_cmd = "E:\\Program Files\\Tesseract-OCR\\tesseract.exe"

x_start_point = 1365
y_start_point = 120

x_howFar = 555
y_howFar = 900

xPos = 0
yPos = 0
landType = ""


def getIngamePos_and_landType():

    print("Taking a screenshot...")
    screenshot = pyautogui.screenshot(region=(x_start_point, y_start_point, x_howFar, y_howFar))

    #converting pyautogui screenshot into one that cv2 can read
    open_cv_image = np.array(screenshot) 
     #Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    grayscale = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    adaptive = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 11)

    #words_in_image = pytesseract.image_to_string(open_cv_image)

    cv2.imshow("show", open_cv_image)
    cv2.waitKey(0)
    #word_list = words_in_image.split()
#
    #for i in range (len(word_list)):
    #    if word_list[i] == "Tile":
    #        xPos = word_list[i+1]
    #        xPos.replace('(', '')
    #        xPos.replace(' ', '')
#
    #        yPos = word_list[i+2]
    #        yPos.replace(' ', '')
    #        yPos.replace(')', '')
#
    #        landType = word_list[i+4]
#
            

    #return xPos, yPos, landType
   # print(xPos, yPos, landType)

getIngamePos_and_landType()


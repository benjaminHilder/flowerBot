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
from pytesseract import Output

pytesseract.tesseract_cmd = "E:\\Program Files\\Tesseract-OCR\\tesseract.exe"

x_start_point = 1564
y_start_point = 146

x_howFar = 39
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

    #grayscale = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    #adaptive = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 11)

    #cv2.imshow("show", open_cv_image)
    #cv2.waitKey(0)

    words_in_image = pytesseract.image_to_string(open_cv_image)
    word_list = words_in_image.split()
    for i in range(len(word_list)):
        if word_list[i] == "‘Tile":
            newString = word_list[i].replace('‘', '')
            word_list[i] = newString

    #data=pytesseract.image_to_boxes(open_cv_image)
    #tVar = None
#
    #tVarX = None
    #tVarY = None
    #for i in range(len(data)):
    #    if data[i] == "T":
#
    #        tVar = data[i]
    #        tVarX = data[i+1]
    #        tVarY = data[i+2]
#
    #print("tVar: ", tVar)
    #print("tVarX", tVarX)
    #print("tVarY", tVarY)   

    d = pytesseract.image_to_data(open_cv_image, output_type=Output.DICT)
    n_boxes = len(d['level'])
    print(n_boxes)
    
    (x, y, w, h) = (d['left'][-1], d['top'][-1], d['width'][-1], d['height'][-1])
    cv2.rectangle(open_cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print (x, y, w, h)


    newScreenshot = pyautogui.screenshot(region=(x_start_point, y_start_point + y, 170, h))
    open_cv_image2 = np.array(newScreenshot) 
     #Convert RGB to BGR 
    open_cv_image2 = open_cv_image2[:, :, ::-1].copy()
    cv2.imshow("new", open_cv_image2)
    cv2.waitKey(0)
            
    #print("tar var: ", tVar)
    #print(data)
    #print ("words in image")
    #print(word_list)
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


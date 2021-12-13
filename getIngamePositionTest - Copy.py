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
x_start_point = 1560
y_start_point = 110
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
#cv2.imshow("new", open_cv_image2)
#cv2.waitKey(0)
words_in_image = pytesseract.image_to_string(open_cv_image2)
word_list = words_in_image.split()
#print("word_list ", word_list)
#if word_list[0] != 'Tile':
#    word_list.pop(0)

for i in range(len(word_list)):
    if word_list[i] == 'Tile':
        xString = word_list[i + 1]
        yString = word_list[i + 2]
        landString = word_list[i + 4]

#print(xString)
#print(yString)
#print(landString)

xClean1 = xString.replace('(', '')
xClean2 = xClean1.replace(',', '')
yClean1 = yString.replace(')', '')
xInt = int(xClean2)
yInt = int(yClean1)

#xClean1 = xString.replace('(', '')
#xClean2 = xClean1.replace(',', '')
#
#yClean1 = yString.replace(')', '')
#
#xInt = int(xClean2)
#yInt = int(yClean1)

#print(xInt)
#print(yInt)
#print(landString)
cv2.imshow("new", open_cv_image2)
cv2.waitKey(0)
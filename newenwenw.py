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


x_start_point = 1450
y_start_point = 120

x_howFar = 470
y_howFar = 900

screenshot = pyautogui.screenshot(region=(x_start_point, y_start_point, x_howFar, y_howFar))

open_cv_image = np.array(screenshot) 
open_cv_image = open_cv_image[:, :, ::-1].copy()
cv2.imshow("show", open_cv_image)
cv2.waitKey(0)
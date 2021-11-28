import cv2 as cv
import pytesseract

def getTextFromImg(image, blurStrength = 1):
    #image = get_grayscale(image)
    #image = thresholding(image)
    #image = remove_noise(image, blurStrength)

    return ocr_core(image)

def getImgPreproccessing(image, blurStrength):
    image = get_grayscale(image)
    #image = thresholding(image)
    #image = remove_noise(image, blurStrength)
    #image = get_canny(image)

    return image
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def get_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)
def remove_noise(image, blurStrng):
    return cv.blur(image, (blurStrng,blurStrng))
def thresholding(image):
    return cv.threshold(image, 0, 25, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

def get_canny(image):
    return cv.Canny(image, 174, 175)

def returnWhite(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    mask = cv.inRange(image,(255,255,255),(238, 238, 238))
    mask_rgb = cv.cvtColor(mask,cv.COLOR_GRAY2BGR)
    return mask_rgb

    



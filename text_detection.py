import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = os.path.join('C:\\', 'Program Files', 'Tesseract-OCR', 'tesseract.exe')

img = cv2.imread('D:\\Projects\\traitement-images\\3.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray, 3)

config = ('-l eng --oem 1 --psm 11')
text = pytesseract.image_to_string(gray, config=config)

print(text)

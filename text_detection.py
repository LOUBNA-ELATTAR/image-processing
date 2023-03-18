import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = os.path.join('C:\\', 'Program Files', 'Tesseract-OCR', 'tesseract.exe')


# Load an image
img = cv2.imread('D:\\Projects\\traitement-images\\3.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply image preprocessing techniques to enhance the text
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray, 3)

# Detect text regions in the image using Tesseract OCR
config = ('-l eng --oem 1 --psm 11')
text = pytesseract.image_to_string(gray, config=config)

# Print the detected text
print(text)

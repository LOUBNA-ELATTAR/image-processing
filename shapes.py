import cv2
import numpy as np

width = 500
height = 500

img = np.zeros((height, width, 3), np.uint8)

cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), 2)    # blue rectangle with thickness 2
cv2.rectangle(img, (200, 200), (300, 300), (0, 255, 0), -1) # green rectangle filled with color

pts = np.array([[350, 350], [450, 350], [400, 450]])
cv2.drawContours(img, [pts], 0, (0, 0, 255), 2)             # red triangle with thickness 2
pts = np.array([[250, 150], [300, 250], [200, 250]])
cv2.fillPoly(img, [pts], (255, 255, 0))                      # yellow triangle filled with color

cv2.circle(img, (75, 400), 25, (255, 0, 255), -1)            # pink circle filled with color
pts = np.array([[100, 100], [150, 100], [125, 50]])
cv2.polylines(img, [pts], True, (255, 255, 255), 3)          # white closed polyline with thickness 3

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

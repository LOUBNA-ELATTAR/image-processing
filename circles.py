import cv2
import numpy as np

width = 500
height = 500

img = np.zeros((height, width, 3), np.uint8)

for i in range(50):
    center = (np.random.randint(0, width), np.random.randint(0, height))
    radius = np.random.randint(10, 100)
    color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))

    cv2.circle(img, center, radius, color, -1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

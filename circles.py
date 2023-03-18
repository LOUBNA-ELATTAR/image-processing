import cv2
import numpy as np

# Set the dimensions of the image
width = 500
height = 500

# Create a blank image
img = np.zeros((height, width, 3), np.uint8)

# Draw circles on the image
for i in range(50):
    # Randomly generate the center and radius of the circle
    center = (np.random.randint(0, width), np.random.randint(0, height))
    radius = np.random.randint(10, 100)

    # Randomly generate the color of the circle
    color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))

    # Draw the circle on the image
    cv2.circle(img, center, radius, color, -1)

# Show the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

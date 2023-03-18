import cv2
import numpy as np

img = cv2.imread('D:\\Projects\\traitement-images\\1.jpg')
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Original Image', img)
# cv2.imshow('Grayscale Image', gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Get the image resolution
height, width, channels = img.shape
print('Resolution: {} x {} ({} channels)'.format(width, height, channels))

# Reshape the image to a 2D array of pixels
pixels = img.reshape((-1, 3))

# Convert pixel values from 0-255 range to 0-1 range
pixels = np.float32(pixels) / 255.0

# Define the number of clusters (colors)
num_clusters = 8

# Define the termination criteria for the K-means algorithm
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Perform K-means clustering to quantize the colors of the image
_, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert the color centers back to 0-255 range and round the values to integers
centers = np.uint8(centers * 255)

# Replace each pixel value with its corresponding color center
quantized = centers[labels.flatten()]

# Reshape the quantized image back to its original shape
quantized = quantized.reshape(img.shape)

# Display the original and quantized images
cv2.imshow('Original Image', img)
cv2.imshow('Quantized Image ({} colors)'.format(num_clusters), quantized)
cv2.waitKey(0)
cv2.destroyAllWindows()

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


height, width, channels = img.shape
print('Resolution: {} x {} ({} channels)'.format(width, height, channels))

pixels = img.reshape((-1, 3))

pixels = np.float32(pixels) / 255.0

num_clusters = 8

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

_, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers * 255)

quantized = centers[labels.flatten()]

quantized = quantized.reshape(img.shape)

cv2.imshow('Original', img)
cv2.imshow('Quantized ({} colors)'.format(num_clusters), quantized)
cv2.waitKey(0)
cv2.destroyAllWindows()

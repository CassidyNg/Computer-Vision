import cv2 as cv
import numpy as np
# think of gradients as edge-like regions that are present in an image, BUT gradients and edges are NOT the same thing (from a mathematical pov)
# canny edge detector - an advanced edge detection algorithm (multi-step process)

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)\

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
# computes the gradients of the grayscale image -- edges in the image are essentially drawn over with a pencil and then lightly smudged
lap = cv.Laplacian(gray, cv.CV_64F) #ddepth = data depth -- when you transition from black to white (and vice versa), that is considered a positive and a negative slope
lap = np.uint8(np.absolute(lap)) # images can not have negative pixels values --> convert all pixel values to the  absolute values --> convert to a uint8 (image specific data type)
cv.imshow('Laplacian', lap)

# Sobel
# computes the gradients in two directions (x and y)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # gradients computed along the x-axis
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
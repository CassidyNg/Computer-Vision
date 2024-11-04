import cv2 as cv
import matplotlib.pyplot as plt
# allow you to visualize the distribution of pixel intensities in an image

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256]) # histSize is the number of bins we want to use for computing the histogram

plt.figure()
plt.title('Gray')

cv.waitKey(0)
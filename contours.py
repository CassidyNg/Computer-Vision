import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # thresholding essentially looks at an image amnd tries to binarize it
# -- if the density of a pixel is below 125, it's going to be set to zero or blank -- if the density is above 125, it is set to white or two
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # mode can be RETR_Tree for all the hierarchal contours, or RETR_EXTERNAL for only external contours, or RETR_LIST for all the contours in the image
# findContours method looks at a structuring element or the edges found in the image and returns the contours (a Python list of all the coordinates of the contours found in the image) and hierarchies (hierarchical representation of countours)
# RETR_LIST returns all the contours found in the image -- RETR_EXTERNAL returns only the external contouurs - all the ones on the outside -- RETR_TREE returns all the hierarchal contours - all the ones that are in a hierachical system
# approximation method - how we want to approximate the contour -- CHAIN_APPROX_NONE does nothing - returns all the contours -- CHAIN_APPROX_SIMPLE compresses all the contours that are returned
print(f'{len(contours)} contour(s) found!') # find the number of contours found

cv.drawContours(blank, contours, -1, (0,0,255), 1) # contourIdx - how many contours you want in the image -- -1 for all contours
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
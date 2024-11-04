import cv2 as cv

# Overview of blurring terms
# kernel - the size of the window that you draw over a specific portion of an image (number of rows and columns)

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging - define a kernel window over a specific portion of an image - computing the average of all of the running pixel intensity
# -- higher kernel size = more blurred
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur - each running pixel is given a weight - the average of them gives you the true center
# -- less blurring but more natural than averaging
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur - finds median of the surrounding pixels
# -- tends to be more effective at reducing noise in an image as compared to averaging -- not meant for high kernel sizes (ex. 7 or 5 in some cases)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
# -- most effective - applies blurring but retains the edges in the image
bilateral = cv.bilateralFilter(img, 10, 35, 25) # sigmaColor - larger values mean more colors in the neighborhood will be considered when the blur is computed
# -- sigmaSpace - larger values mean that pixels further out from the central pixel will influence the blurring calculation
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
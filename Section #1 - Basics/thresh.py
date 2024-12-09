import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # lower thresh = more white (many pixels have an intensity greater than the thresh value) -- higher thresh = less white (not that many pixel intensities are greater than the thresh value)
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # lower thresh = more white (many pixels have an intensity greater than the thresh value) -- higher thresh = less white (not that many pixel intensities are greater than the thresh value)
cv.imshow('Simple Threshold Inverse', thresh_inverse)

# instead of manually specifying the thresholds (simple), the computer can find the optimal threshold value by itself (adaptive)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3) # adaptiveMethod tells the machine which method to use when computing the optimal threshold value - currently set to the mean of some neighborhood of pixels
# blockSize is essentially the neighbrorhood size of the kernel size - used to compute mean to find the optimal threshold -- C value is an integer that is subtracted from the mean, allowing us to fine tune our threshold
cv.imshow('Adaptive Threshold Mean', adaptive_thresh) # basically defined a kernel size or window that is drawn on the image (11 x 11) and openCV computes a mean over those neighborhood pixels and finds the optimal threshold value for that specific part
# the more you subtract from the mean, the more accurate it is 

adaptive_thresh_2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3) # only difference between mean and Gaussian is that Gaussian applied a weight to each pixel value and computed the mean across those pixels
cv.imshow('Adaptive Threshold Gaussian', adaptive_thresh_2)

cv.waitKey(0)
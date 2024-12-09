import cv2 as cv

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) # kernal size/ksize is a 2x2 tuple representing the video size openCV uses to compute the blown image
# -- kernel size has to be an odd number -- large kernel size = more blurred
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny) # can reduce edges by passing in a blurred image

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3) # attempt to get back edge cascade
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) # 500,500 is the destination size -- takes in image resizes image to 500 x 500, ignoring aspect ratio
# interpolation occurs by default in background -- image to smaller dimensions (shrinking) = INTER_AREA -- larger dimensions (enlarging) = AREA_LINEAR or AREA_CUBIC
# AREA_CUBIC is the slowest of them all, but the resulting image is of a much higher quality than INTER_AREA or INTER_LINEAR
cv.imshow('Resized', resized)

# Cropping
# images are arrays, so we can select a portion of the image on the basis of its pixel values - using Array Slicing
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
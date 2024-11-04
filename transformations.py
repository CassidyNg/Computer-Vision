import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) # translation matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left | -y --> Up | x --> Right | y --> Down

translated = translate(img, -100, 100) # shift the image left by 100 pixdels and down by 100 pixels
cv.imshow('Translated', translated)

# Rotation -- specify a point to rotate the image around
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] # grab the height and width of the image by setting it equal to img.shape of the first two values
    
    if rotPoint is None: # if there's no specified rotation point, assume you rotate around the center
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # rotation matrix
    dimensions =(width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) # positive angle = counterclockwise, negative angle  = clockwise
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45) # rotate an already rotated image
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC) # shrinking = INTER_AREA; enlarging = INTER_LINEAR or INTER_CUBIC -- INTER_CUBIC is slower but has a better resulting image
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1) # flipCode could be 0, 1 or -1 -- 0 implies flipping the image vertcally (over x-axis) -- 1 specifies flipping the image horizontally (over y-axis) -- -1 implies both fliping the image vertically AND horizontally
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400] # Array Slicing
cv.imshow('Cropped', cropped)

cv.waitKey(0)
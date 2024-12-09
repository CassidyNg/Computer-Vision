import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # uint8 is the data type of an image
# -- 500, 500, 3 gives shape of height, width, and the number of color channels
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0 # [:] references all the pixels -- 0, 255, 0 paints the entire image green
blank[200:300, 300:400] = 0, 0, 255 # [first range, second range] -- first for height, second for width
cv.imshow('Green', blank)

# 2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness = cv.FILLED) # takes in an image to draw the rectangle over
# -- cv.FILLED AND setting thickness = -1 fills in the rectangle instead of just giving it a border
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), cv.FILLED)
cv.imshow('Rectangle', blank) 

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness = -1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness = 3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Cassidy!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
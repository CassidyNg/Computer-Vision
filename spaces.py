import cv2 as cv
# import matplotlib.pyplot as plt # DOESNT WORK? COME BACK TO LATER??
# color spaces are spaces of colors, a system representing an array of pixel colors -- RGB is a kind of space -- Grayscale is a color space

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
# BGR - opencv default way of reading images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
# HSV (hue saturation value) - based on how humans think and conceive colors
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)
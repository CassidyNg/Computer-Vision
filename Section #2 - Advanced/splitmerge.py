# Overview - learning to split and merge color channels
    # Color images consist of multiple channels: red, green, and blue (RGB) -- all images (BGR/RGB images) are basically those three color channels merged together
    # Split an image into its respective color channels = Splitting an image into its blue, green, and red components

import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img) # split image into blue, green, and red

# blank images consists of height and width but not the number of color channels in the image -- displaying one color channel by setting other components to black
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', b)
cv.imshow('Green', g) 
cv.imshow('Red', r)
# displayed as grayscale images that show the distribution of pixel intensities
# lighter regions = higher concentration of pixels values -- darker regions = little to no pixels in that region

cv.imshow('Blue', blue)
cv.imshow('Green', green) 
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
import cv2 as cv

# Reading Images --

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)


# Reading Videos --
capture = cv.VideoCapture('Videos/dog.mp4') 
# takes integer arguments or a path to a video file
# integer arguments if using a webcam or a camera that is connected to computer
# -- 0 usually references webcam -- 1 references first camera connected -- 2 references second camera connected

# to read videos, use a while loop and read the video frame by frame
while True:
    isTrue, frame = capture.read() # reads in the video frame by frame
    # -- returns the frame and a boolean saying whether the frame was succesfully read in or not
    
    cv.imshow('Video', frame) # displays an individual frame
    
    # to stop the video from playing indefinitely
    if cv.waitKey(20) & 0xFF==ord('d'): # if the letter 'd' is pressed, break out of loop and stop displaying video
        # if no key is pressed within 20 seconds, continue to play the video until the time is up
        break
    
capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)
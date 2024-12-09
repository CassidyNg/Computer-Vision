import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Images, Videos, and Live video
def rescaleFrame(frame, scale = 0.75): # default scale is 0.75
    width = int(frame.shape[1] * scale) # frame.shape[1] is the width of the frame/image   
    height = int(frame.shape[0] * scale) # frame.shape[0] is the height of the frame/image
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) # resizes the frame to a particular dimension

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

# Live video -- video from external camera or webcam; going on currently
def changeRes(width, height): # change resolution of image
    capture.set(3, width) # 3 references width
    capture.set(4, height) # 4 references height

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale = 0.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
        
# cv.waitKey(0)
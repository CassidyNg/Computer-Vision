import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Group of 5 People', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml') # reads those 33,000 lines of XML code and store in the variable
# note - sensitive to noise in an image

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1) # minNeighbors is a parameter that specified the number of neighbors a rectangle should have to be called a face
# detectMultiScale is an instance of the CascadeClassifier class - it will take this image and use the variables scaleFactor and minNeighbor to detect a face and return the rectangular coordinates of the face as a list
# minimmize sensitivity to noise by increasing the scale factor in minNeighbors

print(f'Number of faces found = {len(faces_rect)}')

# loop over the list and grab the coordinates of those images and draw a rectangle over the detected faces
for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)
    
cv.imshow('Detected Faces', img)

cv.waitKey(0)
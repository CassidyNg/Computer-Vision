import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'ELton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'C:\Users\ctng8\OneDrive\Documents\Computer Vision\Faces\train' # base folder containing five folders of people

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = [] # image arrays of faces
labels = []
def create_train(): # loop over every folder in the base folder, looping over every image and essentially grabbing the face in that image to add to the training set
    # training set consists of two lives - features
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
            
            for (x,y,w,h) in faces_rect: # grab the base regions of interest and set this equal to and crop out the face in the image
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done -----------------')

features = np.array(features, dtype = 'object')
labels = np.array(labels)

# instantiate face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recpgnizer on the features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

# p  = []
# for i in os.listdir(r'C:\Users\ctng8\OneDrive\Documents\Computer Vision\Faces\train'):
#     p.append(i)
    
# print(p)
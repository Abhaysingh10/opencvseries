import os
import cv2 as cv
import numpy as np

people = ['Henry Cavil', 'Jennifer Lawrence', 'RDJ', 'Tom Holland', 'Zendaya']
DIR = r'D:\Opencvseries\opencvseries\Faces'

# p =[]

# for i in os.listdir(r'D:\Opencvseries\opencvseries\Faces'):
#     p.append(i)

# print(p)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+h]
                features.append(faces_roi)
                labels.append(label)
            

create_train()
print('Training done ------------')



print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')


features = np.array(features, dtype='object')
labels = np.array(labels)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Training the model on the basis of features and list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yaml')

np.save('features.npy', features)
np.save('labels.npy', labels)





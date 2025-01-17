import cv2 as cv
from cv2 import Sobel
import numpy as np

img = cv.imread('Images/group.jpg')
# cv.imshow('Main', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

print(f'No of faces found = {len(face_rect)}')

for(x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detectedfaces', img)



cv.waitKey(0)
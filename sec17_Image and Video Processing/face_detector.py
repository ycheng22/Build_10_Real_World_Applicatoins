# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:16:15 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

@Github: https://github.com/ycheng22

Reference:
"""
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('news.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 
                                      scaleFactor=1.05, 
                                      minNeighbors=5)

for x, y, w, h in faces:
    #(x,y) is left upper corner, (x+w,y+h) right bottom coner, 
    #(0,255,0) line color, 3 line width
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


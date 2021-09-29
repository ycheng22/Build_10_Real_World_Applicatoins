# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:11:10 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

@Github: https://github.com/ycheng22

Reference:
"""
import cv2, time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


video = cv2.VideoCapture(0) 
#specify a number means use which camera,
#or specify the file name, eg:'movie.mp4
a = 1
while True:
    a += 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 
                                      scaleFactor=1.05, 
                                      minNeighbors=5)
    for x, y, w, h in faces:
        img = cv2.rectangle(gray, (x,y), (x+w,y+h), (0,255,0), 3)
    
    print(check)
    print(frame)
    
    #time.sleep(3)
    cv2.imshow('Capturing', img)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
print(a)   
video.release()
cv2.destroyAllWindows()
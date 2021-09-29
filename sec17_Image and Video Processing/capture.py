# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:40:08 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

@Github: https://github.com/ycheng22

Reference:
"""
import cv2, time

video = cv2.VideoCapture(0) 
#specify a number means use which camera,
#or specify the file name, eg:'movie.mp4
a = 1
while True:
    a += 1
    check, frame = video.read()
    
    print(check)
    print(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow('Capturing', gray)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
print(a)   
video.release()
cv2.destroyAllWindows()


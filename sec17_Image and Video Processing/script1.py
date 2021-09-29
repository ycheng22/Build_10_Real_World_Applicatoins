# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:19:14 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

@Github: https://github.com/ycheng22

Reference:
"""
import cv2

img = cv2.imread('./sample_images/galaxy.jpg', 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow('Galaxy', resized_img)
cv2.imwrite('Galaxy_resized.jpg', resized_img)
cv2.waitKey(0) #windows will last 2000 miliseconds before closing
cv2.destroyAllWindows() #specify the close action


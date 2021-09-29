# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:56:48 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
def weather_condition(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"
    
user_input = int(input("Enter Temperature:"))

print(weather_condition(user_input))
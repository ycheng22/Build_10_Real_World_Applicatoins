# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:24:33 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

@Github: https://github.com/ycheng22

Reference:
"""
#making a basic Bokeh line graph
from boken.io import output_file, show
from bokeh.plotting import figure


x = [1,2,3,4,5]
y = [6,7,8,9,10]

output_file("Line.html")

f = figure()

f.line(x, y)

show(f)
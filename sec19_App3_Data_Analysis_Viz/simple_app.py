# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:08:44 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
#run in anaconda cmd, python app1.py, stop and restart the server when update

import justpy as jp
import pandas as pd

def app():
    wp = jp.QuasarPage()
    #change classes: Quasar, https://quasar.dev/style/spacing
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h1 text-center q-pl-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    return wp

jp.justpy(app)
    
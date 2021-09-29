# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:51:43 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
#run in cmd: python .\script1.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #http://localhost:5000/
def home():
    return render_template("home.html") #must put home.html under folder "template"

@app.route('/about/') #http://localhost:5000/about
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
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

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    from datetime import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN
    
    start = datetime(2020,5,10)
    end = datetime(2020,6,10)
    df = data.DataReader(name='GOOG', data_source="yahoo", start=start, end=end)
    def inc_dec(c, o):
        if c > o:
            value ="Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value
    df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open+df.Close)/2
    df["Height"] = abs(df.Open-df.Close)    
    
    p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
    p.title.text = "Candlestick Chart"
    p.title.align = "center"
    p.title.text_font_size = "25px"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000 #hour, mininute, second, millisecond, total 12 hours
    df_inc = df[df.Status == "Increase"]
    df_dec = df[df.Status == "Decrease"]
    df_equ = df[df.Status == "Equal"]
    p.segment(df.index, df.High, df.index, df.Low, color="black")
    #increase days
    p.rect(df_inc.index, df_inc.Middle, hours_12, 
            df_inc.Height, fill_color="#00ff40", line_color="black")
    #decrease days
    p.rect(df_dec.index, df_dec.Middle, hours_12, 
            df_dec.Height, fill_color="#FF3333", line_color="black")

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0] #only need first one now
    #cdn_css = CDN.css_files #it's empty, 
    return render_template("plot.html", script1=script1,
            div1=div1, cdn_js=cdn_js)

@app.route('/') #http://localhost:5000/
def home():
    return render_template("home.html") #must put home.html under folder "template"

@app.route('/about/') #http://localhost:5000/about
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:32:27 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

@Github: https://github.com/ycheng22

Reference:
"""
from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

import pandas as pd
df = pd.read_csv('Times.csv')

p = figure(x_axis_type ='datetime', plot_width=500, plot_height=400, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

p.quad(left='Start', right='End', bottom=0, top=1, color='Green', source=cds)

output_file("Graph.html")
show(p)
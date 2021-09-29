# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:48:56 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

@Github: https://github.com/ycheng22

Reference:
"""
#from motion_detector import df
#from bokeh.plotting import figure, show, output_file
from bokeh.io import output_file, show
from bokeh.plotting import figure

import pandas as pd
df = pd.read_csv('Times.csv')

p = figure(x_axis_type ='datetime', plot_width=500, plot_height=400)
#p.yaxis.minor_tick_line_color = None
#p.ygrid[0].ticker.desired_num_ticks = 1
p.quad(left=df['Start'], right=df['End'], bottom=0, top=1, color='Green')

output_file("Graph.html")
show(p)


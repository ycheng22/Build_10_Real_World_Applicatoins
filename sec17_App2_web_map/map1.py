# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:11:43 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

mp = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
#for lt, ln, el in zip(lat, lon, elev):
#   fg.add_child(folium.Marker(location=[lt, ln], popup=el, tooltip="click me", 
#                              icon=folium.Icon(color=color_producer(el))))
#use circle marker
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" m", 
                fill_color=color_producer(el), color="grey", fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
#add world layer
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {"fillColor":"yellow" if x["properties"]["POP2005"] < 10000000
    else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red" })) 

mp.add_child(fgv)
mp.add_child(fgp)
mp.add_child(folium.LayerControl()) #add layer control panel

mp.save("Map1.html")

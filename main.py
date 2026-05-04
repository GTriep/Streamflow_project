#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:45:48 2026

@author: triep
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from src.analysis import load_streamflow
from src.analysis import basin_stats

df = load_streamflow("/Users/triep/Downloads/UU AW/Jaar 3/Modelleren van Aardsystemen/intro exercises/streamflow_project/data/AnnualStreamflow.csv")



basin_info ={
    "Upper_Colorado_Basin" : {
        "name" : "Upper Colorado River",
        "units" : "MAF/yr"},
    "Gunnison_Basin" : {
        "name" : "Gunnison River",
        "units" : "MAF/yr"},
    "Yampa_Basin" : {
        "name" : "Yampa River",
        "units" : "MAF/yr"},
    "White_Basin" : {
        "name" : "White River",
        "units" : "MAF/yr"},
    "South_West_Basin" : {
        "name" : "South West River",
        "units" : "MAF/yr"},
}


for basin in basin_info:
    stats = basin_stats(df, basin)
    basin_info[basin].update(stats)
    
print (basin_info)



                        




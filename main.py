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
from src.analysis import classify_year
from src.analysis import anomaly_timeseries
from src.analysis import reservoir_simulation

from src.visualise import plot_timeseries
from src.visualise import plot_all_basins
from src.visualise import plot_reservoir

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


col = "Gunnison_Basin"
mean = basin_info[col]["mean"]
std = basin_info[col]["std"]
years = df["Year"].values
flows = df[col].values
labels = [classify_year(f,mean,std) for f in flows]
for yr, lab in zip (years, labels):
    print (f"{yr}:{lab}")  


plot_all_basins(df, basin_info)     

result = reservoir_simulation(df["Gunnison_Basin"].to_numpy(), 5*10**6, 2.5*10**6 , 2*10**6)
storage = result["storage"]
years = df["Year"].values

fig, ax = plt.subplots()
plot_reservoir(ax, years, storage, capacity=5*10**6)
          




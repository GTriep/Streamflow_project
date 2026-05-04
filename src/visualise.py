#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:04:51 2026

@author: triep
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from src.analysis import anomaly_timeseries


def plot_timeseries(ax, years, flow, anomaly, basin_name):
    colors = ["blue" if val >= 0 else "red" for val in anomaly]
    ax.plot(years, flow, color = "black", label = "Annual flow")
    ax.bar(years, anomaly,color = colors, label = "Anomaly", alpha = 0.5)
    
    ax.set_xlabel("Years")
    ax.set_ylabel("MAF/yr")
    ax.set_title(f"{basin_name} - Streamflow and Anomalies")
    ax.legend()


def plot_all_basins(df, basin_info):
    n_basins = len(basin_info)
    fig, axes = plt.subplots (nrows = n_basins, ncols= 1, figsize = (10, 3*n_basins), sharex=True)
    
    if n_basins == 1:
        axes = [axes]
    
    years = df["Year"].values
    for i, basin_key in enumerate(basin_info):
        ax = axes[i]
        flow = df[basin_key]
        anomaly = anomaly_timeseries(df, basin_key)
        basin_name = basin_info[basin_key]["name"]
    
        plot_timeseries(ax, years, flow, anomaly, basin_name)
    
    plt.tight_layout()
    plt.savefig("streamflow_timeseries.png", dpi=150)
    plt.show()
    

def plot_reservoir(ax, years, storage, capacity):
    """ Plot reservoir storage over time."""
  
    ax.fill_between(years, storage, color="steelblue", alpha=0.6, label="Storage")

    ax.axhline(capacity, linestyle="--", color="black", label="Capacity")

    ax.fill_between(years, 0, storage,
                    where=(storage == 0),
                    color="red",
                    alpha=0.3,
                    label="Deficit years")

    # --- labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Storage (MAF)")
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("reservoir_simulation.png", dpi=150)
    plt.show()


    

    

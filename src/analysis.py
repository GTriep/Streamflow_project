#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:07:04 2026

@author: triep
"""

import pandas as pd
import numpy as np

def load_streamflow(filepath):
    """reads your CSV file and gives you a statistical summary of your file, so you can analyse your dataset
    filepath : the file you want to import"""
    df = pd.read_csv(filepath)
    print(df.describe())
    return df


def basin_stats(df, column):
    """gives you the mean, std, min and max of a specific column from the dataset you want to inspect"""
    data = df[column].to_numpy()
    
    return {
        "mean": float(np.mean(data)),
        "std": float(np.std(data)),
        "min": float(np.min(data)),
        "max": float(np.max(data))
    }

 
def classify_year(flow, mean, std):
    """ classifies the annual flow relative to the long term mean and std as wet, dry or normal
    flow = a single annual flow value
    mean = the long term mean of the flow of a specific basin
    std = the long term std of the flow of a specific basin
    """
    if flow >= (mean-std):
        return "dry"
    elif flow <= (mean+std):
        return "wet"
    else:
        return "normal"

def anomaly_timeseries(df, column):
    values = df[column].to_numpy()
    mean = float(np.mean(values))
    anomalies = values - mean
    return anomalies

    

df = load_streamflow("/Users/triep/Downloads/UU AW/Jaar 3/Modelleren van Aardsystemen/intro exercises/streamflow_project/data/AnnualStreamflow.csv")
 
stats = basin_stats(df, "Upper_Colorado_Basin")
print(stats)
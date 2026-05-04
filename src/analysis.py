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


def reservoir_simulation(inflows, capacity, initial_storage, demand):
    """this function simulates a reservoir over the years given
    
    PARAMETERS
    ==========
    inflows = a NumPy array of annual inflow volumes (MAF/yr)
    capacity = maximum reservoir volume (MAF)
    initial_storage = starting storage (MAF)
    demand = constant annual water demand (MAF/yr)
    
    RETURNS
    =======
    storage = arrays with storage volume over the years
    n_deficit_years = number of years the reservoir had a deficit
    reliability = fraction of years without a deficit
    """
    
    N = (len(inflows))
    storage = np.zeros(N)
    
    S_prev = initial_storage
    n_deficit_years = 0
    for t in range(N):
        S = S_prev + inflows[t] - demand
        
        if S > capacity:
            spill = S - capacity
            S = capacity
        elif S < 0:
            n_deficit_years += 1 
            S = 0
        
        storage[t] = S
        S_prev = S
    reliability= (N-n_deficit_years)/N
    return{
        "storage": storage,
        "n_deficit_years": n_deficit_years,
        "reliavility": reliability
    }

        
            
    
    

    


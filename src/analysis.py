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

    
df = load_streamflow("/Users/triep/Downloads/UU AW/Jaar 3/Modelleren van Aardsystemen/intro exercises/streamflow_project/data/AnnualStreamflow.csv")
 
stats = basin_stats(df, "Upper_Colorado_Basin")
print(stats)
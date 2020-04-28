# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 01:53:00 2020

@author: HARISH SHARMA V.H.S
"""
from sklearn.preprocessing import Imputer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv("Data.csv")
x=dataset.iloc[:-1].values
y=dataset.iloc[:,3].values
imputer=Imputer(missing_values=NaN,stratergy="mean",axis=0)


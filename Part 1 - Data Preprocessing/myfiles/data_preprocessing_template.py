#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:02:01 2018

@author: dianakardys
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../Data.csv') # import original data set
X = dataset.iloc[:,:-1].values # select dependent variables
Y = dataset.iloc[:,3].values # select independent variables

# Treating missing data
# (in statistics, imputation means substitution of missing values)
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) # always initialise the object! (creating an object 'imputer' that is an instance of class 'Imputer')
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])


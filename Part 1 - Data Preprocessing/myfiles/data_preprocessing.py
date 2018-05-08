#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 7

@author: DianaLog
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#####################################################################
# import and split data
#####################################################################
dataset = pd.read_csv('../Data.csv') # import original data set
X = dataset.iloc[:,:-1].values # select dependent variables
Y = dataset.iloc[:,3].values # select independent variables


#####################################################################
# Treating missing data
    # (in statistics, imputation means substitution of missing values)
#####################################################################
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) # always initialise the object! (creating an object 'imputer' that is an instance of class 'Imputer')
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])


#####################################################################
# Encoding categorical vars (strings into integers)
#####################################################################

# independent variable Y can use simple encoding: by substituting integer to unique strings, because there are only 2 unique categories
from sklearn.preprocessing import LabelEncoder
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

# dependent variable 'Country' in X use more complex encoding: create new column for each unique string and mark occurence with '1', because there are more than 2 unique categories
from sklearn.preprocessing import OneHotEncoder
labelencoder_X = LabelEncoder() # first complete simple encoding 
X[:,0] = labelencoder_X.fit_transform(X[:,0]) 
onehotencoder = OneHotEncoder(categorical_features = [0]) # then continue to complex encoding
X = onehotencoder.fit_transform(X).toarray()


#####################################################################
# Splitting data to training and test sets
#####################################################################
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


#####################################################################
# Data/feature scaling
#####################################################################
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)








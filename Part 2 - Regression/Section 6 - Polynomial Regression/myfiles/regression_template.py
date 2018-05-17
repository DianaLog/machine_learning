#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 16:03:36 2018

@author: dlog
"""
# Aim:
# General template for Regression models

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#####################################################################
# import and split data
#####################################################################
dataset = pd.read_csv('../somefile.csv')
X = dataset.iloc[:,1:2].values # independent vars
Y = dataset.iloc[:,2].values # dependent vars


#####################################################################
# splitting data to training and test sets
#####################################################################
# from sklearn.cross_validation import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 1.0/3.0, random_state = 0)


#####################################################################
# data/feature scaling
#####################################################################
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)
# sc_Y = StandardScaler()
# Y_train = sc_Y.fit_transform(Y_train)


#####################################################################
# fit Regression model
#####################################################################
#...


#####################################################################
# predict new result 
#####################################################################
Y_pred = regressor.predict(6.5)


#####################################################################
# plots
#####################################################################

plt.scatter(X, Y, color = 'green')
plt.plot(X, regressor.predict(X), color = 'orange')
plt.title('Regression Model')
plt.xlabel('...')
plt.ylabel('...')
plt.show()


# Plot curve with higher/smoother resolution
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'green')
plt.plot(X_grid, regressor.predict(X_grid), color = 'orange')
plt.title('Regression Model')
plt.xlabel('...')
plt.ylabel('...')
plt.show()
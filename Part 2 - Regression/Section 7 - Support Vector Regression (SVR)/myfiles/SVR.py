#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:20:02 2018

@author: dlog
"""
# Aim:
# Using Support Vector Regression (SVR) we predict the salary at specific position level.
# Independent variables are: Level (job position rank)
# Dependent variables are: Salary

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#####################################################################
# import and split data
#####################################################################
dataset = pd.read_csv('../Position_Salaries.csv')
X = dataset.iloc[:,1:2].values # independent vars
Y = dataset.iloc[:,2:3].values # dependent vars


#####################################################################
# splitting data to training and test sets
#####################################################################
# from sklearn.cross_validation import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 1.0/3.0, random_state = 0)


#####################################################################
# data/feature scaling
#####################################################################
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_Y = StandardScaler()
X = sc_X.fit_transform(X)
Y = sc_Y.fit_transform(Y)


#####################################################################
# fit SVR model
#####################################################################
from sklearn.svm import SVR
reg1 = SVR(kernel = 'rbf')
reg1.fit(X,Y)


#####################################################################
# predict new result 
#####################################################################
Y_pred = sc_Y.inverse_transform(
        reg1.predict(
                sc_X.transform(
                        np.array([[6.5]])
                        )
                )
        )


#####################################################################
# plots
#####################################################################

plt.scatter(X, Y, color = 'green', label = 'Real data')
plt.plot(X, reg1.predict(X), color = 'orange', label = 'Fitted SVR model')
plt.title('SVR model')
plt.xlabel('Career level (scaled with StandardScaler)')
plt.ylabel('Salary (scaled with StandardScaler)')
plt.legend()
plt.annotate(('Predicted salary at career level 6.5:\n '+ str(Y_pred[0])), 
             xy=(1, 1), xytext=(0.2, 2),
            horizontalalignment='right',
            verticalalignment='top'
            )
plt.show()
plt.close()

# Plot curve with higher/smoother resolution
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'green', label = 'Real data')
plt.plot(X_grid, reg1.predict(X_grid), color = 'orange', label = 'Fitted SVR model')
plt.title('SVR model (fine resolution)')
plt.xlabel('Career level (scaled with StandardScaler)')
plt.ylabel('Salary (scaled with StandardScaler)')
plt.legend()
plt.annotate(('Predicted salary at career level 6.5:\n '+ str(Y_pred[0])), 
             xy=(1, 1), xytext=(0.2, 2),
            horizontalalignment='right',
            verticalalignment='top'
            )
#plt.show()
plt.savefig('SVR model in Python.png', bbox_inches='tight', dpi = 110)
plt.close()



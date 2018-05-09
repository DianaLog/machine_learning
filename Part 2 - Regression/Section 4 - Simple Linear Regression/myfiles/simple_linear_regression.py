#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:53:11 2018

@author: dlog
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#####################################################################
# import and split data
#####################################################################
dataset = pd.read_csv('../Salary_Data.csv')
X = dataset.iloc[:,:-1].values  # independent variable, years of experience
Y = dataset.iloc[:,1].values    # dependent variable, salary


#####################################################################
# Splitting data to training and test sets
#####################################################################
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 1.0/3.0, random_state = 0)


#####################################################################
# fit simple linear regression model
#####################################################################
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)


#####################################################################
# predict test set results
#####################################################################
Y_pred = regressor.predict(X_test) # vector of predictions of dependent variable, predicted salaries for all observations


#####################################################################
# plotting
#####################################################################

# predictor performance on training set
plt.scatter(X_train, Y_train, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'orange')
plt.title('Salary versus Experience (training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
#plt.show()
plt.savefig('Salary versus Experience, training set.png', bbox_inches='tight')
plt.close()

# predictor performance on test set
plt.scatter(X_test, Y_test, color = 'blue')
plt.plot(X_train, regressor.predict(X_train), color = 'orange')
plt.title('Salary versus Experience (test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
#plt.show()
plt.savefig('Salary versus Experience, test set.png', bbox_inches='tight')
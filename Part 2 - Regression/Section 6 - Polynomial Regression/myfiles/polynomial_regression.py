#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:30:05 2018

@author: dlog
"""

# Aim:
# Using polynomial regression we predict the salary at specific position level.
# Independent variables are: Level (job position rank)
# Dependent variable are: Salary

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#####################################################################
# import and split data
#####################################################################
dataset = pd.read_csv('../Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values


#####################################################################
# fit simple linear regression model
#####################################################################
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, Y)

#####################################################################
# fit polynomial regression model
#####################################################################
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, Y)


# Plot linear
plt.scatter(X, Y, color = 'green')
plt.plot(X, lin_reg.predict(X), color = 'orange')
plt.title('Linear Regression, Truth or bluff')
plt.xlabel('Position level')
plt.ylabel('Salary')


# Plot polynomial vs linear
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color = 'black', label = 'Real data')
plt.plot(X, lin_reg.predict(X), color = 'orange', label = 'Fitted linear')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color = 'green', label = 'Fitted Polynomial of the 4th order')                 
plt.title('Linear vs Polynomial Regression model')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.legend()
plt.savefig('Linear vs Polynomial Regression model in Python.png', bbox_inches='tight')
plt.close()



#####################################################################
# predict Salary at level 6.5
#####################################################################
lin_reg.predict(6.5) # Linear Regression model
lin_reg2.predict(poly_reg.fit_transform(6.5))



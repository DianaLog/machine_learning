# author: dlog
# created: 14 May 2018


# Aim:
# Using multiple linear regression we build a model to check which circumastances made startups more profitable.
# Independent variables are: R&D costs ($), administration costs ($), marketing costs ($), geographical area.
# The dependent variable is profit ($) of the startup company.

#####################################################################
# import csv located one directory below
#####################################################################
dataset = read.csv('../50_Startups.csv')


#####################################################################
# Encoding categorical vars (strings into integers)
#####################################################################
dataset$State = factor(dataset$State, 
                       levels = c('California', 'Florida', 'New York'),
                       labels = c(1,2,3))


#####################################################################
# Splitting data to training and test sets
#####################################################################
library(caTools)
set.seed(123)
split = sample.split(dataset, SplitRatio = 0.8) # output interpretation: TRUE = training set, FALSE = test set
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#####################################################################
# fit Multiple Linear Regression model
#####################################################################
regressor = lm(formula = Profit ~ .,
               data = training_set)
summary(regressor)



#####################################################################
# predict test set results
#####################################################################
Y_pred = predict(regressor,
                 newdata = test_set)


#####################################################################
# Try backward elimination to find optimal model
#####################################################################

# STEP 1: fit model
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
summary(regressor)
# Results:
    #                   Estimate Std. Error t value Pr(>|t|)    
    # (Intercept)      5.013e+04  6.885e+03   7.281 4.44e-09 ***
    # R.D.Spend        8.060e-01  4.641e-02  17.369  < 2e-16 ***
    # Administration  -2.700e-02  5.223e-02  -0.517    0.608    
    # Marketing.Spend  2.698e-02  1.714e-02   1.574    0.123    
    # State2           1.988e+02  3.371e+03   0.059    0.953    
    # State3          -4.189e+01  3.256e+03  -0.013    0.990 
# Comments: from the table above, 'state2' and 'state3' has highest P-value so let's eliminate it and re-fit the model


# STEP 2: re-fit model
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend ,
               data = dataset)
summary(regressor)
# Results:
    #                   Estimate Std. Error t value Pr(>|t|)    
    # (Intercept)      5.012e+04  6.572e+03   7.626 1.06e-09 ***
    # R.D.Spend        8.057e-01  4.515e-02  17.846  < 2e-16 ***
    # Administration  -2.682e-02  5.103e-02  -0.526    0.602    
    # Marketing.Spend  2.723e-02  1.645e-02   1.655    0.105   
# Comments: from the table above, 'Administration' has highest P-value so let's eliminate it and re-fit the model


# STEP 3: re-fit model
regressor = lm(formula = Profit ~ R.D.Spend  + Marketing.Spend ,
               data = dataset)
summary(regressor)
# Results:
    #                   Estimate Std. Error t value Pr(>|t|)    
    # (Intercept)     4.698e+04  2.690e+03  17.464   <2e-16 ***
    # R.D.Spend       7.966e-01  4.135e-02  19.266   <2e-16 ***
    # Marketing.Spend 2.991e-02  1.552e-02   1.927     0.06 . 
# Comments: from the table above, 'Marketing.Spend' has highest P-value so let's eliminate it and re-fit the model


# STEP 4: re-fit model
regressor = lm(formula = Profit ~ R.D.Spend,
               data = dataset)
summary(regressor)
# Results:
    #               Estimate  Std. Error t value Pr(>|t|)    
    # (Intercept) 4.903e+04  2.538e+03   19.32   <2e-16 ***
    # R.D.Spend   8.543e-01  2.931e-02   29.15   <2e-16 ***
# Comments: The only variable left with p-value < 0.05 is  'R&D Spend' from the original data table. 
# Therefore the model shows there is a strong correlation between R&D expenditure and the profit generated by a startup.




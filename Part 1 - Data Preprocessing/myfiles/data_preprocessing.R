# author: DianaLog
# created: 8 May 2018


#####################################################################
# import csv located one directory below
#####################################################################
dataset = read.csv('../Data.csv')

#####################################################################
# Treating missing data
#####################################################################
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE) ), 
                     dataset$Age
                     )

dataset$Salary = ifelse(is.na(dataset$Salary), 
                     ave(dataset$Salary, FUN = function(x) mean(x,  na.rm = TRUE) ), 
                     dataset$Salary
)

#####################################################################
# Encoding categorical vars (strings into integers)
#####################################################################
dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1,2,3)
                         )

dataset$Purchased = factor(dataset$Purchased, 
                         levels = c('No', 'Yes'),
                         labels = c(0,1)
)

#####################################################################
# Splitting data to training and test sets
#####################################################################
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8) # output interpretation: TRUE = training set, FALSE = test set
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#####################################################################
# Data/feature scaling
#####################################################################
training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])

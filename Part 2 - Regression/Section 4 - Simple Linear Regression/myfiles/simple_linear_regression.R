# author: dlog
# created: 9 May 2018


#####################################################################
# import csv located one directory below
#####################################################################
dataset = read.csv('../Salary_Data.csv')


#####################################################################
# Splitting data to training and test sets
#####################################################################
library(caTools)
set.seed(123)
# split by dependent variable 'Salary'
split = sample.split(dataset$Salary, SplitRatio = 2/3) # output interpretation: TRUE = training set, FALSE = test set
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#####################################################################
# fit simple linear regression model
#####################################################################
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)
summary(regressor)


#####################################################################
# predict test set results
#####################################################################
Y_pred = predict(regressor, newdata = test_set)

#####################################################################
# plotting
#####################################################################
library(ggplot2)
# predictor performance on training set
ggplot() +
    geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary),
               colour = 'green') +
    geom_line(aes(x=training_set$YearsExperience, y=predict(regressor, newdata = training_set)), 
              colour = 'orange') +
    ggtitle(('Salary versus Experience \ntraining set')) +
    xlab('Years of Experience') +
    ylab('Salary')
ggsave('Salary versus Experience, training set.jpg', width = 6, height = 4, units = "cm", scale = 2, dpi = 130)

# predictor performance on test set
ggplot() +
    geom_point(aes(x=test_set$YearsExperience, y=test_set$Salary),
               colour = 'green') +
    geom_line(aes(x=training_set$YearsExperience, y=predict(regressor, newdata = training_set)), 
              colour = 'orange') +
    ggtitle('Salary versus Experience \ntest set') +
    xlab('Years of Experience') +
    ylab('Salary')
ggsave('Salary versus Experience, test set.jpg', width = 6, height = 4, units = "cm", scale = 2, dpi = 130)


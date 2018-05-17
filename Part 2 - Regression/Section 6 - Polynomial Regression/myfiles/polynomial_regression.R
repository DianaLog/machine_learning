# author: dlog
# created: 16 May 2018

# Aim:
# Using polynomial regression we predict the salary at specific position level.
# Independent variables are: Level (job position rank)
# Dependent variable are: Salary


#####################################################################
# import csv located one directory below
#####################################################################
dataset = read.csv('../Position_Salaries.csv')
dataset = dataset[,c(2,3)] # keep only Level and Salary cols

#####################################################################
# fit simple linear regression model
#####################################################################
lin_reg = lm(Salary ~ Level, data = dataset)

#####################################################################
# fit polynomial regression model
#####################################################################
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(Salary ~ ., data = dataset )
summary(poly_reg)


#####################################################################
# plots
#####################################################################
library(ggplot2)
ggplot() +
    geom_point(aes(x = dataset$Level, y = dataset$Salary, shape = 'Salary per career level')) +
    geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset), colour = 'Linear'), show.legend = TRUE) +
    geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset), colour = 'Polynomial of the 4th order')) +
    ggtitle('Linear vs Polynomial Regression model') +
    ylab('Salary ($)') +
    xlab('Career level') +
    # customise legend titles and shapes
    guides(shape = guide_legend(title = 'Real data', override.aes = list(linetype = 0)), 
           color = guide_legend(title = 'Fitted models'))
ggsave('Linear vs Polynomial Regression model.jpg', width = 9, height = 4, units = "cm", scale = 2.5, dpi = 100)
    

#####################################################################
# predict Salary at level 6.5
#####################################################################
# based on linear regression
y_pred = predict(lin_reg, data.frame(Level = 6.5))
# based on polynomial regression
y_pred = predict(poly_reg, data.frame(Level = 6.5,
                                      Level2 = 6.5^2,
                                      Level3 = 6.5^3,
                                      Level4 = 6.5^4))
y_pred


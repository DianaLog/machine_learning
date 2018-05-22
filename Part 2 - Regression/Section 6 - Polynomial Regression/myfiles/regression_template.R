# author: dlog
# created: 22 May 2018

# Aim:
# general regression template


#####################################################################
# import csv located one directory below
#####################################################################
dataset = read.csv('../Position_Salaries.csv')
dataset = dataset[,c(2,3)] # keep only Level and Salary cols

#####################################################################
# fit regression model
#####################################################################
# create a regressor here


#####################################################################
# predict new result
#####################################################################
y_pred = predict(regressor, data.frame(Level = 6.5))
y_pred

#####################################################################
# plots
#####################################################################
library(ggplot2)
# normal resolution
ggplot() +
    geom_point(aes(x = dataset$Level, y = dataset$Salary, shape = '...')) +
    geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset), colour = '...')) +
    ggtitle('Regression model') +
    ylab('...') +
    xlab('...') +
    # customise legend titles and shapes
    guides(shape = guide_legend(title = 'Real data', override.aes = list(linetype = 0)), 
           color = guide_legend(title = 'Fitted models'))
ggsave(' .jpg', width = 9, height = 4, units = "cm", scale = 2.5, dpi = 100)


# finer resolution
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
    geom_point(aes(x = x_grid, y = dataset$Salary, shape = '...')) +
    geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(levels = x_grid)), colour = '...')) +
    ggtitle('Regression model') +
    ylab('...') +
    xlab('...') +
    # customise legend titles and shapes
    guides(shape = guide_legend(title = 'Real data', override.aes = list(linetype = 0)), 
           color = guide_legend(title = 'Fitted models'))
ggsave(' .jpg', width = 9, height = 4, units = "cm", scale = 2.5, dpi = 100)


#Data Preprocessing

#Importing the dataset
dataset = read.csv('Data.csv')
#dataset = dataset[, 2:3]

#Taking Care Of Missing Data
# dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
# dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)
# 
# #Encoding Categorical Variables
# dataset$Country = factor(dataset$Country, levels = c('France', 'Spain', 'Germany'), labels = c(1, 2, 3))
# dataset$Purchased = factor(dataset$Purchased, levels = c('No', 'Yes'), labels = c(0, 1))

#Splitting The Dataset Into The Training And Testing Set
#install.packages('caTools') - To install a package in R we run this line, only need to do this once
library(caTools)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
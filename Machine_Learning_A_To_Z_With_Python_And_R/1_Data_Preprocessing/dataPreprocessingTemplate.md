# Data Preprocessing Template

Below are Data Preprocessing templates for obth Python and R that we will use in our machine learning models

These templates are reusable and useful because we will always need to import data and split our data into training and testing sets so we can teach the program how to label new input

### In Python

```python
#Import libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import Dataset
dataset = pd.read_csv('Data.csv')
inpen = dataset.iloc[:, :-1].values
depen = dataset.iloc[:, 3].values

#Splitting The Dataset Into The Training And Testing Set
from sklearn.cross_validation import train_test_split
inpen_train, inpen_test, depen_train, depen_test = train_test_split(inpen, depen, test_size = 0.2)
```

***

### In R

```r
#Data Preprocessing

#Importing the dataset
dataset = read.csv('Data.csv')
#dataset = dataset[, 2:3]

#Splitting The Dataset Into The Training And Testing Set
#install.packages('caTools') - To install a package in R we run this line, only need to do this once
library(caTools)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)
```

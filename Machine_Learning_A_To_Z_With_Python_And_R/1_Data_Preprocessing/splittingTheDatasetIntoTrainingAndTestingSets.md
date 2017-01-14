#Splitting The Dataset Into The Training And Testing Sets

###Training Vs Test Sets

The training set is the set of our data that includes both the independent and dependent variables. It is used to "train" or "teach" our program how to label the dependent variable on its own by measuring the relationship between the independent and dependent variables given in our testing set.

The testing set is the set of data the includes only the independent variables. This is the set where the program can use what it learned from the training set to label the dependent variables on its own.

***

###Splitting Dataset In Python

```python
#Import libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import Dataset
dataset = pd.read_csv('Data.csv')
inpen = dataset.iloc[:, :-1].values
depen = dataset.iloc[:, 3].values

#Taking Car Of Missing Data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0) #Grab the null values
imputer = imputer.fit(inpen[:, 1:3]) #Get the mean of all the other values in each of these columns
inpen[:, 1:3] = imputer.transform(inpen[:, 1:3]) # Set the null vals to the calculated mean

#Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encoder_country = LabelEncoder()
inpen[:, 0] = encoder_country.fit_transform(inpen[:,0])
onehotencoder = OneHotEncoder(categorical_features= [0])
inpen = onehotencoder.fit_transform(inpen).toarray()
encoder_purchased = LabelEncoder()
depen = encoder_purchased.fit_transform(depen)

#Splitting The Dataset Into The Training And Testing Set
from sklearn.cross_validation import train_test_split
inpen_train, inpen_test, depen_train, depen_test = train_test_split(inpen, depen, test_size = 0.2)
```

To split the data in Python we import the train_test_split class from the sklearn.cross_validation package

We then declare the variables for holding the testing and training datasets for both our independent and dependent variables. We use the train_test_split() method to split the data up for us and pass through 0.2 as our test_size - which means that 20% of our data will be testing data and 80% will be training data.

After running this code the arrays inpen_test and depen_test will contain dependent variables that our program labeled by itself based on the training data.

***

###Splitting Dataset In R

```r
#Data Preprocessing

#Importing the dataset
dataset = read.csv('Data.csv')

#Taking Care Of Missing Data
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)

#Encoding Categorical Variables
dataset$Country = factor(dataset$Country, levels = c('France', 'Spain', 'Germany'), labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased, levels = c('No', 'Yes'), labels = c(0, 1))

#Splitting The Dataset Into The Training And Testing Set
#install.packages('caTools') - To install a package in R we run this line, only need to do this once
library(caTools)
#set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

```

In R we can split the dataset into training and testing sets using the caTools library that we import using install.packages('caTools'), and include in our program using library(caTools). We then declare a variable called split and set it equal to the result of the sample.split() method. The sample.split() method takes our independent variable dataset$Purchased and the ratio of the split, which we set to 0.8 - which means that 20% of our data will be testing data and 80% will be training data.

The result of the sample.split() method is a array of of our ten items that looks like this: logi [1:10] TRUE TRUE TRUE TRUE TRUE TRUE FALSE TRUE TRUE FALSE

The TRUE values in this array represent the data that we used as training data, and the FALSE values represent the data we used as testing data

We save this data in our variables training_set and testing_set by calling the subset() method on our split dataset, and saving only the TRUE values into our training_set and the FALSE values into our testing_set.

#Feature Scaling

Lets say you have a dataset full of salaries:

| Name    | Salary |
|:------- | ------:|
| Joe     | 72000  |
| Hellen  | 48000  |
| Steve   | 54000  |
| Beth    | 61000  |
| Linda   |     0  |
| Kevin   | 58000  |
| B.Gates |99999999|
| Francis | 79000  |
| Mary    | 83000  |
| George  | 67000  |

Now you will notice that there are two Salary values that are potentially dangerous for our program. Namely, Bill Gates makes 99999999 and Linda makes 0. When we are trying to teach our program how to label data we have to make sure we take into account these types of data that could potentially throw off our model's calculations. If we want our program to work in the real world we have to make it account for situations like this because they exist. So we are going to use **Feature Scaling** so that we can "pan-out" our data so that the program doesn't get confused when it sees that Bill Gates makes 100 times more, and Linda makes infinitely less than everyone else.

***

###Feature Scaling In Python

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

#Feature Scaling
from sklearn.preprocessing import StandardScaler
stdScale_inpen = StandardScaler()
inpen_train = stdScale_inpen.fit_transform(inpen_train) #We need to fit the training set before we transform it
inpen_test = stdScale_inpen.transform(inpen_test) #We do not need to fit the test set before we transform it because it's already fitted to the training set
```

In python we import the StandardScaler class from the sklearn.preprocessing package to scale our data

First we create a StandardScaler() object (named stdScaler_inpen) to scale our independent variables. Then we scale both the training data and the test data separately by passing the data through the stdScale_inpen.fit_transform() and stdScale_inpen.transform() methods. We don't need to call fit_transform() on the test data because the test data because it is already fitted to the training data, so we just call transform() on it.

Now all of our features are scaled!

***

###Feature Scaling In R

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
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Feature Scaling
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])
```

In R we can just call the scale() method on both our training and test set. We only want to call it on the 2nd and 3rd columns (Age and Salary) because the other variables (Country and Purchased) are categorical variables that have been encoded to certain values. We would not gain anything by scaling these values, but we would lose our ability to tell which category each value was representing since the scaling would average them all together.

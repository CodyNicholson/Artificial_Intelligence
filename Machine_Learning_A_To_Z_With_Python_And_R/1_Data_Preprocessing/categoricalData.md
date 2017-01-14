#Categorical Data

**Categorical Date** is data that can be put into categories like a country, gender, yes/no, true/false, languages spoken, etc

When we set up a machine learning algorithm we want to be able to do mathematical calculations to get our program to do what we want. We can't do math with Categorical Variables because they are not number values. That is why we have to encode each of our categorical variables into number values so we can work with them in our ML algorithms.

***

###Encoding Categorical Data In Python

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
```

In the Encoding Categorical Data section of the above code we import two different encoders and send them our columns of data

The LabelEncoder is used for labeling the countries each a different number. We do this by first declaring the encoder_country variable, and then fitting our inpen data at the column with index 0 (The countries column). For example, it might make France = 1, Germany = 2, and Spain = 3.

Since the Purchased column in our table only has two options (Yes/No) we can use the OneHotEncoder to quickly fit our depen variable by passing it the data stored in the fourth column. For example, it might make No = 0, and Yes = 1.

***

###Encoding Categorical Data In R

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
```

In R we can encode our Categorical Data into numbers in a one liner

First we get the column of data we want to encode using dataset$ColumnName and we set the data in that column equal to the result of the factor() method. The factor() method takes the data from dataset$ColumnName, and for all data with the value 'France' it changes the value to 1, 'Spain' becomes 2, and 'Germany' becomes 3.

We go the same for dataset$Purchased and all our Categorical variables become encoded so we can use them in our ML algorithms

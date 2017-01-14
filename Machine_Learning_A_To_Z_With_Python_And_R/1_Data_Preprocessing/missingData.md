#Missing Data

| Country | Age | Salary | Purchased |
|:------- | ---:| ------:| ---------:|
| France  | 44  | 72000  | No        |
| Spain   | 27  | 48000  | Yes       |
| Germany | 30  | 54000  | No        |
| Spain   | 38  | 61000  | No        |
| Germany | 40  |        | Yes       |
| France  | 35  | 58000  | Yes       |
| Spain   |     | 52000  | No        |
| France  | 48  | 79000  | Yes       |
| Germany | 50  | 83000  | No        |
| France  | 37  | 67000  | Yes       |

In the above table you can see that their are two missing data spots near the middle of the table

To solve this problem we can populate our missing data spots with the mean of the other data in that column

***

###In Python

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
from sklearn.preprocessing import Imputer #Import the Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0) #Grab the null values
imputer = imputer.fit(inpen[:, 1:3]) #Get the mean of all the other values in each of these columns
inpen[:, 1:3] = imputer.transform(inpen[:, 1:3]) # Set the null vals to the calculated mean
```

As you can see in the comments, we grab the null values that are labeled "NaN" and replace them with the mean of the other values in the same column

***

###In R

```r
#Importing the dataset
dataset = read.csv('Data.csv')

#Taking Care Of Missing Data
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)
```

In R what we are doing is creating an if else statement by calling the built-in ifelse function with the conidtion that the input data is null: is.na(dataset$columnName)

If the data at a location is null then we calculate the average of the other data in the same column and set the null spots equal to that average

Else (if the data is not null), then just return the existing data

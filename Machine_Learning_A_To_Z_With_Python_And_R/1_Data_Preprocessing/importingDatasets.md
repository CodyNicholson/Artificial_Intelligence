#Importing Datasets

To import datasets in python you need to set your working directory by simply making sure that your python file is in the same directory as your data file

Once you have your working directory set, you can get your dataset into your python program by using the below code:

```python
#Import libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import Dataset
dataset = pd.read_csv('Data.csv')

inpen = dataset.iloc[:, :-1].values
depen = dataset.iloc[:, 3].values
```

Now we have the data saved in the dataset variable

Remember that when we make a machine learning algorithm we need to declare our independant variables and our dependant variable separately so that we can "teach" our the program how to infer the dependant variable from the independant variable

To do this we call the .iloc method on the dataset to parse the it and save every row and every column EXCEPT the last one into the inpen variable (The last column contains the dependant variable, so we want to avoid that)

We then use .iloc to get every row or our dataset but only the data at column with index 3, and put that data in our depen variable

***

###In R this is much easier

```r
#Importing the dataset
dataset = read.csv('Data.csv')
```

In R we can just import the dataset into our program using the read.csv() method

Unlike in python, once the data file is input into your program it will be saved in the program and does not need to be inputted every time you run your program

We do not need to worry about saving the independent and dependent variables in R

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Import libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import Dataset
dataset = pd.read_csv('Data.csv')
inpen = dataset.iloc[:, :-1].values
depen = dataset.iloc[:, 3].values

"""
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
"""

#Splitting The Dataset Into The Training And Testing Set
from sklearn.cross_validation import train_test_split
inpen_train, inpen_test, depen_train, depen_test = train_test_split(inpen, depen, test_size = 0.2)

"""
#Feature Scaling
from sklearn.preprocessing import StandardScaler
stdScale_inpen = StandardScaler()
inpen_train = stdScale_inpen.fit_transform(inpen_train) #We need to fit the training set before we transform it
inpen_test = stdScale_inpen.transform(inpen_test) #We do not need to fit the test set before we transform it because it's already fitted to the training set
"""

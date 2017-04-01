# Nonlinear SVMs

SVM decision boundaries come in all shapes, they do not have to be lines

For example, if all of your data points from class one is located near the origin of a coordinate plane, and all the data points of class two are farther away from the origin then a SVM would create a decision boundary that would be a circle separating class one and two that maximizes the distance between the nearest point from either class

You can add features so your SVM will draw the best line given your scatterplot

***

### Kernel Trick For SVM - The Kernel Parameter

In our previous code:

```python
import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
clf = SVC(kernel="linear")
clf.fit(features_train, labels_train)

#### store your predictions in a list named pred
pred = clf.predict(features_test)

#### find accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc

def submitAccuracy():
    return acc
```

Notice the line where we declare our classifier: clf = SVC(kernel="linear")

We are using the kernel parameter of "linear" to create a classifier that will produce a straight line when it is asked to predict the labels of the features we pass through

***

### The C Parameter

The **C Parameter** controls the trade-off between a smooth decision boundary and classifying training points correctly

A large value of C in your classifier means that you will get more training points correct, and will have a less linear decision boundary

A small value of C means that your decision boundary will be more straight/linear

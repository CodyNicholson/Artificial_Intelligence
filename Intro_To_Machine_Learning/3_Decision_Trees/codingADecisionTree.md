#Coding A Decision Tree

```python
#Main.py
import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()

### This calls the method in the other python file the classifies the data
clf = classify(features_train, labels_train)

#### Creates a visual representation of the classifed data
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
```

```python
#Classify.py
def classify(features_train, labels_train):
    
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)
    
    return clf
```
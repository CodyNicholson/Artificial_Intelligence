# Outliers

Let's say you have a scatterplot with two distinct clusters of data

It should be easy for a SVM to draw a line between the two that maximizes the distance between the closest two points from either class - but there is a catch

What if in the middle of the class one cluster there is a single point from class two? Now it is impossible to draw a perfect line between the two classes because no matter what line you draw you will always have at least one point on the wrong side of the line!

This one point from class 2 in the middle of the class 1 cluster can be called an **outlier**

When SVM finds an outlier it will still try to do the best it can to draw a line that best divides the data, and it will let you know that the outlier is there

In this way, the SVM algorithm will not be perfect but it will give you valuable data

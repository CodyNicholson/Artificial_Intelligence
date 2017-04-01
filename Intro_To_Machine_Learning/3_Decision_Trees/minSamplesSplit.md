# Min_Samples_Split

The **min_samples_split** is an parameter you can set in your DecisionTreeClassifier that tells the algorithm when to stop splitting data in your decision tree - the default value is 2

When you ask questions in your decision tree you split up your original input, and if you keep asking questions eventually you will only be left with a few data points left. The decision tree will stop splitting data for a branch when the amount of data <= to 2.

-

By having a small min_samples_split set for your classifier, your data will be much more finely tuned - and your decision surface will be more eratic

By having a large min_sample_size your data will be less finely tuned and more general - and your decision surface will look a lot cleaner

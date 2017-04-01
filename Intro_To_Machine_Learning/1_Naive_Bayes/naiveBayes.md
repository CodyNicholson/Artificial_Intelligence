# Naive Bayes

### Sklearn Interpreted

```python
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]) #X represents features
Y = np.array([1, 1, 1, 2, 2, 2]) # Y represents Labels
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB() # This is how we create our classifier
clf.fit(X, Y) # The fit() method trains our classifier based on features and labels
print clf.predict([[-0.8, -1]]) # Now that the classifier is trained it can be used to label new input
```

***

### Bayes Rule

Prior = P(C)
Sensitivity = P(Pos|C)
Specitivity = P(Neg|7C)

When you receive a positive test result - you take your Prior and you multiply in the probability of this test result given C (P(Pos|C)) and given not C (P(Pos|7C))

This provides you with the probabilities of your test being true or false

You can add these together to get the **total probability** for your test, but it will normally not equal 1

To get to one you take your probabilities of your test being true and false, and you divide each of those probabilities by your test's total probability

The two numbers you get from doing this calculation is the desired posterior probability (P(C|Pos)) and (P(7C|Pos)) which should add up to 1 if you did everything correctly

-

A simple example:

If you are trying to program to learn from text messages you can use Naive Bayes

Lets say you have two people texting each other, Chris and Sara

Chris talks about: 10% Love, 80% Deals, and 10% Life

Sara talks about: 50% Love, 20% Deals, and 30% Life

Let's suppose you are trying to figure out who sent the email: "Love life!", and lets suppose that you are sure it was either Chris or Sara

That means that: P(Chris) = 0.5 and P(Sara) = 0.5 which means: the probability or it being Chris is 50% and Sara is also 50%

Using Naive Bayes, since we know Sara talks more about Love and Life than Chris, our algorithm would determine that it was most likely Chris

This is calculated by the computer as:

Chris: .1 (love) x .1 (life) x .5 (prior) = 0.05

Sara: .5 (love) x .3 (life) x .5 (prior) = 0.075

Since Sara has a higher value, it was most likely an email from Sara

Now in order to calculate the **Posterior Probabilities** we divide each of our probabilities (0.05 and 0.075) by our total probability (0.05 + 0.075 = 0.125)

Chris: 0.05/0.125 = 0.4 or 40%

Sara: 0.075/0.125 = 0.6 or 60%

***

### Naive Bayes Strengths

- It is easy to implement and efficient to run

***

### Naive Bayes Weaknesses

- Naive Bayes is called Naive because, while it does a great job, it does not take into account the order of the words which is an important factor in the equation - but it is good enough

- It cannot handle phrases with multiple words, like searching 'Chicago Bulls' would result in pictures of Chicago, and pictures of Bulls if you used Naive Bayes

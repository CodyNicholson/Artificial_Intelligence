#Stochastic Search

Stochastic Search gives a good guess at the correct answer and will get close, but is not gaurenteed to find the best answer

It is faster than Brute-Force but less accurate

We generate random numbers that are the indices where we evaluate the function

We store a reference to the best solution element and keep checking the other elements to see if they are a better answer

The code is the same as Brute-Force Search, but instead of having a while loop check every element in the list, we have a for loop that checks however many random indices you want to check
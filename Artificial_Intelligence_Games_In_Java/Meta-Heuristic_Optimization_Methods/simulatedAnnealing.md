#Simulated Annealing

**Simulated Annealing** is a good algorithm to avoid local optimum (Hill-Climbing's Problem) and finding the global optimum instead

Lots of applications use Simulated Annealing: Traveling Salesperson, AI, Training Neural Nets

***

###How does it work?

Simulated Annealing mimics the annealing process to solve an optimization problem

It uses a temperature parameter that controls the search

The temperature parameter typically starts off high and is slowly "cooled" or lowered in every iteration

At each iteration a new point is generated (usually at random) and its distance from the current point is proportional to the temperature

If the new point has a better function value it replaces the current point and iteration counter is incremented. It is possible to accept and move forward with a worse point.

The probability of doing so is directly dependant on the temperature. This unintuitive step sometimes helps identify a new search region in hope of finding a better minimum.

-

When the **temperature is high** we accept bad moves with higher probability

When the **temperature is low** we do not accept bad moves

***

##Algorithm

1. We set the initial temperature and create a random initial solution

2. We iterate until a stop is met, for example: the system has sufficently cooled or an approximated solution has been found

3. We generate a neighbor, For example: make some little change to the current state

4. We decide whether to move to that neighbor state with the help of the acceptance function

5. Decrease the temperature + looping (Repeat from step 2)
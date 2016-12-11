#Heuristics Vs. Meta-Heuristics

###Heuristics

Heuristics can do better than Brute-Force and Hill-Climbing Algorithms

There are several problems that are very hard to solve exactly, most of which are graph algorithms like: The Hamiltonian-cycle problem, Traveling Salesman Problem, coloring problem

To solve these problems efficiently we make our goal to get an approximate solution instead of a exact one

**Heuristic Algorithms are going to find approximate solutions, not exact one**

-

A* search is a Heuristic Algorithm

We can use Heuristics when we know the problem that we want to solve in advance and we use some feature of the given problem

-

We are going to use the Heuristic Alpha-Beta Pruning Algorithm to solve problems like Chess, and Tic-Tac-Toe

**Alpha–beta pruning** is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree

***

###Meta-Heuristics

Like regular Heuristics, we want to get a good guess of the solution and we want it fast

The difference between Heuristic Algorithms and Meta-Heuristic Algorithms is that **Meta-Heuristic Algorithms are problem independant**

In other words, our algorithm knows nothing about the problem that it wants to solve, its kind of a black box

For example: genetic algorithms, simulated annealing, or particle swarm optimization are Meta-Heuristic Algorithms

***

###The Difference

#####Heuristics

Not that generic: we use some underlying feature of the given problem like in Chess of Tic-Tac-Toe we can build a tree-like structure for this problem

#####Meta-Heuristic

Generic: we do NOT use some underlying feature of the given problem like in genetic algorithms and simulated annealing, we cannot make a tree-like structure for this problem
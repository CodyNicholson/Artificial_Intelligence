# Iterative Deepening Depth-First Search

Very important in artificial intelligence and robotics

-

BFS is very good for local searches but it is very memory consuming

We have to keep pointers and references in a queue

-

DFS can be implemented easily with recursion BUT it keeps going further and further

DFS is memory friendly

-

Can we create a searching algorithm that inherits the advantages of both DFS and BFS?

Yes, it is the **Iterative Deepening DFS Algorithm**

***

The algorithm works like this:

It visits the nodes in the search tree in the same order as DFS, but the cumulative order in which nodes are first visited is effectively the same as BFS

Keep going deeper and deeper in the given tree with DFS on each iteration (By keeping a deep parameter count)

The time complexity of IDDFS in well-balanced trees works out to be the same as DFS

The disadvantage is that we keep recomputing the same problem over and over again -- it isn't that bad: O(cN)~O(N) where c is a constant

***

## A* Search

Important in AI because it is used in path-finding and graph traversal

Thus, it can solve path-finding problems in games

However, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance (Dijkstra or BFS)

It is similar to Dijkstra: A* achieves better time performance by using heuristics

It uses a knowledge-plus-heuristic cos function of node x (usually denoted f(x)) to determine the order in which the search visits nodes in the tree. The cost function is a sum of the two functions:

- g(x) the known distance from the starting node to the current node x

- h(x) "heuristic estimate" of the distance from x to the goal

Note: if h(x) = 0, that is the common shortest path problem

It is like the classic Dijkstra method, but here we make decisions according to the f(x)=g(x)+h(x) function

This is good because if there are obstacles in the way between us and the final destination, A* helps to find the best path possible

Greedy best first search may lead us to dead ends instead

Manhattan distance: we usually use this kind of heuristic

- Keep tracking what is the distance between us and the goal

- NOT the Euclidean distance

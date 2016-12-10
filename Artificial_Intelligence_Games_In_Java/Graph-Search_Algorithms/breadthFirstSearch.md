#Breadth First Search (BFS)

BFS is good when we have a graph and we want to visit every *node* exactly once

We visit the neighbours, then the neighbor's neighbors, and so on

BFS visits every vertex on a **row by row** basis

-

Runtime complexity is linear: **O(V+E)**

The memory complexity is not good because we have to store lots of references/pointers

-

This memory complexity is the reason that Depth-First Search is usually preferred

Unlike DFS, BFS constructs a shortest path

Dijkstra's Algorithm does a BFS if all the edge weights are equal to 1

***

##BFS Sudo-code

```
bfs(vertex)

    Queue queue
    vertex set visited to true
    queue.enqueue(vertex)

    while queue is not empty
        actual = queue.dequeue()

        for v in actual neighbors
            if v is not visited
                v set visited true
                queue.enqueue(v)
```

***

###Applications for BFS

In AI/ML it can be used by robots to discover the surrounding area more easily

It is also impotant in **maximum flow**: Edmonds-Karp algorithm uses BFS for finding augmenting paths

It is used in Cheyen's algorithm for garbage collection to maintain active references on the heap memory (Detects all the references on the heap)

It is used for **Serialization/deserialization** of a tree like structure (when order does matter) because it allows the tree to be reconstructed in an efficient manner
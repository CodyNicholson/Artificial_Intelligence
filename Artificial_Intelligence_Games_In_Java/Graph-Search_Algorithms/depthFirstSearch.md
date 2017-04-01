# Depth-First Search (DFS)

DFS is a widely used graph traversal algorithm like BFS

It explores as far as possible along each branch before backtracking

Its runtime complexity is: **O(V+E)**

The memory complexity is a bit better than that of BFS

***

### DFS Pseudo Code - Recursive

```
dfs(vertex)

    vertex set visited true
    print vertex

    for v in vertex neighbors
        if v is not visited
            dfs(v)
```

-

### DFS Pseudo Code - Iterative

```
dfs(vertex)

    Stack stack
    vertex set visited true
    stack.push(vertex)

    while stack is not empty
        actual = stack.pop()

        for v in vertex neighbors
            if v is not visited
                v set visited true
                stack.push(v)
```

***

## Applications of DFS

Topological ordering

It is used in the Kosaraju Algorithm for finding strongly connected components in a graph - which is used in recommendation systems

Detecting cycles (checking whether a graph is a Directed Assembly Graph (DAG) of not)

Generating mazes OR finding the way out of a maze

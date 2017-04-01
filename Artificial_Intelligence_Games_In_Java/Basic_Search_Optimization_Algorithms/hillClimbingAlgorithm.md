# Hill Climbing Algorithm

The algorithm starts at a given **x** position

It keeps comparing the adjacent elements to try and find the maximum/minimum among them

As it compares, it updates its solution like brute-force and continues **until it cannot find a better solution**

This means if you have a function with two hills and you run the Hill Climbing Algorithm, it will only ever go up **one** of those hills, and when it reaches the top and cannot find an a better adjacent solution, it will terminate

It usually stops at a local max/min (Local, meaning not the global solution, one of the smaller hills)

In order to find the global optimum we should start the algorithm again and again several times (repeated local search)

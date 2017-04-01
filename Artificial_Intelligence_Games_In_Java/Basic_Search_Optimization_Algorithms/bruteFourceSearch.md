# Brute-Force Search

In a Brute-Force Search we iterate through the given interval and do a brute-force maximum/minimum find

Brute-force search is a linear search-meaning we have to consider all of the items n (Unlike binary search where we only consider log(n))

We systematically enumerate all possible candidates for the solution

We examine all possible solutions causing us to be very slow BUT we always find the optimal solution

It is slow because the number of candidates is extremely large

***

### Pseudo Code:

```
solution equals first value

while there is a next candidate:
    if next candidate is a better solution:
        solution = next candidate
```

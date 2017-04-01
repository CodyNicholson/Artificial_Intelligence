# Tabu Search

**Tabu Search** is a Meta-Heuristic Search method

Local search methods have a tendency to become stuck in suboptimal regions (like the hill climbing algorithm)

-

In Tabu search worsening moves can be accepted if no improving move is available (Like when you are stuck in a local min/max)

Also, prohibitions (tabu) are introduced to discourage the search from coming back to previously-visited solutions

-

In Tabu Search we have to use a data structure to store the prohibited points, and we have to check according to this data structure whether a move is allowed or not

***

### Tabu Tenure

When a move is made tabu it is added to the so called tabu list with a certain value: this value is the "tabu tenure"

With each iteration the tabu tenure is decremented by by one

When the tabu tenure of a certain move is 0, then the certain move can be accepted

-

### Aspiration Criteria

Aspiration criteria allows a tabu move to be selected based on certain constraints

For example, the given move allows a new global best solution

In these situations the move is accepted and its tabu tenure is renewed

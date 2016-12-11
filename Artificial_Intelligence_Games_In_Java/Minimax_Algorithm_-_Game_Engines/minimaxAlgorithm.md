#Minimax Algorithms

**Minimax** is a decision rule in decision theory and game theory used for minimizing the possible loss for a maximum loss scenario

-

The algorithm assumes that both players will play to the best of their ability

**Max** - We would like to maximize our probability of winning

**Min** - We want to minimize the other player's probability of winning

This algorithm can be used in two-player games like tic-tac-toe

-

The Minimax Algorithm is a recursive algorithm for choosing the next move in a game

A value is associated with each position of state of the game: +1: win situation, 0: neutral situation, -1: lose situation

We construc a tree like structure with as many bracnches as the number of possible outcomes

***

For small games such as tic-tac-toe we can construct the full tree at the beginning: only 9! (factorial) different scenarios

For chess we have to use heuristics because we cannot store the entire game tree

For example: the chess computer Deep Blue looked ahead at least 12 plies, then applied a heuristic evaluation function

This function predicts whether that situation is a +1 win situation, 0 neutral situation, or -1 lose situation

***

##The Algorithm Behavior

The root of our game tree is the current state of the game - if it is our move then our goal is to maxmize our chances of winning

The first level of edges under the root represent the **first-player's potential moves**

Each node that those each of those edges leads to represent the updated state of the game after each of those moves

Then we look at the next layer of edges that represent the second player's moves, and that lead us to all the potential states of the game after the second players moves - if the second player is our opponent our goal is to minimize their chance of winning

At the end of this tree structure we have our **last potential game states** and our algorithm decides if these states are win situations, neutral situations, or lose situations

**We might only have a few layers in our game tree because of memory restrictions**, each additional layer will make our program a more accurate but will consume more memory

-

We use DFS to go through our game tree that we constructed, and for every level where it is our move we select the highest value (of the given: +1, 0, -1) to maximize our chances of winning

For every level that it is the opponents move, we select the lowest value to minimize there chance of winning

Once we have considered all the possible moves we can make for the next **x** turns (That we decide based on how much memory we want to consume), we select the optimal move

# Game Trees

A **Game Tree* is a directed graph whose nodes are positions in the game

The edges of this graph are the "moves" you can make in the game

The complete game tree includes every possible outcome of the game

-

Usually it would be impossible to build the entire game tree for certain games, like chess

The tree can get very big with only a few moves

To handle large games like chess, computer programs are forced to estimate who is winning and losing by sampling a small portion of the entire game tree

So we create the first few levels of the tree and guess at the best moves to make with the help of a heuristic function

-

The game tree is important in AI because if we want to get the best move in a game, we have to search the game tree with a **minimax algorithm**

Basically, we need to use Depth-First Search

#Alpha-Beta Pruning

The problem with the minimax algorithm is that there are sometimes branches of the game tree we should not visit

We use **Alpha-Beta Pruning** to reduce the time complexity of our minimax algorithm by minimizing the number of branches we visit

This can be especially helpful for large game trees like chess

-

Iterative deepening is another algorithm that helps the minimax algorithm and is usually used in conjunction with alpha-beta so that a reasonably good move can be returned even if the algorithm is interrupted before finishing execution

-

##How does Alph-Beta Pruning work?

We have to assign two extra variables to every node: alpha and beta

**Alpha**: best already explored option along path to the root for maximizer, only maximizer nodes can change its value. Alpha is the maximum value the maximizer can receive. It is initialized to minus infinity.

**Beta**: best already explored option along path to the root for minimizer, only minimizer nodes can change its value. Beta is the minimum score the minimizer can receive. Initialized to positive infinity.

When **alpha is greater or equal to beta** we can prune that branch

***

###In Summary

After we construct the minimax tree, we can guess whether we can traverse the branch/sub-tree or not

By preventing the minimax algorithm from searching through unecessary branchs/sub-trees we can make the algorithm more efficient
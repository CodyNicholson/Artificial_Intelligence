# Genetic Algorithms

**Genetic Algorithms (GA)** are search heuristics that mimic the process of natural selection

GA is used to generate useful solutions to optimization and search problems

Generate solutions to optimization problems using techniques inspired by natural evolution, such as mutation or crossover

A candidate solution is evolved toward better and better solutions

Each candidate solution has a set of properties (genes) which can be mutated and altered

(Usually solutions are represented in binary)

***

### Algorithm Basics

The evolution usually starts from a population of randomly generated individuals

It is an iterative process - with the population in each iteration called a generation (Every generation mutates from the previous generation)

In each generation, the fitness of every individual in the population is evaluated

The fitness is usually the value of the objective function in the optimization problem being solved

-

More fit individuals are selected from the current population, and each individual's genome is modified (recombined and possibly randomly mutated) to form a new generation

The new generation of candidate solutions is then used in the next iteration

Commonly, the algorithm terminates when either a maximum number of generations has been produced, or a satisfactory fitness level has been reached for the population

***

## Genetic Algorithms - Chromosomes

In order to use genetic algorithms we first have to encode any potential solution into "chromosomes"

For example: string of real numbers OR more often a binary bit string ",, 100011011010111011000001"

At the beginning of the algorithm a large population of random chromosomes is created

Each chromosome represents a different solution

The fitness function tells us how good that chromosome is

Our program will return doubles, but we can easily convert those doubles into binary representation for use in our chromosomes, which makes mutation easy

***

## Genetic Algorithms - Crossover

The **crossover** is the method by which we mutate our chromosomes

We take the binary representations of all the possible solutions

Crossover works by using a **crossover threshold** to determine when to change each bit of the binary string that can be found in our list of possible solutions

For example, if your crossover threshold is 0.35 and our solution is "0100110":

We generate a random value between 0.00 and 1.00 for the first bit: 0.43

Since 0.43 is greater than our crossover threshold, we do not switch the first bit from "0" to "1"

For the second bit we randomly generate: 0.22

Since 0.22 is less than our crossover threshold, we change the second bit from "1" to "0" making our new solution: "0000110"

We generate a random number for each other bit in our string (there are 5, so five more random numbers) and we swap our bits when we generate numbers below 0.35 - our crossover threshold

-

If our crossover threshold is low, we will make few changes and our algorithm will be less accurate but faster

If our crossover threshold is high we will make lots of changes with higher probability and our algorithm will get slower but more accurate

***

## Genetic Algorithms - Mutation

**Mutation** does exactly the same operation as Crossover, but with only one chromosome

We iterate through the genes and make mutations if necessary (flip the bits) based on the **mutation threshold** that serves the exact same purpose and function as the crossover threshold

-

**Mutation** is a divergence operation, it forces one of more members of the population to discover other regions of the search space - so it is essential in order to find the global optimum

On the other hand, crossover is an operation which drives the population towards a local max/min

If we use only crossover it will yield approximately the same result as the hill-climbing algorithm

Crossover is a more frequent operation than mutation, mutation only affects few members of the population

***

## Algorithm

1. We have to encode the possible solutions as strings of bits, Basically we have to construct the chromosomes for the problem

2. We have to define a fitness function, Better solutions have a higher fitness value

3. While solution is not found:
    Select a random sub-population
    Perform crossover on the sub-population
    Perform mutation on the sub-population
    Calculate fitness of the sub-population
    Store the best individual
    Then we have to keep iterating until we find the best solution, or we have done enough iterations

-

### Advantages

Applying GA to a new problem is very simple: we just have to define a new fitness function best suited to the new problem

GA will not often get stuck in a local optimum because the crossover and mutation processes produce radically different chromosomes

"Survival of the fittest" principle is quite effective

It scales well even in high dimensions


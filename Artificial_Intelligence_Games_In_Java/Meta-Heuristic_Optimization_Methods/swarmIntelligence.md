#Swarm Intelligence - Artifical Intelligence

**Swarm Intelligence** is a collective behavior of self-organized systems

Independant entities following very simple rules can produce something quite complex

Swarm intelligence systems consist of a population of **agents**

These agents interact with each other and the environment locally

The intuition comes from biological systems, like a colony of ants

***

##Particle Swarm Optimization

The goal is to make an optimization algorithm that will find the global optimum for a function

-

**Particle Swarm Optimization** consists of a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality

It is one of the swarm intelligence algorithms (ant colony optimization is another famous one)

**Swarm Intelligence**: the collective behavior of decentralized, self-organized systems

- The inspiration often comes from nature, especially biological systems

- Consist typically of a population of simple agents (particles, ants, bees)

- Agents are interacting locally with one another and with their environment

- The agents follow very simple rules - lead to the emergence of "intelligent" global behavior, unknown to individual agents

-

###Algorithm

We create artifical particles and move them around in the search-space according to simple mathematical formulas over the particle's position and velocity

Each particle's movement is influenced by its local best known position

Each particle is guided toward the best known positions in the search-space, whcih are updated as better positions are found by other particles

This is expected to move the swarm toward the best solutions

Advantage: we do not need the gradient - the problem does not need to be differentiable (it is usually required)

-

```
**f: R^n -> R** is the cost function we want to optimize, the aim is to find the global optimum for this f function

**S** is the number of particles in the swarm
**x_i** is the position of particle i
**v_i** is the velocity of particle i
**p_i** best known position of particle i
**g** best known position of entire swarm / best global
```

1.) For every particle i=1, 2 ... S:

- Initialize the **x_i** position for every particle

- Initialize the **v_i** velocity for every particle

- Initialize the particle best known position **p_i <- x_i**

- Update best position of the swarm:

```
if f(p_i) < f(g) then g <- p_i
```

-

```
**f: R^n -> R** is the cost function we want to optimize, the aim is to find the global optimum for this f function

2.) while(condition is met):

    for every particle i=1, 2, ... S
        for every dimension d=1, 2, ... n

            Generate random numbers r_p and r_g
            update velocity:
            v_i,d <- w*vi,d + c1 * r_p(p_i,d - x_i,d) + c2 * r_g(g_d - x_1,d)

        update particle position: x_i <- x_i + v_i
        if f(x_i) < f(p_i) then p_i <- x_i
        if f(p_i) < f(g) then g <- p_i (update best solution)
```

The equation from above explained:

```
v_i,d <- w*vi,d + c1 * r_p(p_i,d - x_i,d) + c2 * r_g(g_d - x_1,d)
```

**w** is the Inertia Weight: Defines the memory of the system, how significant is the last step

**c1** is the Local Weights: Defines the tendency to return to the particle's best previous position "attractor"

**c2** global weights: Defines the tendency to move towards the neighborhood's best previous position. c1 = c2 usually "repellent"

-

This is the **Local Neighborhood**:

```
c1 * r_p(p_i,d - x_i,d)
```

This is the **Global Neighborhood**:

```
c2 * r_g(g_d - x_1,d)
```

-

If the **w** inertia weight is big, we are going to make a global search (This will be slower but more accurate)

If the **w** inertia weight is small, local search is dominant (Faster, less accurate)
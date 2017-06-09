# AI Systems As Intelligent Agents

An **agent** is something that can:

- perceive its "environment" through sensors (percepts)

- Act upon that environment through actuators (or effectors)

An agent is defined by its agent function

- A percept sequence is the complete history of everything the agent has ever perceived

- The agent function maps all possible percept sequences onto actions

We implement an agent by writing an agent program

***

### Example Agent: A Vacuum Robot

Percepts: 2-tuple [square, state]

Actions: Left, Right, Suck

Agent function determines whether it's a good or bad element

-

A good agent function:

```
Percept sequence, Action
[A,Clean], Right
[A,Dirty], Suck
[B,Clean], Left
[B,Dirty], Suck
[A,Clean][A,Clean], Right
[A,Clean][A,Dirty], Suck
```

-

### What Makes An Agent Intelligent?

We need to define a performance measure for the agent

At any given time, an intelligent agent selects an action which, given its percept sequence and whatever built-in knowledge the agent has, maximizes the expected value of the performance measure

-

### A Performance Measure For The Vacuum

Assume:

- The agent has a lifetime of x time steps

- The performance measure awards 1 point for each clean square at each time step

- The agent knows the geography of its environment (2 squares, A and B)

- Initial dirt distribution and location of the agent are not known

- 3 possible actions that the agent can perform

- The agent correctly perceives its location and whether that location contains dirt

Under these conditions, the agent function shown in the above table is intelligent/rational

***

## PEAS Analysis

**P**erformance Measure, **E**nvironment, **A**ctuators, **S**ensors

- Designing an intelligent agent involves specifying each of these

- Obviously, the performance measure depends on sensors and actuators

- Actuators determine the effects that the agent has on the environment

-

#### Examples:

- Automated taxi driver

- Backgammon player

- Chess agent

- Internet shopping agent

***

### Types Of Environments

Fully Vs Partially Observable

- In a fully observable environment, an agent's sensors give it access to the complete state of the environment at all times

Deterministic Vs Stochastic/Random

- In a deterministic environment the next state is completely determined by the current state and the action executed by the agent

Episodic Vs Sequential

- In an episodic environment the agent's experience is divided into atomic "episodes". Each episode consists of the agent perceiving and then performing a single action, and the choice of action in each episode depends only on the episode itself.

Static Vs Dynamic

- A static environment is unchanged while an agent is deliberating (the environment is semi-dynamic if the environment itself does not change with the passage of time but the agent's performance score does)

Discrete Vs Continuous

- A discrete environment can be divided into clearly defined percepts and actions

Single Vs Multi-agent

- Single Agents is like solving a crossword puzzle, multi-agent is like self-driving car

-

#### Types Of Environments:

|               | Solitaire | Backgammon | Internet Shopping | Taxi |
|:------------- |:--------- |:---------- |:----------------- |:---- |
| Observable    | Yes       | Yes        | No                | No   |
| Deterministic | Yes       | No         | Partly            | No   |
| Episodic      | No        | No         | No                | No   |
| Static        | Yes       | Semi       | Semi              | No   |
| Discrete      | Yes       | Yes        | Yes               | No   |
| Single-agent  | Yes       | No         | Yes (not auction) | No   |

***

### Agent Types

**Simple Reflex Agents**

- The action to be selected only depends on the most recent percept, not a percept sequence

- As a result, these agents are stateless devices which do not have memory of past world states

-

**Model-based Reflex Agents**

- Have internal state which is used to keep track of past states of the world (percept sequences may determine action)

- Can assist an agent deal with at least some of the unobserved aspects of the current state

-

**Goal-Based Agents**

- Agent can act differently depending on what the final state should look like

- Example: automated taxi driver will act differently depending on where the passenger wants to go

-

**Utility-Based Agents**

- An agent's utility function is an internalization of the performance measure (which is external)

- Performance and utility may differ if the environment is not completely observable or deterministic

-

**Learning Agents**

- Cuts across all of the other types of agents: any kind of agent can learn

-

**Search And Knowledge Representation**

Goal-Based and utility-based agents require representation of:

- states within the environment

- actions and effects (effect of an action is transition from the current state to another state)

- goals

- utilities

Problems can often be formulated as search problem

- To satisfy a goal, agent must find a sequence of actions (a path in the state-space graph) from the starting state to the goal state

To do this efficiently, agents must have the ability to reason with their knowledge about the world and the problem domain

- Which path to follow (which action to choose from) next

- How to determine if a goal state is reached OR how decide if a satisfactory state has been reached

# Introduction To Search

**Search** is one of the most powerful approaches to problem solving in AI

Search is a universal problem solving mechanism that:

- Systematically explores the alternatives

- Finds the sequence of steps towards a solution

Problem Space Hypothesis (Allen Newwll, SOAR: An Architecture for General Intelligence)

- All goal-oriented symbolic activities occur in a problem space

- Search in a problem space is claimed to be a completely general model of intelligence

***

### Problem-Solving Agents

```
function SimpleProblemSolvingAgent(percept)

inputs: p, a percept
stati: s, and action sequence, initially empty state,
    a descriptionof current world state g,
    a goal that is initially null

state <- Update-State (state, p)
if(s is empty)
    g <- Formulate-Goal(state)
    problem <- Formulate-Problem(state, g)
    s <- Search(problem)
endif
action <- first(s)
s <- remainder(s)
return action
```

The agent follows a simple "formulate, search, execute" design

**Assumptions On Environment**

- Static: formulating and solving the problem does not take any changes into account

- Discrete: enumerating all alternative courses of action

- Deterministic: actions depend only on previous actions

- Observable: initial state is completely known

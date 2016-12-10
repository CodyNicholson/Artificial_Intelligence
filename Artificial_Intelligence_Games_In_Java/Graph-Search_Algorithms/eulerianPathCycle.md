#Eulerian Paths and Cycles

An **Eulerian Path** is a trail in a graph which visits every edge exactly once

A **trail** is a walk that does not pass over the same edge twice. A trail might visit the same vertex twice, but only if it comes and goes from a different edge each time.

A **walk** is an alternating sequence of vertices and connecting edges

A **path** is a walk that does not include any vertex twice, except that its first vertex might be the same as its last.

A **cycle** is a path that begins and ends on the same vertex

A **circuit** is a trail that begins and ends on the same vertex

An **Eulerian Cycle** is an Eulerian Trail which starts and ends on the same vertex

An udirected graph has an Eulerian Cycle if and only if every vertex has even degree

***

###Chinese Postman Problem

A postman needs to go through every street at least once on a closed circuit and wants to find the shortest path

If there is an Eulerian Cycle then that is the solution for the problem
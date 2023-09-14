<https://www.bogotobogo.com/python/python_graph_data_structures.php>



# Vertex

A vertex is the most basic part of a graph and it is also called a node. Throughout we'll call it note. A vertex may also have additional information and we'll call it as payload.

## Edge

An edge is another basic part of a graph, and it connects two vertices/ Edges may be one-way or two-way. If the edges in a graph are all one-way, the graph is a directed graph, or a digraph. The picture shown above is not a digraph.

## Weight

Edges may be weighted to show that there is a cost to go from one vertex to another. For example in a graph of roads that connect one city to another, the weight on the edge might represent the distance between the two cities or traffic status.

## Graph

A graph can be represented by $G$ where $G=(V,E)$. $V$ is a set of vertices and $E$ is a set of edges. Each edge is a tuple $(v,w)$ where $w,v \in V$. We can add a third component to the edge tuple to represent a weight. A subgraph $s$ is a set of edges $e$ and vertices $v$ such that $e \in E$ and $v \in V$.

The picture above shows a simple weighted graph and we can represent this graph as the set of six vertices

## Path

A path in a graph is a sequence of vertices that are connected by edges. We usually define a path as $w_1, w_2,..., w_n$ such that $(w_i, w_{i+1}) \in E$ for all $1 \le i \le n-1$. The unweighted path length is the number of edges in the path $(n-1)$. The weighted path length is the sum of the weights of all the edges in the path. For example in the picture above, the path from $a$ to $e$ is the sequence of vertices $(a, c, d, e)$. The edges are $\{(a, c, 9), (c, d, 11), (d, e, 6)\}$.

## Cycle

A cycle in a directed graph is a path that starts and ends at the same vertex. A graph with no cycles is called an acyclic graph. A directed graph with no cycles is called a directed acyclic graph or a DAG. 
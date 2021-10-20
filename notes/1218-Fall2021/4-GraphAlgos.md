
# Computer Science III
## CSCE 310H - Fall 2021
### Graph Algorithms

#### Introduction

* Undirected Graphs: edges between nodes (vertices) have no orientation
* Directed Graphs; edges do have an orientation, $(x, y)$ refers to an edge $x \rightarrow y$ but not necessarily the other way
* Weighted vs unweighted graphs: each edge may have a numerical "weight" associated with it (a cost or a benefit)
* Unweighted graphs are weighted graphs with uniform weights of 1
* A *path* in a graph is a sequence of connected vertices
* A *cycle* in a graph is a path that begins and ends at the same vertex
* The length of a path/cycle is the number of edges on it
* Generally we use $|V| = n$, $|E| = m$
* A graph is a tuple, $G = (V,E)$ of a vertex set $V$ and an edge set $E$
* There are many ways to represent graphs:
  * Adjacency Matrix
  * Adjacency List
  * Maps
  * Sets (of pairs of vertices)
  * Etc.
* Python: `networkx`: https://networkx.org/documentation/stable/tutorial.html
* https://pypi.org/project/network2tikz/

## Depth First Search

* Depth First Search: searches a graph as deep as possible first before backtracking
* We want tomake sure we make progress:
  - *DON'T* want to enumerate every possible path or
  - *don't* want to repeat a node/path (too much)
* Goal: explore the graph, enumerate every vertex
* Tree traversals are DFS: preorder, inorder, post order
* Strategy: go as deep into the graph as possible before backtracking
* Along the way we keep track of vital information:
  * Have you visited this vertex before?
  * Have you processed this vertex before?
  * When did you first see the vertex?
  * When did you process the vertex

## DFS Observations

* DFS *may* need to be restarted at unvisited vertices if it is a disconnected or directed graph
* DFS can produce several artifacts:
* DFS Tree/Forest:
  * Tree edges: edges you traversed when you performed the DFS
  * Back Edges: connect descendants to ancestors in the DFS tree (only possible with directed graphs)
  * Forward Edges: connect ancestors to descendants in the DFS tree (for undirected: forward/back are the same)
  * Cross Edges: can only connect between components in a DFS tree for a *directed graph*
* In an undirected graph, the presence of a back/forward edge implies the existence of a cycle
* In a directed graph: back edges are possible and indicate a *directed* cycle
* In a directed graph, all 4 types of edges are possible
* Complexity: $O(n)$ or $O(m)$ or (as a catch-all, $O(n+m)$)



```text









```

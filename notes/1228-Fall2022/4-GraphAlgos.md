
# Computer Science III
## CSCE 310H - Fall 2022
### Graph Algorithms

# Introduction

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
  * Maps: a vertex to a set of vertices
  * Sets (of pairs of vertices)
  * Etc.
* Python: `networkx`: https://networkx.org/documentation/stable/tutorial.html
* https://pypi.org/project/network2tikz/

# Depth First Search

* Depth First Search: searches a graph as deep as possible first before backtracking
* Tree traversals are DFS: preorder, inorder, post order
* We want to make sure we make progress:
  - *DON'T* want to enumerate every possible path or
  - *don't* want to repeat a node/path (too much)
* Strategy: go as deep into the graph as possible before backtracking
* Along the way we keep track of vital information:
  * Have you visited this vertex before?
  * Have you processed this vertex before?
  * When did you first see the vertex?
  * When did you process the vertex
* Used colors to indicate state:
  * White = unvisited
  * Gray = visited, but not yet processed
  * Black = processed, done

## Algorithm

* You can develop a recursive version:
  * Given the "current" node, you need to decide which node to visit next
  * Only consider unvisited ("white") nodes in the neighborhood of the current vertex, choose the next one:
    * color the current vertex gray (you've visited, but not yet processed the node)
    * Make a recursive call to the next available white node using some criteria (lexicographic, edge weights, etc.)
    * If no such unvisited vertex exists or if you have then visited them all in the neighborhood, you: process the current node (color it black, output it, etc.); hten return
* Stack-based DFS:
  * The top of the stack holds the current vertex
  * We peek at the top of the stack, look at its neighborhood:
    * among all unvisited (white) vertices, you choose the next one and push it on to the stack
    * If none, you start backtracking

## Observations

* DFS *may* need to be "restarted" at unvisited vertices if it is a *disconnected graph*: a graph with "multiple" connected components: some vertices are not reachable from any path
* DFS can produce several artifacts:
  * DFS Tree/Forest
  * Tree Edges: edges that are directly traversed in the DFS "walk"
  * Back Edges: connect a "descendent" in the DFS tree to an "ancestor"
  * Forward Edges: connect an ancestor to a descendent in the DFS Tree
  * Cross Edges: all other edges
  * Observation:
    * In an *undirected graph*: back and forward edges are the same
    * In an *undirected graph*: cross edges are not possible
  * Directed graphs may have forward and back and even cross edges due to the orientation of the edges
  * Each run of DFS may have a different ordering/tree depending on your starting point!
* DFS can be used to determine if a graph is connected, if iti is a tree (acyclic), etc.
* Complexity: $O(??)$
  * Input: graph
  * Input size: say it is $|V| = n$ ($|E| = m$ is reasonable too, but $m \in O(n^2)$)
  * Elementary operation:
    * Vertex examination/traversal
    * Edge examination/traversal
    * Processing of an actual node
  * Each node is processed exactly once: $O(n)$

## Breadth First Search

* Explores the graph by "spanning" out from a central vertex
* Explores "near" vertices first before moving out
* Observations
  * In a BFS tree for undirected graphs, no back/forward edges are possible (otherwise they would have been discovered during the BFS traversal)
  * In a directed graph, back edges are possible but forward edges are not
  * Both have potential cross edges
  * In an undirected graph, cross edges imply a cycle
  * BFS may need to be restarted if you have a disconnected graph
  * THe BFS tree can be used to determine the shortest path from the *source* (starting vertex) to any other connected vertex, but ONLY for undirected, unweighted graphs
* Analysis

  * Same: $O(n)$

## Applications

* Connectivity: given two vertices, $u, v \in V$ in a graph $G = (V, E)$: determine does there exist a path connecting $u, v$?
  * BFS or DFS: Perform either starting at $u$, if you ever encounter $v$ (enqueue or push it into your data structure): stop; answer yes. Otherwise no.
* Cycle Detection: given a graph $G$, does there exist a cycle in $G$?  
  * Or if it doesn't contain a cycle it must be a tree
  * DFS/BFS: if there are no back/forward or cross edges: it must be a tree!
  * Run DFS/BFS: if you ever encounter a visited vertex that you did not immediately come from, you found a cycle!
  * A cycle of length $\ell$? (difficult)
  * Given a particular vertex $v$, is there a cycle that involve $v$?
* Bipartite Testing

## Types of Problems

* Decision Problems = yes/no questions
* Function Problems: output a solution if one exists
* Optimization Problems: output the *best* solution
* Counting Problems: how many valid solutions exist?

```text









```

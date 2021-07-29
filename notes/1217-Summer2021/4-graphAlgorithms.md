
# Computer Science III
## CSCE 310 - Summer 2021
### Graph Algorithms

#### Introduction

* Undirected Graphs: edges have no orientation $(x, y) = (y, x)$
* Directed Graphs; edges do have an orientation, $(x, y)$ refers to an edge $x \rightarrow y$ but not necessarily the other way
* Weighted vs unweighted graphs: each edge may have a "weight" (numerical) value associated with it
* Unweighted graphs can be seen as weighted graphs with uniform weights of 1
* There are many ways to represent graphs:
  * Adjacency matrices
  * Adjecency lists
  * maps
  * Sets of pairs of vertices (set of edges)
* Recommendation: use a library; networkx is great!
* Why Graph Algorithms?

#### Depth First searches

* DFS: searches a graph as deeply as possible before "backtracking"
* We want to make sure that we make progress: we only want to visit or "process" a node at most once
* Tree traversal algorithms: preorder, postorder, inorder are all DFS variants
* Keep track of vital information:
  * Have you visited this vertex before?
  * Have you visited all of its neighbors
  * have you processed this vertex already?
  * When did you first see this vertex?
  * When did you last see it?

##### Gotchas/Misc

* DFS *may* need to be restarted at unvisited vertices if it is disconnected (or if it is directed)
* DFS can produce several other artifacts
* DFS Tree/Forest:
  * Tree Edges: edges that are traversed via the DFS traversal
  * Back Edges: edges that connect descendents in the DFS tree to an ancestor
  * Forward Edges: edges that connect an ancestor to a descendent
  * Cross Edges: connect between components of a DFS tree
* Observations:
  * In an undirected graph only tree/back edges are possible (forward are the same as back; cross edges would not exist**)
  * In an undirected graph: the presence of a back edge implies a cycle
  * Directed graph: back edges are possible and indicate a *directed* cycle
  * Directed graph: all four types of edges are possible

```text








```

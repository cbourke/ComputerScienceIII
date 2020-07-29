
# Computer Science III
## CSCE 310 - Summer 2020
### Graph Algorithms

#### Introduction

* Undirected: edges have no orientation (x, y) = (y, x)
* Directed graphs: edges have an orientation (x,y) is not the same (y,x)
* Unweighted graphs: all edges have uniform weights of 1 
* Weighted graphs: each edge may have a weight associated with it
* Many ways to implement graphs:
  * Adjacency matrices
  * Adjacency list
  * Sets of pairs of vertices (sets of edges)
* Recommendation: NetworkX https://networkx.github.io/

#### Basic Searching

* Depth First Search: searches a graph as deep as possible first before backtracking
* We want to make sure that we make progress: we don't want to visit or process a vertex more than once, and we don't want to get stuck in a loop
* Tree traversal algorithms: preorder, postorder, inorder traversals are all DFS
* Go as deep into the graph as possible, only backtracking when we hit a dead end
* Keep track of vital information:
  * Have you visited this vertex before?
  * Have you processed this vertex already?
  * When did you first see this vertex?
  * When did you last see this vertex?
  
* DFS traversal can produce several artifacts
* DFS Tree/Forest:
  * Tree Edges: edges that are traversed in the DFS traversal
  * Back Edges: connect a descendent in the DFS tree to an ancestor
  * Forward Edges: connect an ancestor in the DFS to a descendent
  * Cross Edges: connect components in a DFS forest
* Observations: 
  * In an undirected graph, only tree/back edges are possible (forward/back are the same thing)
  * In an undirected graph: the presence of a back edge implies a cycle
  * Directed: a back edge indicates a cycle, 
  * Directed: all four types of edges are possible
    
  
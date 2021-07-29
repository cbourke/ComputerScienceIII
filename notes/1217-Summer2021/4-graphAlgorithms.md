
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

#### Breadth First Search

* Explores each vertex that is "closest" to the initial vertex first
* Closest = *distance* (number of edges), not with respect to any edges weights

* Observations
  * In a BFS tree for undirected graphs, no back/forward edges are possible
  * In a BFS tree for directed graphs, back edges are possible but no forward edges are
  * With BFS the finishing/discover orders are the same due to the FIFO nature of the queue
  * Cross edges in a BFS tree connect cousins/aunts but never descednents/ancestors
  * BFS may need to be restarted if it is disconnected (undirected graphs) or it is directed and some vertices are not reachable from other vertices

#### Analysis

* Both DFS and BFS only process each node exactly once
* If your elementary operation is the "processing" of a node, and there are $n$ nodes, then both are $O(n)$
* If visiting a node or "traversing" or "examining" an edge is your elementary operation, then it becomes $O(|V| + |E|) = O(n + m)$ (recall that $m = O(n^2)$)
  * For sparse graphs $m = O(n)$ and so BFS/DFS is $O(n)$
  * For dense graphs, $m = O(n^2)$ and so BFS/DFS becomes $O(n^2)$
* Examining or traversing an edge or computing a neighborhood of a vertex may have different complexities based on the graph representation

#### Applications

* Connectivity: given two vertices $x, y \in V$ determine if there is a path between them (works for directed or undirected)
* Topological Sorting: given a poset (partially ordered set), ie a DAG = Directed Acyclic Graph: imposing a total order on the set
  * Run DFS and not the finishing times; sort them in descending order to get a total topological order out of it
* Cycle detection: Undirected: forward or back or cross edge implies a cycle
* Bipartite Testing: given a graph $G$ is it bipartite or not
* Condensation Graph: it "collapses" a large complex graph into its *strongly connected components*
  * Two vertices are *strongly connected* in a directed graph $G$ if there is a directed path from $x$ to $y$ *and* from $y$ to $x$
  * A strongly connected component is a subset of vertices that are each strongly connected to each other 






```text








```

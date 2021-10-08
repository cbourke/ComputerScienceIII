
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

#### Depth First Search

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

#### Breadth First Search

* Alternative: explore the "closest" vertices first
* Closest = *distance*, not necessarily *weighted distance*

* Observations
  * In a BFS Tree, no back/forward edges are possible in an undirected graph
  * In a BFS Tree, forward edges are not possible, but back edges are in a directed graph
  * With BFS, the finishing/starting time stamps have the exact same order (FIFO)
  * Cross edges in a BFS connect cousins/aunts, etc.  They do NOT connect descendents/ancestors
  * A BFS tree identifies a shortest path *from the initial vertex* to any other connected vertex in an unweighted graph: BFS is a single source shortest path algorithm

#### Applications

* Connectivity: Given two vertices $x, y \in V$, determine if there is a path from $x$ to $y$ (directed, undirected, etc.)
* Topological Sorting: given a poset (partially ordered set), output a consistent total order
  * Run DFS and note the finishing times
  * Sort the elements in descending order according to the finishing time stamps
  * The resulting order is a total order consistent with the poset  
* Cycle detection: detect a cycle by finding forward/back or cross edges (undirected graphs)
* Bipartite Testing: given a graph $G$ is it bipartite
* Condensation graphs: often you want to *simplify* a graph topology
  * You can take an arbitrary digraph (directed graph) possibly with cycles and *collapse* it into an "equivalent" graph without cycles
  * Collapses *strongly connected vertices*: there is a path from $x$ to $y$ AND a path from $y$ to $x$
  * The result is a DAG: Directed Acyclic Graph that preserves connectivity
    * Run DFS once, keeping track of the finish times
    * Reverse the graph (transpose graph) and run DFS on it
    * Each time the second DFS restarts, you start a new Strongly Connected Component
    * You can add edges based on connectivity in the original graph

## Minimum Spanning Trees

* Given an undirected weighted graph (edges have weights), we want to create a
*spanning tree* of minimal total weight
* A spanning tree is simply a tree that connects all of the vertices into one graph
* If your graph is disconnected, there is no spanning tree, but you *can* create a spanning forest
* In general, there may be many minimum spanning trees

### Kruskal's Algorithm

* Greedy: we'll consider the least weighted edges first, we'll include the edge if and only if it does not *induce* a cycle
* Outline:
  * Presort all the edges in non-decreasing order
  * You add the edge to the MST $T$ if and only if it does not create a cycle
  * You stop after you have added $n-1$ edges OR you run out of edges to consider

### Prim's Algorithm

* We don't do cycle detection
* Instead, we iteratively build a tree starting at an arbitrary vertex
* Throughout the algorithm we build a "frontier" of "fringe" vertices/edges
* We expand the tree, adding a "fringe" vertex on each iteration


### Shortest Distance Algorithms: Dijkstra's

* Start at a *source* vertex $s4
* Produces a shortest-path from $s$ to all other vertices
* Works on directed or undirected graphs with edge weights
* It updates a list of triples: vertex, distance to the vertex (from $s$) and the *predecessor* or how to get there
* It uses a min-heap/priority queue to store references to the vertices
* BUT: when using the min-heap, you need the ability to update the priority/weight

### Shortest Distance Algorithm: Floyd-Warshall Algorithm

*

```text











```

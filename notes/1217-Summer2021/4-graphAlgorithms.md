
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

## Minimum Spanning Trees

* Given an undirected (connected) weighted graph (edges have weights) we want to create a *spanning tree* of minimal total weight
* A spanning tree is simply a tree (subset of edges with the same vertices) that "spans" the vertices: all vertices are connected
* You can perform a MST algorithm on a disconnected graph, it would just give you a forest
* In general there are many equivalent spanning trees

### Kruskal's Algorithm

* Greedy Algorithm: it makes *locally optimal choices* which lead to a *globally* optimal solution
* Basic idea: you consider edges in increasing order of weight, adding them to your tree/forest as long as they do not induce a cycle
* If you naively use BFS/DFS to detect cycles, you'll get $O(n^3)$ in the worst case
* If instead, you use an alternative data structure, *disjoint set*, then you can get it down to $O(m\log{n})$
* Kruskal's Correctness: proof by contradiction

#### Disjoint Set Datastructure

* Purpose: maintains a disjoint set of elements and ultimately combines them all (as a union)
* Sets are represented as trees; BUT: there may be an arbitrary number of children and we only maintain references to the *parent* node
* Each set is identified with a *representative*: the root of the tree

* Operations
  * Initialize(u): creates a single node "tree" where
    * $u$ is the representative
    * $u$ is checked to make sure it is not part of any other tree
    * We will also maintain a reference to each node to provide random access
  * Find-Set(u): returns the *representative* of the set containing $u$  
  * SameSet(u, v): returns true if both $u$ and $v$ are in the same set; ie if they have the same representative: two calls to Find-Set
  * Union(u, v): combines the set containing $u$ and the set containing $v$ into one new set
  * Essential details:
    - WHen unioning two sets we always attach the smaller (shallower) of two trees to the larger
    - Optimization step: every operation that traverses up the tree will also collapse it at the same time
  * The efficiency depends on the height of the trees; at most the height is $O(\log{n})$
  * Overall, the *amortized* cost of searching, combining, etc. is $O(n)$

## Prim's Algorithm

* Works by starting at a vertex and "buidling" the tree outward
* Vertices are separated into three sets: a tree set (tree we've formed so far), a "fringe" set of vertices that are connected to a tree vertex, "unseend" vertices: those that are not yet connected to the tree
* Consider edges on the "fringe" (or the frontier): among all of these edges, choose the minimum, update the sets and continue until all vertices are in the tree set

* Efficiency
  * Updating the priority of a single element in the heap: $O(\log{n})$ and is possible if we maintain random "free" access to each node in the heap
  * Initialization: trivial, put the first vertex at index 0, all other vertices in the heap have equal priority and don't need to be sorted or inserted
  * Each operation of getMin and updatePriority is $O(\log{n})$
  * getMin is called $n$ times, updatePriority is called once for each edge, (technically each vertex is examined a second time but no update occurs) so overall $m$ times
  * In total we have:
    $$n\log{n} + m\log{n} = O(m\log{n})$$

## Shortest Distance Algorithms

## Dijkstra's

* Single-source shortest path algorithm
* It will produce a shortest path to all other vertices from a single *source* vertex $s$
* Essentially the same algorithm as Prim's but with different criteria
* We keep track of a triple: vertex, the distance to the vertex (shortest one so far) and the *predecessor* vertex (so we can rebuild the shortest distance path)

## Floyd-Warshall Algorithm

* A dynamic programming algorithm
* It produces the path/distance for *all pairs*
* It keeps track of two matrices: one for the minimum weighted distance and one for the "successor" vertex 


```text








```

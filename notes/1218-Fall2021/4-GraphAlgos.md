
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

#### Breadth First Search

* Explores each vertex that is "closest" to the initial vertex first
* Closest = *distance* (number of edges), not with respect to any edges weights

* Observations
  * In a BFS tree for undirected graphs, no back/forward edges are possible
  * In a directed graph, back edges are possible, but forward edges are not
  * Both have potential cross edges: edges that connect vertices in the BFS tree that are not ancestors or descendants
  * BFS may need to be restarted if it is a disconnected graph or if it is a directed graph such that some vertices are reachable but others are not
  * Cross edges in a BFS tree connect cousins/aunts but never descednents/ancestors

* Analysis

* Elementary operations:
  * Processing a vertex (likely the most expensive): $n = O(n)$
  * Traversing an edge ($2m = O(m)$)
  * Examining a vertex (black/gray/white): $2m = O(m)$
  * Overall if you want to capture all work: $O(n + m)$

## Applications

### Connectivity

* Given a graph $G=(V,E)$ and (say) two vertices, $x, y \in V$ determine if $x$ and $y$ are "connected"
  * Does there exist a (undirected/directed) path from $x$ to $y$?
  $$p : x \rightsquigarrow y $$
  * Problems that are posed such that there is a yes/no answer (true/false, 1/0, etc.) are *decision versions*
  * Problems that require the output of an actual solution are *functional versions*: it maps your input to an output that is a "witness" or "certificate" to the yes/no question
  * Given $G, x, y$: if there is a path from $x$ to $y$ output it, if not, output some flag value
  * Problems that require not only a solution, but the *best* solution are *optimization versions*
  * shortest path or the longest path or the least weighted path or the most weighted path
  * What you are trying to optimize is an "objective function"
  * *counting versions*: how many paths exist between those vertices
* Potential Solutions (undirected)
  * Run DFS: Start at $x$, if you ever see $y$, stop answer yes
  * If DFS has to restart to discover $y$, the answer is no
  * BFS: same criteria
* Potential Solutions (directed)
  * Run DFS starting at $x$, if you ever encounter $y$ without starting over: yes

#### Cycle Detection

* Given a graph $G$, does it contain a cycle or not (ie is it acyclic, ie a tree)
  * Run DFS: if you ever encounter a gray vertex: implies a back edge (undirected) implies a cycle
  * Run BFS: if you ever encounter a gray vertex: implies a cross edge, implies a cycle
  * Directed: 1) does there exist a path $x \rightsquigarrow y$ AND does there exist a path $y \rightsquigarrow x$: if yes then there is a directed cycle: $O(n^2(n+m))$

#### Bipartite Testing

* A graph $G$ is bipartite if its vertices can be partitioned into two sets $L, R$ such that edges only connect between the two sets
* Given a graph $G$, is it bipartite or not?
* Obsevation: $G$ is bipartite iff $G$ contains no odd length cycles
* Perform a DFS and keep track of alternating colors: red/blue; if a red vertex is adjacent to a red vertex (or a blue to a blue), NOT bipartite
* Condensation Graph
  * A lot of graph "equivalencies": isomorphisms, homomorphisms, homeomorphisms, etc.
  * Goal: take a "large" directed graph and "condense" it into a smaller graph, but preserving connectivity
  * Let $G$ be a directed graph; let $x, y$ be vertices in $G$.  We say that $x, y$ are strongly connected if there exists path from $x$ to $y$ AND from $y$ to $x$
  * A condensation graph collapses a large complex graph into its strongly connected components
  * A component is a subset of vertices each of which is pairwise strongly connected
  * You start with a directed graph:
    1. Perform a DFS noting the finish times
    2. You compute the *transpose* graph (you simply reverse the edge orientation)
    3. You perform another DFS in order of finish time; each time you start over you create a new node (this indicates a strongly connected component)
  * Result: a DAG = Directed Acyclic Graph
  * Removes a lot of "redundant" information

## Minimum Spanning Tree

* Given an undirected (connected) weighted graph (edges have weights) we want to create a *spanning tree* of minimal total weight
* A spanning tree is simply a tree (subset of edges with the same vertices) that "spans" all the vertices: all vertices are connected by some path
* Many spanning trees may exist, you want to find the "best" (minimally weighted) one
* There may be more than one!

### Kruskal's Algorithm

* Greedy Algorithm: it makes *locally optimal choices* which lead to a *globally* optimal solution
* Basic idea: you consider edges in increasing order of weight, adding them to your tree/forest as long as they do not induce a cycle

#### Disjoint Set Data Structure

* Purpose: we maintain a collection of *disjoint* sets of elements, then eventually we *combine* or Union them all together
* Sets are represented as trees; BUT: there may be an arbitrary number of children and we only maintain references to the *parent* node
* Each set is identified with a *representative*: the root of the tree

**Operations**

* Initialize(u): creates a single node "tree" where
  * $u$ is the representative
  * $u$ is checked to make sure it is not part of any other tree
  * We will also maintain a reference to each node to provide random access
* Find-Set(u): returns the *representative* of the set containing $u$  
* SameSet(u, v): returns true if both $u$ and $v$ are in the same set; ie if they have the same representative: two calls to Find-Set
* Union(u, v): combines the set containing $u$ and the set containing $v$ into one new set
  * Essential details:
    - When union-ing two sets we always attach the smaller (shallower) of two trees to the larger
    - Optimization step: every operation that traverses up the tree will also collapse it at the same time
* The efficiency depends on the height of the trees; at most the height is $O(\log{n})$
* Overall, the *amortized* cost of searching, combining, etc. is $O(n)$

## Prim's Algorithm

* Works by starting at a vertex and "building" a connected tree outward
* Vertices are separated into three sets:
  * Tree vertices: vertices that have been added to the "intermediate" MST
  * Fringe vertices: vertices that have been "seen" (ie are connected to tree vertices)
  * Unseen vertices: vertices that are not connected to the tree yet
* Consider vertices on the the "fringe": which one do you add next?

```text









```

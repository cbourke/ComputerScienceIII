
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
* Types of Problems
  * Decision Problems = yes/no questions
  * Function Problems: output a solution if one exists
  * Optimization Problems: output the *best* solution
  * Counting Problems: how many valid solutions exist?
* Bipartite Testing
  * A graph $G$ is bipartite if its vertices can be partitioned into two sets $L, R$ such that edges only connect between the two sets
  * Given a graph $G$, is it bipartite or not?
  * Observation: $G$ is bipartite iff $G$ contains no odd length cycles
  * Pseudocode

### Condensation Graphs

* A morphism is a mapping from one graph to another graph such that the mapping *preserves* some structure
* A homomorphism is a mapping from one graph to another graph that preserves connectivity (edge connectivity)
* Goal: take a directed graph and *simplify* it to its core connectivity
* Two vertices in a digraph (directed graph) are *strongly connected* if there is a directed path from one to the other and vice versa
* Create a "smaller" condensation graph of a directed graph: smaller graph that preserves *strongly connected compontents*
* You start with a directed graph:
  1. Perform a DFS noting the finish times
  2. You compute the *transpose* graph (you simply reverse the edge orientation)
  3. You perform another DFS in order of finish time; each time you start over you create a new node (this indicates a strongly connected component)

## Minimum Spanning Trees

* Given an undirected weighted (connected) graph (edges have weights), you want to create a *spanning tree* of minimum total weight
* A spanning tree is a tree (same vertex set, subset of edges) that leave the graph still connected but acyclic
* Many spanning trees may exist, but you want to find the "best" one: the one of minimum weight
* even then, there may be more than one MST
* Note: if you have a disconnected graph, it is still possible to compute a Minimum Spanning Forest

### Kruskal's Algorithm

* Greedy Algorithm: it makes *locally optimal choices* which lead to a *globally* optimal solution
* Basic Idea: you consider edges in increasing order of weight; add them if adding them would not *induce a cycle* (create a cycle); otherwise you don't add them
* Problem: the naive implementation gives a $O(m) \cdot O(m + n) = O(n^4)$ worst case running time
* Observation: DFS is performed on a *sparse graph*
* A sparse graph means you don't have many edges, $m = O(n)$
* so DFS = $O(n + n) = O(n)$; still $O(n^3)$ overall
* Another, potentially better way is to not do cycle detection: use a smart data structure!

#### Disjoint Set Data Structure

* Purpose: we maintain a collection of *disjoint* sets of elements, then eventually we *combine* or Union them all together
* Sets are represented as trees; BUT: there may be an arbitrary number of children and we only maintain references to the *parent* NOT the children
* Each set is identified with a *representative*: the root of the tree

**Operations**

* Initialize(u): creates a single node "tree" where
  * $u$ is the representative
  * $u$ is checked to make sure it is not part of any other tree already
  * We will maintain random access to each node so we can "jump" to the node in any particular
* Find-Set(u): returns the *representative* of the set containing $u$  
* SameSet(u, v): returns true if both $u$ and $v$ are in the same set; ie if they have the same representative: two calls to Find-Set
* Union(u, v): combines the set containing $u$ and the set containing $v$ into one new set
* Essential details:
  - When union-ing two sets we always attach the smaller (shallower) of two trees to the larger
  - Optimization step: every operation that traverses up the tree will also collapse it at the same time
* The efficiency depends on the height of the trees; at most the height is $O(\log{n})$
* The overall (amortized) cost of starting with $n$ disjoint sets and union-ing them until you have one set is $O(n)$

## Prim's Algorithm

* Works by starting at a single vertex and "building" a connected tree outward
* Vertices are separated into three sets:
  * Tree vertices: vertices that have been added to the "intermediate" MST
  * Fringe vertices: vertices that have been "seen" (ie are connected to tree vertices)
  * Unseen vertices: vertices that are not connected to the tree yet
* Consider vertices on the the "fringe": which one do you add next?

### Efficiency

* We store triples of vertices and their weights so at most $n$ elements are ever stored in the heap
* Updating the priority of a single element (assuming you have random access to it) in a heap is at most $O(\log{n})$
* THe number of iterations: $n$
* BUT: you also update the priority for *every* edge overall, $O(m)$
* In total you have $O(m\log{n})$ operations


```python3
import random

class PriorityQueue:
    """
    A priority queue/min heap implementation that supports
    additional features over the standard python heaq
    implementation.

    Items need to be hashable, priorities must be comparable
    but generally should be numerical.
    """

    def __init__(self):
        self.itemToIndex = {}
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0

    def enqueue(self, item, priority):
        self.arr.append( (item, priority) )
        currIndex = len(self.arr) - 1
        while currIndex > 0 and self.arr[currIndex][1] < self.arr[ currIndex//2 ][1]:
            self.arr[currIndex], self.arr[ currIndex//2 ] = self.arr[ currIndex//2 ], self.arr[currIndex]
            self.itemToIndex[ self.arr[currIndex][0] ] = currIndex
            currIndex = currIndex // 2
        self.itemToIndex[item] = currIndex

    def dequeue(self):
        (item, priority) = self.arr[0]
        self.itemToIndex.pop(item)
        #x is the last item
        (x,p) = self.arr.pop()
        if not self.arr:
          # queue is now empty
          return (item, priority)
        self.arr[0] = (x,p)
        self.itemToIndex[x] = 0
        currIndex = 0
        while True:
          if currIndex >= len(self.arr):
            break
          # 0-index based:
          # i -> 2(i+1) - 1 (left)
          # i -> 2(i+1)     (right)
          leftIndex  = 2 * (currIndex+1) - 1
          rightIndex = 2 * (currIndex+1)
          swapIndex = currIndex
          if leftIndex < len(self.arr) and self.arr[swapIndex][1] > self.arr[leftIndex][1]:
            swapIndex = leftIndex
          if rightIndex < len(self.arr) and self.arr[swapIndex][1] > self.arr[rightIndex][1]:
            swapIndex = rightIndex
          if swapIndex == currIndex:
            break #no children or both are greater
          self.arr[swapIndex], self.arr[currIndex] = self.arr[currIndex], self.arr[swapIndex]
          self.itemToIndex[self.arr[swapIndex][0]] = swapIndex
          self.itemToIndex[self.arr[currIndex][0]] = currIndex
          currIndex = swapIndex
        return (item, priority)

    def updatePriority(self, item, newPriority):
        if item not in self.itemToIndex:
            return
        itemIndex = self.itemToIndex[item]
        self.arr[itemIndex] = (item, newPriority)
        # go up
        currIndex = itemIndex
        while currIndex > 0 and self.arr[currIndex][1] < self.arr[ currIndex//2 ][1]:
            self.arr[currIndex], self.arr[ currIndex//2 ] = self.arr[ currIndex//2 ], self.arr[currIndex]
            self.itemToIndex[ self.arr[currIndex][0] ] = currIndex
            currIndex = currIndex // 2
        self.itemToIndex[item] = currIndex
        # go down
        while True:
          if currIndex >= len(self.arr):
            break
          # 0-index based:
          # i -> 2(i+1) - 1 (left)
          # i -> 2(i+1)     (right)
          leftIndex  = 2 * (currIndex+1) - 1
          rightIndex = 2 * (currIndex+1)
          swapIndex = currIndex
          if leftIndex < len(self.arr) and self.arr[swapIndex][1] > self.arr[leftIndex][1]:
            swapIndex = leftIndex
          if rightIndex < len(self.arr) and self.arr[swapIndex][1] > self.arr[rightIndex][1]:
            swapIndex = rightIndex
          if swapIndex == currIndex:
            break #no children or both are greater
          self.arr[swapIndex], self.arr[currIndex] = self.arr[currIndex], self.arr[swapIndex]
          self.itemToIndex[self.arr[swapIndex][0]] = swapIndex
          self.itemToIndex[self.arr[currIndex][0]] = currIndex
          currIndex = swapIndex

    def __str__(self):
        return str(self.arr) + "\n" + str(self.itemToIndex)


h = PriorityQueue()
for p in range(26):
    h.enqueue(chr(p+65), random.randint(0, 100))
for p in range(26):
    h.updatePriority(chr(p+65), random.randint(0, 100))
for p in range(26):
    h.updatePriority(chr(p+65), random.randint(0, 100))
for p in range(26):
    h.updatePriority(chr(p+65), random.randint(0, 100))
while not h.isEmpty():
    x = h.dequeue()
    print("x = ",x)

```

```text









```



Reductions

* Goal: want to establish the relative complexity of problems
* Relative complexity of algorithms can be done easily with Big-O analysis
  * Quicksort is better than Selection Sort
  * Coming up with algorithms is hard, how do we know that no such algorithms exist?  
* Doing this for problems means we need another framework
* In general: if you can use/adapt a (supposed) solution for problem $B$
to solve another problem $A$, then:
  * $A$ is no more complex than $B$
  * $B$ is just as complex as $A$ (and may be more complex)
  * $A$ *reduces* to $B$
* Reduction:
  * NOT as in making smaller or simpler
  * Intuitively you are reducing an "easier" problem to a "harder"
  * In this sense: you are reducing the problem of solving a problem to solving another problem: "I don't know how to solve $A$, but if I 
  could solve $B$ I could solve $A$, so I've reduced the problem of
  solving $A$ to the problem of solving $B$"

- Mapping Reductions
- NPC definition
- 5 step process
- SAT
- SAT -> clique

 def isConnected(G, x, y):
 """Determines if there is a path in the graph G connecting vertices x and y.
   Args:
       G: an undirected graph
       x: the first vertex
       y: the second vertex
   Returns:
       True if a path exists between vertices x and
       y in the graph G, false otherwise
 """


 def shortestPathLength(G, x, y):
 """Determines the length of the shortest path between vertices x and y in the graph G.
   Args:
       G: an undirected graph
       x: the first vertex
       y: the second vertex
 Returns:
 An integer representing the length (number of edges) of the shortest path between x and y. Zero is returned if x = y and -1 if no such path exists.
 """


 def shortestPath(G, x, y):
 """Computes the the shortest path between vertices xandyinthegraphG.
   Args:
       G: an undirected graph
       x: the first vertex
       y: the second vertex
 Returns:
 A list representing the sequence of vertices in
 the shortest path between x and y. None is returned if no such path exists.
 """

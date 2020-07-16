
# Computer Science III
## CSCE 310 - Summer 2020
### Brute Force Algorithms

* You design a straightforward "just get it done" approach
* "Obvious" but "Naive" (inefficient)
* Often such solutions are not practical on even moderately large data
* Often such approaches require generating combinatorial objects
  * Combinations: given a set of $n$ unique elements, you want to generate an unordered subset of size $k$ (or all such
    subsets of size $k$)
  * Permutations: given a set of $n$ unique elements, you want to generate an *ordered* sequence of all $n$ elements
  
### Generating Combinations

* Given a set of $n$ elements: ${1, 2, 3, \ldots, n}$
* Outline:
  * Start with ${1, 2, \ldots, k}$
  * Assume that you have elements $a_1, a_2, \ldots, a_k$
  * Want to generate the next combination
  * Locate the last element $a_i$ such that
    $$a_i \neq n - k + i$$
  * Replace $a_i$ with $a_i + 1$
  * Replace each $a_j$ with $a_i + j - i$
    for $j = i+1, i+2, \ldots, k$
  
### Generate Permutations

* Start with permutations $1234\ldots n$
* Given the current permutation $a_1, a_2, \ldots, a_n$
* Find the right-most (last) pair, $a_i, a_{i+1}$ such that $a_i < a_{i+1}$
* Find the smallest element to the right ("tail") larger than $a_i$, call it $a'$
  * swap $a'$ and $a_i$
  * sort (order) the elements to the right of the swapped $a'$
  
## Backtracking

* Generating combinatorial objects is "blind" problem solving
* We often *need* to take the *structure* of the problem into account
* WE like structure: it can be exploited
* Brute force algorithms: we may not even need to consider a large proportion of possible solutions (don't need to generate every single combination/permutation)
* General technique: backtracking
  * Iteratively (recursively) build a (partial) solution until it becomes infeasible in which case you *backtrack* 
  * Wondering around a maze
  * Playing games: chess: look ahead to possible solutions and ignore any losing moves
   
### Satisfiability

* Satisfiability:
* Given: a *predicate* $P(x_1, x_2, \ldots, x_n)$
* Determine (output true or false) if $P$ is *satisfiable*    
  $$\exists x_1, x_2, \ldots, x_n [P(x_1, x_2, \ldots, x_n) = 1]$$  
* Naive brute force approach: generate all $2^n$ possible bit strings of length $n$ (permutations with repetition over $\{0, 1\}$)
* Better solution: build partial solutions to a predicate

### Hamiltonian Path/Cycle

* Recall that undirected graphs are represented by a set of vertices $V = \{v_1, v_2, \ldots, v_n\}$ and a set of edges $E$ (undirected pairs of vertices), 
* $(u, v) \in E$ means that $u$ and $v$ are connected by an unoriented edge
* Definition: given a vertex $v$, the *neighborhood* of $v$, denoted $N(v)$ is the set of vertices connected to it by a single edge
* A *Hamiltonian path* (or cycle) in a graph $G$ is a (simple) path that visits every vertex exactly once
* Variations:
  * Yes/No (decision version): determine whether or not a given graph $G$ has a Hamiltonian path or not
  * Function version: if $G$ does have a Hamiltonian path, output at least one (if not, then output $\phi$)
  * Counting version: how many Hamiltonian paths does $G$ have?
  * Optimization version: for a weighted graph, output a Hamiltonian path of least weight
* Naive solution: generating combinatorial objects
  * generate all permutations of vertices ($n!$)
  * check if each one represents a valid Hamiltonian path
* Bad because it ignores missing edges: if the edge $(x, y)$ is not present, no permutation with vertices $xy$ nor $yx$ need to be considered
* Backtracking solution: recursively build permutations by exploring the graph (essentially DFS but with repeatedly revisiting vertices)
  * Only valid paths are explored
  * Still may be exponential, but at least it is not "blind"

### Clique Problem

* Given a graph $G = (V, E)$ a *clique* is a subset of vertices $C \subseteq V$ such that every vertex in $C$ is connected to every other vertex in $C$
* $C$ is a *complete subgraph*
* MOtivation: social networks, biology, dependency analysis, finding "dense" sub network: lots of redundancy 
* Clique problem:
  * Decision version: given $G$ and an integer $k$: does there exist a clique of size $k$?
  * Optimization problem: given $G$, what is the size of the maximal clique 
  * Functional version: output the maximal clique (at least one or maybe all of them)
* Naive combinatorial approach: generate every possible subset!
* Better approach: build partial solutions as long as they represent a clique
  * if adding a vertex $x$ does not result in a clique, prune any further recursive calls!

### 0-1 Knapsack Problem

* Given:
  * A collection of items $A = \{a_1, \ldots, a_n\}$
  * Each item has a *weight* $w_i$
  * Each item has a *value* $v_i$
  * Our knapsack has a maximum capacity of $K$
  * We want to take items such that the total (sum) value of all the items is maximized, BUT subject to our weight constraint
* Greedy approach will NOT work (may not give the optimal solution)
* There are other variations that are easily solved: fractional knapsack
* Naive combinatorial apporach: generate all subsets
  * Verify that the subset is valid (weight constraint $K$ is not exceeded)
  * Update the maximum value'd knapsack
* Backtracking approach: you don't consider infeasible solutions: any subset that exceeds the weight of the capacity $K$

### Closest Pair of Points
  * Brute force even though it was "only" $O(n^2)$
  * Naive combinatorial approach: generate all pairs
  * Can we exploit the nature of the problem to avoid some pairs?
  * Like a graph, but all edges are present so we can't immediately discount them
  * Unlike Ham Path/Clique/Knapsack: we cannot simply ignore some pairs
  * Need a different approach: exploit geometry
  * CS = Mathematics
   
```text











```
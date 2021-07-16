
# Computer Science III
## CSCE 310 - Summer 2021
### Brute Force Algorithms

* In general not a great solution; not really efficient
* You generate or examine every possible solution to find *a* solution or the *best* solution to a problem
* Often creating a brute force solution helps you to understand the problem and look for *structure* to exploit
* Often such approaches require generating combinatorial objects
* Example: finding the closet pair (generating combinations of size 2 = generating subsets of size 2 of a set of size *n*)

## Generating combinations

* Given a set of $n$ elements: {1, 2, 3, 4, ..., n}
* Outline:
  * Start with {1, 2, 3, ..., k}
  * Assume that you have elements a_1, a_2, ... a_k
  * Want to generate the next *k* combinations
  * Locate the last element a_i
  such that a_i != n - k + i
  * Replace a_i with a_i + 1
  * replace each a_j with a_i + j - i for all j: i+1 ... k

## 0-1 Knapsack Problem

  * Given:
    * A collection of items $A = \{a_1, \ldots, a_n\}$
    * Each item has a *weight* $w_i$
    * Each item has a *value* $v_i$
    * Our knapsack has a maximum capacity of $K$
    * We want to take items such that the total (sum) value of all the items is maximized, BUT subject to our weight constraint
  * Greedy approach will NOT work (may not give the optimal solution)
  * Generating all possible subsets and taking the best solution among all feasible solutions is possible

## Backtracking

* Generating combinatorial objects is "blind" problem solving
* We often need to take *structure* of the problem into account
* We like structure: it can be exploited for more efficient solutions
* You may not need to consider a large proportion of possible solutions
* General technique of backtracking:
  * You iteratively (recursively) build a partial solution until it becomes infeasible in which case you *backtrack* to a previous partial solution
  * Walking a maze: once you hit a dead end, you backtrack
  * Chess: computer or 'AI' players will "look ahead" to a huge portion of possible moves and choose the best path

### Hamiltonian Path/Cycle

* A Hamiltonian path (or cycle) is a simple path (cycle) in a graph that visits every vertex exactly once
* Recall that undirected graphs are represented by a set of vertices $V = \{v_1, v_2, \ldots, v_n\}$ and a set of edges $E$ (undirected pairs of vertices),
* $(u, v) \in E$ means that $u$ and $v$ are connected by an unoriented edge
* Definition: given a vertex $v$, the *neighborhood* of $v$, denoted $N(v)$ is the set of vertices connected to it by a single edge
* Variations:
  * Decision version: yes or no question: does a solution exist at all
  * Functional version: given a problem, if a solution exists, output it
  * Optimization problems: among all feasible solutions, output the best one
  * Counting Problem: *how many* solutions exist?
Naive solution: generate Permutations

## Generating permutations

* You start with the identity permutation: $1234...n$
* Given the current permutation, $a_1, a_2, \ldots, a_n$, we want to find the *next* permutation
* Find the right-most (last) pair of elements, $a_i, a_{i+1}$ such that $a_i < a_{i+1}$
* Find the smallest element to the right ("tail") larger than $a_i$, call it $a'$
  * swap $a'$ and $a_i$
  * sort (order) the elements to the right of $a'$

## More Combinatorial Objects

* You can also generate general $k$-permutations
* Generating permutations with repetition (binary strings, DNA sequences, etc.)

## More Problems

### Clique

* Given a graph $G = (V,E)$ a *clique* is a subset of vertices $C \subseteq V$ such that every vertex in $C$ is connected
* $C$ is a *complete subgraph*
* Motivation: social networks, biology, dependency analysis, finding "dense" sub networks, a lot of redundancy
* Clique problem: given a graph and an integer $k$, does the graph contain a clique of size $k$?
* Optimization: given a graph, find the size of the largest clique
* Naive approach: generate all possible subsets, verify that a subset is a clique, take the largest clique
* Slightly better approach: take the graph connectivity into account: if you build a subset that is not a clique, then do not consider any further superset (backtrack if that is the case)

### Satisfiability

* Recall that a predicate is a logical statement on $n$ boolean variables
  $$P(\vec{x}) = P(x_1, x_2, \ldots, x_n)$$
* Examples...
* SAT: given a predicate on $n$ variables, does there exist an assignment of those variables (true or false) such that the predicate evaluates to true
* This problem is equivalent to determining if the quantified statement,
$$\exists x_1, x_2, \ldots x_n P(\vec{x})$$
* Naive approach: generate the truth table and evaluate it on all possible truth assignments
  * You generate all possible bit strings of length $n$
  * Generate all permutations with repetition (count)
* Better approach: generate *partial* assignments, if the assignment of a value to a variable makes the entire predicate false, backtrack

```c









```

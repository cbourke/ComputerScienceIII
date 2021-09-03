
# Computer Science III
## CSCE 310 - Fall 2021
### Brute Force Algorithms

# Motivating Example

* Given a set of points $\{(x_1, y_1), \ldots, (x_n, y_n)\}$ in
the Euclidean plane, determine which pair is the closest

# Introduction

* Brute Force style algorithms simply try every single possibility:
  * You find the *best* solution (optimization problems)
  * You need to examine every possible solution to determine if they are valid/feasible (decision problems)
  * You need to create a solution (functional problems)
* In general brute forcing is not ideal, not efficient, not feasible
* Often creating a brute force algorithm means generating combinatorial objects
* Example: we generated pairs or combinations of 2 from a set of $n$ elements

## Generating Combinations

* Given a set of $n$ elements, $\{1, 2, 3, \ldots, n\}$
* Outline:
  * Start with $\{1, 2, 3, \ldots, k\}$
  * Assume that you have a "current" combination, $a_1, a_2, \ldots, a_k$
  * Want to generate the *next* $k$ combination
  * Locate the last element $a_i$ such that $a_i \neq n -k + i$
  * Replace $a_i$ with $a_i + 1$
  * Replace each $a_j$ with $a_i + j - i$ for all $j = i+1, i+2, ... k$

## Generating Permutations

* Given a set of $n$ elements, $\{1, 2, 3, \ldots, n\}$ we want to
generate all possible *permutations*
* Permutation review
  * An ordered arrangment of elements
  * In general there are $n!$ possible permutations of $n$ elements
* Given a current permutation, $a_1, a_2, \ldots, a_n$ we want to find the *next* permutation:
  * Find the right-most (last) pair of elements $a_i, a_{i+1}$ such that $a_i < a_{i+1}$
  * Find the smallest element to the right of $a_i$ (the "tail" of the permutation) larger than $a_i$ call it $a'$
    * Swap $a'$ and $a_i$
    * Sort (order) the elemnts to the right of $a'$

## Problems

### Hamiltonian Path Problem

* Given an undirected graph $G = (V, E)$ (with vertices $V = \{v_1, v_2, \ldots, v_n\}$ and edges $E$) determine if there is a *Hamiltonian Path* or not
  * A Hamiltonian Path is a path in a graph that traverses every vertex exactly once
* Brute Force (combinatorial) solution:
  * generate every permutation of every vertex and check if it is a Hamiltonian Path

## Backtracking

* Generating combinatorial objects is "blind" problem solving
* Often we need or it is better to take the *structure* of the problem or the input into account
* We like structure: structure can be exploited
* Generally brute force "backtracking" is not necessarily better asymptotically
* But in practice it can save a lot of work and make "exponential" algorithms more feasible
* General technique:
  * You iteratively (recursively) build a partial solution until you reach a feasible solution or you reach a "dead end" at which point you backtrack
  * Walking a maze: you keep track of where you've been (breadcrumbs)
  * Chess: computer "AI" player will simply "look ahead" and choose the best possible move

### 0-1 Knapsack Problem

* Given:
  * A collection of items $A = \{a_1, \ldots, a_n\}$
  * Each item has a *weight* $w_i$
  * Each item has a *value* $v_i$
  * Our knapsack has a maximum capacity of $K$
  * Want to steal as much as possible subject to our weight capacity
  * Want to maximize the sum of the values of all items we take
  * BUT, the sum of all weights of items we take cannot exceed $K$
* Greedy approach is not necessarily optimal
* Attempting to max out your weight capacity is not necessarily optimal
* Combinatorial approach: generate every possible combination (subset)
  * If the sum of weights exceeds $K$ it is not a *feasible* solution
  * Among all feasible solutions, you choose the best one (maximum sum of values)
* Backtracking solution:
  * Iteratively/recursively create all possible subsets
  *

```python

import copy

count = 0

def subsetTree(set, subset, k):
  """
  set is the original set
  subset is the current subset consisting of some of
  the elements a_1 thru a_k
  k is the index of the elements

  going to make recursive calls to generate all other
  subsets
  """
  global count
  n = len(set)
  if k == n:
    return
  for j in range(k+1, n):
    #add set[j] to the subset and
    newSubset = copy.deepcopy(subset)
    newSubset.append(set[j])
    # "process" the current subset...
    print(newSubset)
    count += 1
    # recurse
    subsetTree(set, newSubset, j)
    #alternative: subset.pop()

n = 4
set = list(range(n))
subset = []
subsetTree(set, subset, -1)
print(count)
```

## Other Problems and Brute Force Solutions

* Permutations with repetition
  * Example: $\{A, G, C, T\}$
  * Generate permutations of these with repetition of length 10
  * In general, there are $4^k$ possible permutations with repetition of length $k$ of 4 elements
  * More generally:
  $$n^k$$
  possible permutations with repetition of $n$ elements of length $k$
* Set partitions?
  * Given a set $\{a, b, c\}$ how many partitions are there?
  * Partitioning is a set of all elements divided into subsets


```text




```


# Computer Science III
## CSCE 310H - Fall 2022
### Brute Force Algorithms

# Motivating Example

* Given a set of points $\{(x_1, y_1), \ldots, (x_n, y_n)\}$ in
the Euclidean plane, determine which pair is the closest

# Introduction

* Brute Force style algorithms simply try every single possibility:
  * Sometimes it is about optimization: you try every solution and then choose the *best* (optimization problems)
  * You may need to examine every possible solution to determine that there is *no* valid or feasible solution (decision problems)
  * You may need to actually find a solution (functional problem)
* In general, brute forcing is not ideal, efficient or even feasible
* BUT: a brute force solution *might* be a good approach for *small* input sizes
* Generally: it may involve generating *combinatorial objects* (pairs, triples, permutations)

## Generating Combinatorial Objects: Combinations

### Generating *All* Combinations

* Simply count in binary
* Each bit is associated with an element, 0 if a subset does not contain
  the element, 1 if it does

### Generating $k$-Combinations

* Given a set of $n$ elements, $\{0, 1, 2, 3, \ldots, n-1\}$ want to generate all possible $k$-combinations
* Outline:
  * Start with the combination $\{0, 1, 2, \ldots, k-1\}$
  * given the current combination of $a_0, a_1, a_2, \ldots, a_{k-1}$ want to generate the next one
  * Locate the last element $a_i$ such that $a_i \neq n - k + i$
  * Replace $a_i$ with $a_i + 1$
  * Replace each $a_j$ with $a_i + j - i$ for all $j = i+1, i+2, ... k$

## Generating Permutations

* Review
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

## Computational Problems

### 0-1 Knapsack Problem

* Given:
  * A collection of items $A = \{a_1, \ldots, a_n\}$
  * Each item has a weight $w_i$
  * Each item has a value $v_i$
  * Our knapsack has a maximum capacity of $K$
  * We want to maximize our total value (sum of the values of the things we take)
  * Subject to the maximum weight capacity (sum of weights of things we take cannot exceed $K$)
  * Greedy approach is not necessarily optimal
  * Attempting to max out your weight capacity is not necessarily optimal
  * Combinatorial approach: generate every possible combination (subset)
    * If the sum of weights exceeds $K$ it is not a *feasible* solution
    * Among all feasible solutions, you choose the best one (maximum sum of values)
  * Backtracking solution:
    * Iteratively/recursively create all possible subsets

### Hamiltonian Path Problem

  * Given an undirected graph $G = (V, E)$ (with vertices $V = \{v_1, v_2, \ldots, v_n\}$ and edges $E$) determine if there is a *Hamiltonian Path* or not
  * A Hamiltonian Path is a path in a graph that traverses every vertex exactly once
  * Brute Force (combinatorial) solution:
      * generate every permutation of every vertex and check if it is a Hamiltonian Path


```text








```

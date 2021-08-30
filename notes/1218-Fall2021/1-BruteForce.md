
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

```text




```

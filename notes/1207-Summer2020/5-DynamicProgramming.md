
# Computer Science III
## CSCE 310 - Summer 2020
### Dynamic Programming

## Introduction

* "Dynamic" = fancy marketing term
* Basic Idea:
  * Divide & Conquer approach to problem solving
  * Eliminate redundant recursion with memoization (caching)
  * Eliminate remaining recursions by identifying a tableau (table) and filling it out
  
### Example: computing binomials

* Consider:
  $${n \choose k}$$
* Straightforward solution:
  $${n \choose k} = \frac{n!}{(n-k)!k!}$$
* Pascal's Identity:
$${n \choose k} = {n-1 \choose k-1} + {n-1 \choose k}$$
* Base cases: 
  $${n \choose n} = 1 = {n \choose 0}$$

* Basic Steps
  * Identify a value that represents the optimal of a problem
  * Identify a recurrence identity in terms of values to "smaller" problems
    * Prove your recurrence is correct ("Optimal Substructure Property"; its just a simple application of induction)
    * Identify trivial base cases
    * Identify the desired final result
  * Setup a tableau that holds values to subsolutions (and possibly additional data to reconstruct solutions)
    * Fill in cells corresponding to the trivial base cases
    * Identify the cell corresponding to the final result
  * Identify how cells relate to each other
  * Fill out cells in the table in an order so that needed values are cached 
  
## Problem: Optimal Binary Search Trees

* Given a set of keys and probabilities of searching for those keys...
* We want to build a binary search tree that minimizes the average number of key comparisons

## Problem: Dynamic 0-1 Knapsack

* Given a collection of items with weights and values and a capacity $W$, we want to maximize our total value subject to the capacity
* Steal as much stuff as we can carry (maximize value)

  
```text











```
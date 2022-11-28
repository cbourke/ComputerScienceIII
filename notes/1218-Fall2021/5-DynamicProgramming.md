
# Computer Science III
## CSCE 310H - Fall 2021
### Dynamic Programming

## Introduction

* "Dynamic" = fancy marketing term
* Basic Idea
  * Divide & Conquer approach to problem solving
  * Eliminate redundant recursion with memoization (caching)
  * Eliminate the remaining recursion by using a tableau

### Illustrative Example: computing binomials

* Consider:
  $${n \choose k} = \frac{n!}{(n-k)!k!}$$
* Pascal's Identity:
$${n \choose k} = {n-1 \choose k-1} + {n-1 \choose k}$$
* Base case:
  $${n \choose n} = 1 = {n \choose 0}$$

## FAST Method

https://www.byte-by-byte.com/fast-method/

* First Solution
* Analyze the first solution
* Identify the *S*ubproblems
* Turn the solution around

## Basic Steps

* Identify a value that represents the desired solution/optimal solution to a problem
* Identify a recurrence identity in terms of "smaller" values of the problem
   * Use math to prove your recurrence is correct ("Optimal Substructure Property")
   * Identify the (trivial) base case
   * Identify the desired *final* result
* Design a table or "tableau" that holds values to each "sub"solution
* Possibly: you may need to keep track of additional data in order to reformulate the solution
* You then design your loops to fill in the table so that the necessary subproblems are available in a proper order
* Then you fill out the table in the order you need to

## Problem: Dynamic 0-1 Knapsack Problem

* Analysis:
  * The size of the table is $n \times W$
  * Thus filling out the table is $O(nW)$
  * Can you treat $W$ as a constant?  If so, it **looks** to be linear: $O(n)$
  * It could be that $W = O(2^n)$
  * Generally the input size is bounded by some value, suppose $n$
  * What is the maximum value you can represent  if you have $n$ bits?  $2^n - 1$
  * This algorithm is "pseudolinear": the analysis is *hiding* the true complexity if you ignore $W$
  * The 0-1 knapsack problem is $\mathsf{NP}$-complete: no polynomial time algorithm is known for it (or even though to exist)

## Optimal Binary Search Trees (OBSTs)

* Given a set of keys and a probability distribution of searching those keys, create the "optimal" binary search tree
* Keys are still *ordered* and the BST property must be maintained
* Don't want to necessarily *balance* the tree: want to optimize for searches
* Optimization: minimize the number of *expected* key comparisons

Basic Idea

* Keys: $k_1, \ldots, k_n$ with probabilities $p_1, \ldots, p_n$
* Let $C_{i,j}$ be the optimal BST for keys $k_i, \ldots, k_j$...


```text





```

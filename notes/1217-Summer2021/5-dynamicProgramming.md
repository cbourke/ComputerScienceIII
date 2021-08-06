
# Computer Science III
## CSCE 310 - Summer 2021
### Dynamic Programming

## Introduction

* "Dynamic" = fancy marketing term
* Basic Idea
  * Divide & Conquer approach to problem solving
  * Eliminate redundant recursion with memoization (caching)
  * Eliminate the remaining recursion by using a tableau

## Motivating Example: computing binomials

* Consider:
  $${n \choose k} = \frac{n!}{(n-k)!k!}$$
* Pascal's Identity:
$${n \choose k} = {n-1 \choose k-1} + {n-1 \choose k}$$
* Base case:
  $${n \choose n} = 1 = {n \choose 0}$$

## Basic Steps

* Identify a value that represents the desired solution/optimal solution to a problem
* Identify a recurrence identity in terms of values of "smaller" problems
  * Prove your recurrence is correct ("Optimal Substructure Property")
  * Identify trivial base cases
  * Identify the desired final result
* Design a table/tableau: that holds values to each "sub"solution
* Possibly: you may need to keep track of additional data in order to build the actual solution
* You design loops to fill in the cells of the table so that "sub" problems that needed are computed first
* fill out the cells in the table in the order that you need them

## Problem: Dynamic 0-1 Knapsack Problem

* Given a collection of items with weights and values and a maximum capacity $W$, we want to take as many items as possible to maximize our value subject to the weight constraint
* Building a solution
* Complexity
  * Filling out the table is simply $O(nW)$ where $n$ is the number of items and $W$ is the weight capacity
  * Building a solution can be done in $O(n)$
  * If we assume that $W$ is a constant, is the complexity linear?
  * Pseudolinear: the analysis is "hiding" the true complexity by ignoring $W$
  * It could be that $W = O(2^n)$
  * Suppose you have $n$ bits to represent $W$, then $W$ could be as large as $2^n$
  * Consequently: your tableau would be exponentially sized

## Problem: Optimal Binary Search Trees

* Given a set of keys and a probability distribution of searching those keys, create the "optimal" binary search tree

```text














```

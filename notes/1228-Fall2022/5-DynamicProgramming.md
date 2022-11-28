
# Computer Science III
## CSCE 310H - Fall 2022
### Dynamic Programming

## Introduction

* "Dynamic" = fancy marketing term
* Basic Idea
  * Divide & Conquer approach to problem solving
  * Eliminate redundant recursion with memoization (caching)
  * Eliminate the remaining recursion by using a tableau

## Motivating Example: Computing Binomials

* Consider:
  $${n \choose k} = \frac{n!}{(n-k)!k!}$$
* Pascal's Identity:
  $${n \choose k} = {n-1 \choose k-1} + {n-1 \choose k}$$
* Base cases:
    $${n \choose n} = 1 = {n \choose 0}$$

## FAST Method

https://www.byte-by-byte.com/fast-method/

* First Solution
* Analyze the first solution
* Identify the *S*ubproblems
* Turn the solution around


```python


n = 100
k = 50

def binomial(n, k):
    """returns the value n choose k"""
    if n == k or k == 0:
        return 1
    else:
        return binomial(n-1,k-1) + binomial(n-1, k)

def binomialMemoization(map, n, k):
    """ computes the value n choose k using memoization
        the given map is assumed to be dictionary mapping
        (n, k) => n choose k
    """
    if (n, k) in map:
        return map.get( (n, k) )
    elif n == k or k == 0:
        return 1
    else:
        a = binomialMemoization(map, n-1, k-1)
        b = binomialMemoization(map, n-1, k)
        r = a + b
        map[ (n,k) ] = r
        return r

def binomialDynamicProgramming(n, k):
    """produces the value of n choose k using dynamic programming:
       filling out a tableau of pascal's triangle
    """
    c = {} # (i, j) => i choose j values
    for i in range(0, n+1):
        for j in range(0, min(i, k) + 1):
            #if a base case:
            if i == j or j == 0:
                c[ (i,j) ] = 1
            else:
                c[ (i,j) ] = c[ (i-1,j-1) ] + c[ (i-1,j) ]
    return c[ (n,k) ]


r = binomialDynamicProgramming(n, k)
print(f"{n} choose {k} = {r}")
```

## Basic Steps

* Identify a value that represents the desired solution/optimal solution to a problem
* Identify a recurrence identity in terms of "smaller" values of the problem (subsolutions)
  * You use math to prove your recurrence is correct ("Optimal Substructure Property")
  * Identify the trivial base cases
  * Identify the final desired result
* Design a table or "tableau" that holds values for each subproblem
* POssibly: you may need to keep track of additional information in order to build the actual solution; the table may only hold the optimal *values*
* You then design your loops to fill out the tableau in an order such that the needed subproblem solutions are available
* Then you fill out the table in the order you need to

## Examples

* Optimal Binary Search Trees
* 0-1 Knapsack Problem

## Optimal Binary Search Trees (OBSTs)

* Given a set of keys and a probability distribution of searching those keys, create the "optimal" binary search tree
* Keys are still *ordered* and the BST property must be maintained
* Don't want to necessarily *balance* the tree: want to optimize for searches
* Optimization: minimize the number of *expected* key comparisons

Basic Idea

* Keys: $k_1, \ldots, k_n$ with probabilities $p_1, \ldots, p_n$
* Let $C_{i,j}$ be the optimal BST for keys $k_i, \ldots, k_j$...

## 0-1 Knapsack Problem

### Illustrative Example

Consider the following input:
  * Items: $a_1, a_2, \ldots, a_{13}$
  * Weights: $\vec{w} = 5, 3, 8, 9, 7, 1, 4, 9, 8, 1, 3, 2, 3$
  * Values:  $\vec{v} = 22, 55, 36, 48, 10, 35, 25, 15, 8, 44, 47, 13, 30$
  * Capacity: $W=15$
Consider:
  * $V_{i,j} = V_{6,8}$
  * Interpretation: What is the optimal solution value involving
    * Items $a_1, a_2, a_3, a_4, a_5, a_6$
    * With (intermediate) capacity 8?
  * Consider the **previous** optimal solution involving
    * Items $a_1, a_2, a_3, a_4, a_5$
    * Same weight capacity of 8
    * Best possible solution has value $V_{5, 8}$
    * Best value: 77
    * Items $a_1, a_2$
    * Weight is 8 (we're at the intermediate capacity)
  * Consider taking $a_6$ instead:
    * If we don't take it, then we have the same solution:
    $a_1, a_2$, ie: $V_{5,8}$ or $V_{i-1,j}$ in general
    * If we do: then we need to get rid of something else
    * Adding $a_6$:
      * We have an added value of +35
      * We have reduced our capacity by the weight of $a_6$: which is 1
      * New weight capacity is 7:
      * Reduces our capacity to $j - w_6 = 8 - 1 = 7$
      * Then the best subsolution is $V_{i-1, j-w_i} = V_{5, 7} = 55$
      * New solution: $a_2, a_6$ (weight: $3 + 1 = 4$, value: $55 + 35 = 90$
      * 90 is better than 77, so *we choose to include $a_6$*
      * Column 8: changes from $77$ to $90$ indicating we took item $a_i = a_6$



```text












```

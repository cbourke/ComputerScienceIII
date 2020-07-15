
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
* We often *need* to take the *structure* of a problem into account
* Structure can be exploited
* For brute force algorithms: we may not need to consider a large number of possible solutions (combinations/permutations)
* General technique: backtracking
  * Iteratively (recursively) build a (partial) solution until it becomes unfeasible, in which case you *backtrack* and build a different solution
  * Wondering around a maze
  * Playing games (chess): looking ahead to possibilities and ignoring losing moves
   
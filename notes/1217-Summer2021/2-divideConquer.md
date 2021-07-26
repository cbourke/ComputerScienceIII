
# Computer Science III
## CSCE 310 - Summer 2021
### Divide & Conquer Algorithms

### Introduction

* Divide a problem into smaller problems
* Until the problem is easily or trivially solved (base case)
* You may then need to combine sub-solutions to produce a solution the larger problem
* Usually such approaches are presented as recursive, but they don't have to be
* Well-suited for parallelization and distribute computing
  * MapReduce
  * Searching & Sorting
  * Tournament style strategies

## Repeated squaring

* Task: compute
  \[ a^n \mod m \]
  for "large" $n$
* A naive approach of making $n-1$ multiplications leads to an exponential inefficiency
* Repeated squaring: compute $a, a^2, a^4, a^8, \ldots$ using only 1 multiplication each
* Include the result depending on the bit representation of $a$
* Leads to a $O(\log{n}) = O(N)$ where $N$ is the actual *true* input size
* IE this algorithm is linear with respect to $n$

### Karatsuba Multiplication

* Can use the FOIL rule to reduce number of multiplications using a recursive divide & conquer approach

### Strassen's Matrix Multiplication

* Normal definition implementation of matrix multiplication of two $n \times n$ matrices requires:
  * $n^3$ multiplications
  * $n^2(n-1)$ additions
  * Both are cubic
* Strassen's identities led to 1 fewer multiplication (for $2 \times 2$ matrices) but 18 additions
* Strassen's identities generalize to any $n \times n$ matrix
* Problem: to divide evenly each time all through the recursion, requires matrices that are of size some power of 2: $n = 2^k$
* You can always pad out a matrix with zeros (left, right, bottom, top) without changing its values
* When you are done, you can "trim"
* How much better is this?
  * The number of multiplications made by Strassen is $O(n^{2.8074})$
  * Likewise, the same analysis can show you that the number of additions is *also* $O(n^{2.8074})$
* Other improvements:
  * Winogard: $O(n^{2.3756})$
  * Williams: $O(n^{2.3727})$

### Closest Pair Revisited

* Review
* Naive Divide & Conquer approach
* Outline of the good recursive/divide and conquer closest-pair algoirthm:

Input: a set of points $S$, presorted with respect to the x coordinate

0. Base case: if the size of $S$ is "small enough": use brute force (generate all pairs) to solve the problem, return the pair/distance of the minimum distance pair
1. Partition $S$ into two roughly equally sized arrays/lists, $L$ and $R$
2. Recursively find the two closest points (p, q) in $L$ and (r, s) in $R$
3. Choose the closest pair between (p, q) and (r, s), call it (p, q) with distance $\delta$
4. Find the median x between the two Insertions
5. Build a subset of $S$ whose x values are in $[m - \delta, m + \delta]$
  * You need to use binary search to find these slice cutoffs: using a linear search gives you $O(n)$ behavior and overall a quadratic algorithm
  * Tip: make sure you include ALL points that may have equal $x$ values
  * Tip: you may want to maintain a *separate* left and right slice
6. For each p in the left slice: compute the distance to each potential point in the right slice; if you find a closer pair, update the closest pair/distance
  * Careful: there may be O(n) points in the right slice.
  * Solution A: sort the right slice with respect to their $y$ coordinates, use binary search to limit the number of comparisons to the $y$-range $[p.y-\delta, p.y + \delta]$
  Solution B: so avoid resorting by sorting once and maintaining 2 lists, by-X and by-Y; when you split the lists, you split the Y list too


```text




```

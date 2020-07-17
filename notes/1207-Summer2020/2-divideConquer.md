
# Computer Science III
## CSCE 310 - Summer 2020
### Divide & Conquer Algorithms

### Introduction 

* Divide a problem into smaller problems
* Until each problem is trivially solvable
* May need to combine sub-solutions to produce a larger solution
* Usually presented as recursive, but doesn't have to be
* Well-suited for parallelization and distributed computing
* MapReduce
* Searching & Sorting
* Tournament style operations

### Examples and Tools

* General divide & conquer approach on arrays for searching for a particular element
  * Divide by a constant

  ```python

  a = [4, 5, 2, 3, 9, 2, 3]

  def search(a, i, key):
    if i >= len(a):
      return None
    elif a[i] == key:
      return i
    else:
      return search(a, i+1, key)

  index = search(a, 0, 3)
  print(index)
  ```
  
  * Divide by a factor: dividing into two or more parts
   
  ```python

  import math

  a = [0, 1, 4, 5, 2, 3, 9, 2, 3, 42]

  def search(a, l, r, key):
    m = math.floor((l + r) / 2)
    if l > r:
      return None
    elif a[m] == key:
      return m
    else:
      #search the left:
      i = search(a, l, m-1, key)
      if i is not None:
        return i
      return search(a, m+1, r, key)

  index = search(a, 0, len(a)-1, 0)
  print(index)
  ```     

  #### Master Theorem

  Let $T(n)$ be a monotonically increasing function that satisfies

  \[
  \begin{array}{lcl}
  T(n) & = & aT(\frac{n}{b}) + f(n)\\
  T(1) & = & c
  \end{array}\]

  where $a \geq 1, b \geq 2, c> 0$.  If $f(n) \in \Theta(n^d)$ where $d \geq 0$, then

  \[T(n) = \left\{
           \begin{array}{lcl}
           \Theta(n^d) & \mathrm{~if~} a < b^d\\
           \Theta(n^d\log{n}) & \mathrm{~if~} a = b^d\\
           \Theta(n^{\log_b{a}}) & \mathrm{~if~} a > b^d
           \end{array}\right.\]

### Closest Pair of Points

* Divide & Conquer approach work for the closest pair of points?
  * Divide the set of points into two sets 
  * Recursively find the two closest points in each subset
  * When you have a subset of size 2: trivially, those two points are the closest
  * 


```text











```
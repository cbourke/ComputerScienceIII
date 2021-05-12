
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
  * Observation: there are only a constant number of points that we have to consider on the right hand side which gives us a recurrence:
  
  $$C(n) = 2C(n/2) + O(n)$$
  
  * By the master theorem, this gives us $\Theta(n\log{n})$

### Repeated Squaring/Fast Binary Exponentiation

* Task: compute 
  \[ a^n \mod m \]
  for "large" $n$
* A naive approach of making $n-1$ multiplications leads to an exponential inefficiency
* Repeated squaring: compute $a, a^2, a^4, a^8, \ldots$ using only 1 multiplication each
* Include the result depending on the bit representation of $a$
* Leads to a $O(\log{n}) = O(N)$ where $N$ is the *true* input size (linear)

### Karatsuba multiplication

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

### More Matrices: Gaussian elimination

* Not directly related to divide & conquer BUT it involves matrices
* Indirectly related to divide & conquer with respect to the *determinant* of a matrix  
* THe determinant of a $n \times n$ matrix models the "signed volume" of a linear transformation or a "parallelogram" in $n$-dimensional space
* The "official" definition of the determinant is 
$$\det{A} = \sum_{\sigma \in S_n} \left[ \mathrm{sgn}(\sigma) \prod_{i=1}^n A_{i, \sigma_i} \right]$$
where $S_n$ is the symmetric group on $n$ elements (the set of all permutations).

Divide & Conquer:

\[\det A = \sum_{j=1}^n s_j a_{1j}\det{A_j}\]

where

\[s_j = 
\left\{\begin{array}{ll}
1 & \textrm{if $j$ is odd}\\
-1 & \textrm{if $j$ is even}
\end{array}\right.\]

* $a_{1j}$ is the element in row 1 and column $j$
* $A_j$ is the $(n-1) \times (n-1)$ matrix obtained by deleting row 1
     and column $j$ from $A$
*  If $n = 1$ then $\det{A} = a_{11}$

* Observation: the determinant of an upper-diagonal matrix (triangular matrix) is simply the product of its diagonal elements
* You can apply various elementary operations to a matrix to make into an upper diagonal matrix and preserve the value of the determinant.

## Linear Systems

* Given $n$ equations with $n$ variables $\vec{x} = (v_1, \ldots, v_n)$
* Build an augmented matrix $A\vec{b}$
* Make the matrix upper triangular: elements below the diagonal are all zero
* for each row $i$: we make elements in column $i$ zero below the element $a_{i,i}$

```text











```

# Computer Science III
## CSCE 310 - Fall 2021
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

### General Tools

* Divide into 2 parts
* Recursion
* Combine/Conquer
* Recursion is essentially induction
* Master Theorem

```python


def linearSearchIterative(a, key):
  """
  Returns an index at which the key exists, None if no such element
  """
  for i in range(0, len(a)):
      if a[i] == key:
          return i
  return None

def linearSearchDivideConquer(a, left, right, key):
    #base case
    if left > right:
        return None
    if left == right:
        if a[left] == key:
            return left
        else:
            return None
    m = math.floor((left + right) / 2)
    # recursive step:
    #  search the left part
    #     if success: stop, return the index
    result = linearSearchDivideConquer(a, left, m, key)
    if result is not None:
        return result
    #  search the right part
    #     return success/failure
    return linearSearchDivideConquer(a, m+1, right, key)


a = [5, 2, 9, 3, 2, 1, 0, 9, 4, 7]
key = 42
index = linearSearchDivideConquer(a, 0, len(a)-1, key)
print(f"Found {key} at index {index} ")
```

## Repeated Squaring

* Task: compute
  \[ a^n \mod m \]
  for "large" $n$
* A naive approach of making $n-1$ multiplications leads to an exponential inefficiency
* Repeated squaring: compute $a, a^2, a^4, a^8, \ldots$ using only 1 multiplication each
* Include the result depending on the bit representation of $a$
* Leads to a $O(\log{n}) = O(N)$ where $N$ is the actual *true* input size
* IE this algorithm is linear with respect to $n$

### Input Sizes

* Suppose you have a number $n$ as an input to an algorithm
* Note however that $n$ is NOT the input size!!!
* The input size of a number is $\log_2(n)$

## Greatest Common Divisor

* Definition: $a$ *divides* $b$ and we write $a | b$ if there exists an integer $k$ such that
  $$b = ak$$
* More generally, any integer can be written as
  $$b = ak + r$$
with remainder $r$
* Equivalent notation: congruences
* $a$ is *congruent* to $r$ modulo $m$:
  $$a \equiv r\pmod{m}$$
* Equivalently: $m$ devides $a - r$ or
$$a \equiv r\pmod{m} \iff a = mk + r$$
* The *greatest common divisor* (GCD) of two integers $a, b$ written as $gcd(a, b)$ is the largest integer that divides both $a$ and $b$
* Example: $gcd(60,210) = 30$
* THe GCD always exists:
* If $gcd(a, b) = 1$ then $a, b$ are *relatively prime*

### Simple Euclid

* Demonstration: $gcd(1768,184)$
* It only gives you the GCD of the two numbers
* Analysis: GCD is a linear algorithm

### Extended Euclid

* Computes GCD, $s, t$ such that:
  $$gcd(a, b) = sa + tb$$
* $s, t$ are the Bezout coefficients

### Application: Public Key Cryptography

#### Overview

* Motivation: want to communicate securely without prior interaction/agreement
* You can publish a *public key* such that anyone can *encrypt* a message and send it to you over an insecure channel
* Your *private key* can be used to *decrypt*
* It should be *computationally difficult* to compute the private key from (just) the public one
* Trap-door functions

### Algebra


* $\mathbb{Z}_m$
* This is known as an algebraic *group*: closed under addition, additive inverse (actually a *ring*)
* Does not necessarily have a *multiplicative* inverse
* An *inverse* of a number $x \in \mathbb{Z}$ is a number $x^{-1}$ such that
  $$xx^{-1} \equiv 1\pmod{m}$$
* Theorem: an inverse of $x$ modulo $m$ exists if and only if $x$ and $m$ are relatively prime
* Field: $\mathbb{Z}_p$
* Computing Inverses: Extended Euclid
* Computes GCD, $s, t$ such that:
  $$gcd(a, b) = sa + tb$$
* If (and only if) GCD is 1, then:
    * $s = a^{-1} \mod{b}$
    * $t = b^{-1} \mod{a}$

### RSA

* Choose two "large" prime numbers $p, q$
* Compute $n = pq$
* Compute Euler's totient $\phi(n) = (p-1)(q-1)$
* Choose $a$ such that $2 \leq a \leq \phi(n)$ such that $gcd(a, \phi(n)) = 1$
* This guarantees there is an inverse, $a^{-1} \bmod \phi(n)$
* Compute $b = a^{-1} \bmod \phi(n)$
* Publish $n, a$ as your public key
* Keep $p, q, b$ private
* Encryption is done via:
  $$e_k(x) = x^a \bmod n$$
* Decryption:
  $$d_k(y) = y^b \bmod n$$

### Closest Pair Revisited

* Given $n$ points in the Euclidean plane, we want to find the two closest pair of points
* Brute Force: you try all pairs, ${n \choose 2} \in O(n^2)$
* Naive divide & conquer:
  * Divide the points two sets into 2 sets
  * Conquer: recursively finding the two closest pairs
  * BUT when we "come back" from the recursion, we still have 2 pairs of points that are the closest...

Input: a set of points $S$, presorted with respect to the x coordinates

0: Base case: if the size of $S$ is "small enough" then use brute force (generate all pairs) to solve the problem, return the pair/distance of the two closest points
1. Partition $S$ into two roughly equally sized lists of points, $L, R$ via their x-coordinates
2. Recursively find the two closest points $(p,q)$ in the left, $(r,s)$ in the right
3. Choose the closest pair between $(p,q), (r, s)$, WLOG suppose this is $(p,q)$ with a distance $\delta$
4. Find the median $x$-value (call it $m$) between the two partitions
5. Build a subset of $S$ whose $x$ values are in $[m - \delta, m + \delta]$
  * You *need* to or *should* use binary search to find these slice cutoffs: using linear search gives you $O(n)$ behavior and a quadratic algorithm
  * Tip: it may help to keep track of a left slice and a right slice separately
  * Tip: make sure you include ALL points with an equal $x$ value!
6. For each point $p$ in the left slice: compute the distance to each potential point in the right slice, if you find a closer pair, update your closest pair
  * Careful: you cannot (or should not) compare it to *every* point in the right slice otherwise it would be $O(n)$ and over all a quadratic algorithm!
  * Solution A: sort the right slice with respect to their $y$ coordinates, use binary search to find the "cutoffs"
  $[p.y-\delta, p.y + \delta]$
  * Solution B: so avoid resorting by sorting once and maintaining 2 lists, by-X and by-Y; when you split the lists, you split the Y list too

## "Better" Multiplication

* Problem: given two $n$-digit integers $a, b$, compute $a \times b$
* The naive "grade school" multiplication method makes $O(n^2)$ single digit multiplications
* Is there a "better" way?
* Toom Cook: 1963 $O(n^{1.465})$
* Schonhage-Strassen (1968, FFT): $O(n\log{n}\log{\log{n})})$
* Furer (2007): $O(n\log{n}\cdot2^{\log^*{n}})$
* 2019: reached optimality: $O(n\log{n})$

## Strassen's Matrix Multiplication

* Matrix multiplication in sub-$O(n^3)$ time

## Related: Using Matrices to Solve Linear Systems

* Consider a linear system in $n$ variables...




```text








```

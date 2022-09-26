# Computer Science III
## CSCE 310H - Fall 2022
### Divide & Conquer Algorithms

### Introduction

* Divide a problem into smaller problems
* Until the problem is easily or trivially solved (base case)
* You may then need to combine sub-solutions to produce a larger solution to the actual problem
* Usually presented as a recursive solution, but it doesn't have to be
* Well-suited for general approaches: parallel computing/distributed computing
  * MapReduce
  * Searching & Sorting: Binary search, quick sort, merge sort
  * Tournament style strategies

```python
#import math

def linearSearchIterative(a, key):
  """
  Returns an index at which the key exists, None if no such element
  """
  for i, x in enumerate(a):
      if x == key:
          return i
  return None

def linearSearchRecursive(a, key, left, right):
    """
    Returns an index at which the key is found, None if no such element
    """
    if left > right:
        #empty (sub) list:
        return None
    elif left == right:
        if key == a[left]:
            return left
        else:
            return None
    else:
        # m is the "middle" index
        m = int( (left + right) / 2 )
        # search the left half:
        index = linearSearchRecursive(a, key, left, m)
        if index is not None:
            # don't bother with the right half
            return index
        # search the right half:
        index = linearSearchRecursive(a, key, m+1, right)
        return index


        def linearSearchRecursiveVersion2(a, key, index) -> int:
            """
            Returns an index at which the key is found, None if no such element
            """
            if index == len(a):
                return None
            else:
                if a[index] == key:
                    return index
                else:
                    return linearSearchRecursiveVersion2(a, key, index+1)

a = [5, 2, 9, 3, 2, 1, 0, 9, 4, 7]
key = 42
index = linearSearchRecursive(a, key, 0, len(a)-1)

print(f"Found {key} at index {index}")
```

## More Math Fun

* Task: compute
  $$a^n \bmod m$$
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
* More generally, any integer can be rewritten as
  $$b = aq + r$$
* Equivalent notation: congruences
* $a$ is *congruent* to $r$ modulo $m$:
    $$a \equiv r\pmod{m}$$
* Equivalently: $m$ devides $a - r$ or
    $$a \equiv r\pmod{m} \iff a = mk + r$$
* The *greatest common divisor* (GCD) of two integers $a, b$ written $\gcd(a, b)$ is the largest integers that divides both $a$ and $b$
* Example: $\gcd(60, 210)$

### Simple Euclid

* It repeatedly divides one by the other to get the remainder (gcd must divide both a and b and its remainder (algebra)); until it has no remainder
* The number of iterations is maximized when one of the values is 2,
* The max number of iterations is $O(\log(b)) = O(n)$
* Remember: the input size is $n = \log{(b)}$ (the number of bits required to represent $b$)
* Therefore this is a *linear* algorithm
* Implementation: python

### Extended Euclidean Algorithm

* Keeps track of more information in order to give you *Bezout* coefficients

#### Modern Algebra

* There are sets of elements and operations on those sets of elements
* These sets have more and more structure if operations conform to certain properties
* By keeping track of more information (quotients); you can *compute inverses*!
* Given $a, b$, we want to compute $a^{-1} \bmod b$

### Application: Public Key Cryptography

#### Overview

* Motivation: want to communicate securely with someone without having prior communication
* You can publish a *public key* that anyone can use to encrypt a message and send to you
* You use a *private key* to decrypt the message
* as long as no one has the private key, it is secure OR
* as long as it is computationally infeasible to derive the private key from the public key, then it is secure
* One-way trap door function

### RSA

* Choose two "large" prime numbers $p, q$
* Compute $n = pq$
* Compute Euler's Totient function: $\phi(n) = (p-1)\cdot(q-1)$
* Choose $a$ such that $2 \leq a \leq \phi(n)$ such that $gcd(a, \phi(n)) = 1$
* typically we choose 65537
* This guarantees there is an inverse, $a^{-1} \bmod \phi(n)$
* Compute $b = a^{-1} \bmod \phi(n)$
* Publish $n, a$ as your public key
* Keep $p, q, b$ as private
* Encryption:
  $$e_k(x) = x^a \bmod n$$
* Decrypt:
  $$d_k(y) = y^b \bmod n$$
* Observations:
  * Both encryption and decryption and the system setup are all computationally efficient
  * exponentiation: repeated squaring
  * generate primes (easy)
  * inverse: extended euclidean algorithm
* Observations:
  * How do you break RSA?
  * You need to find the inverse, which means you need to find the totient, which means finding $p, q$
  * You have $n = pq$: you need to factor $n$
* Other ways of breaking RSA:
  * look for flaws in the implementation that an be exploited


```python

from euclid import inverseMod


# choose two "large" primes
p = 74217184163048431963832600587002469451524514974745153970702424474604108986849
q = 72827623597574187110970757719612267008966857667509013434053059553366108132709
n = p * q
totient = (p-1) * (q-1)
#choose an a relatively prime to totient:
a = 65537

#compute b = a^-1 mod totient
b = inverseMod(a, totient)

publicKey = (a, n)
privateKey = (p, q, b, n)

#encode and encrypt a message...
message = 'Lets attack at noon, okay?'
# convert my string into a "number"
bytesOfMessage = bytes(message, 'ascii')
# convert the raw bytes to an integer...
x = int.from_bytes(bytesOfMessage, "big") #big endian: MSB at the left
print(x)

#encrypt:
#y = x^a mod n
y = pow(x, a, n)

print(y)
# try to convert our encrypted number back to a string:
encryptedBytes = y.to_bytes(256, "big")
#print(encryptedBytes)
encryptedText = encryptedBytes.decode("UTF-8", errors='ignore')
print(encryptedText)

# decrypt:
# y^b mod n
decryptedNumber = pow(y, b, n)
print(decryptedNumber)
decryptedBytes = decryptedNumber.to_bytes(256, "big")
decryptedText = decryptedBytes.decode("UTF-8", errors='ignore')
print(decryptedText)
```


## Closest Pair Revisited

* Brute Force solution: $O(n^2)$
* Given $n$ points in the Euclidean plane, we want to find the two closest pair of points
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
6. For each point $p$ in the left slice: compute the distance to each potential point in the right slice, if you find a closer pair, update your closest pair
  * Careful: you cannot (or should not) compare it to *every* point in the right slice otherwise it would be $O(n)$ and over all a quadratic algorithm!

### Tools & Tips

* We need a couple of binary search implementations:
  * Given a set of points (or numbers) and a key, find an element matching that key OR in the event that no such element exists, find where it "should" be...
  * Given a set of points (or numbers) and a *range* (low, high), find indices `(i,j)` such that all values in the set $a[i]..a[j]$ lie within the range
  * To create a left/right slice, you can use the `rangeBinarySearch` to get all points whose `x` coordinate lie within a range
  * You can reuse the same idea/binary search to limit in the `y` axis: BUT they are not necessarily sorted with respect to the `y` coordinates
    * Solution: resort values in the right slice by their `y` coordinates and repeat the binary search to limit in the `y`-direction (for each point): $O(n\log(n))$
    * Solution (not recommended): maintain two lists before the algorithm begins, one sorted wrt $x$, one sorted wrt $y$; then when you build a left/right slice, you also limit the second subarray (the one sorted wrt the $y$-coordinate, $O(n)$)

```python


def binarySearch(arr, key):
    """
    Performs a binary search on the given list (arr) which is assumed
    to be sorted for the given key element.

    If such an element is found, it returns *an* index at which it
    exists.  If no such key element is found, returns an index at which
    it *would* appear if it were to be inserted in order.

    for example,
    [4, 6, 7, 8, 8, 8, 8, 10, 12, 12, 20]
    - a search for 7 would return 2
    - a search for 8 would return 3, 4, 5, or 6
    - a search for 2 would return 0
    - a search for 4 would return 0
    - a search for 20 would return 10
    - a search for 25 would return 11
    - a search for 9 would return 7
    """
    n = len(arr)
    if key < arr[0]:
        return 0
    elif arr[n-1] < key:
        return n
    left = 0
    right = n-1
    while left <= right:
        m = (left + right) // 2
        if arr[m] == key:
            return m
        elif key < arr[m]:
            # search left
            right = m - 1
        else:
            # search right
            left = m + 1
    # not found...
    # return the index where it *should* be
    return left

def rangeBinarySearch(arr, lower, upper):
    """
    Returns a pair of indices, (i, j) such that all values in the array/list
    lie within the range given: [lower, upper]
    """
    n = len(arr)
    i = binarySearch(arr, lower)
    #shift i down as long as arr[i] == lower
    while i > 0 and arr[i-1] == lower:
        i -= 1
    j = binarySearch(arr, upper)
    while j < n and arr[j] == upper:
        j += 1
    return (i, j)


arr = [4, 4, 4, 6, 7, 8, 8, 8, 8, 10, 12, 12, 20, 20, 20]
(i, j) = rangeBinarySearch(arr, 7.1, 7.5)
slice = arr[i:j]
print("result = ", slice)
```

## Multiplication

* Problem: given two $n$-digit integers $a, b$, compute $a \times b$
* The naive "grade school" multiplication method makes $O(n^2)$ single digit multiplications
* Karatsuba: $O(n^{1.58 \ldots})$
* Toom Cook: 1963 $O(n^{1.465})$
* Schonhage-Strassen (1968, FFT): $O(n\log{n}\log{\log{n})})$
* Furer (2007): $O(n\log{n}\cdot2^{\log^*{n}})$
* 2019: reached optimality: $O(n\log{n})$

## Strassen's Matrix Multiplication

* What if you don't have square matrices?
* What if your matrices are not nice "powers of two"
* Pad them out with zeros!


```text






```

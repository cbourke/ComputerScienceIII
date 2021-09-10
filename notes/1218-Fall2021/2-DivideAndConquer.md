
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

## Input Sizes

* Suppose you have a number $n$ as an input to an algorithm
* Note however that $n$ is NOT the input size!!!
* The input size of a number is

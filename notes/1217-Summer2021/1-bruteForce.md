
# Computer Science III
## CSCE 310 - Summer 2021
### Brute Force Algorithms

* In general not a great solution; not really efficient
* You generate or examine every possible solution to find *a* solution or the *best* solution to a problem
* Often creating a brute force solution helps you to understand the problem and look for *structure* to exploit
* Often such approaches require generating combinatorial objects
* Example: finding the closet pair (generating combinations of size 2 = generating subsets of size 2 of a set of size *n*)

## Generating combinations

* Given a set of *n* elements: {1, 2, 3, 4, ..., n}
* Outline:
  * Start with {1, 2, 3, ..., k}
  * Assume that you have elements a_1, a_2, ... a_k
  * Want to generate the next *k* combinations
  * Locate the last element a_i
  such that a_i != n - k + i
  * Replace a_i with a_i + 1
  * replace each a_j with a_i + j - i for all j: i+1 ... k

```c









```

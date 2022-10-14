# Computer Science III
## CSCE 310 - Fall 2022
### Data Structures

## Review

### Trees, Binary Search Trees, Heaps

* Trees are acyclic graphs
* Binary Search Trees:
  * Each node contains a unique *key* element (integers)
  * Oriented: top to bottom, left to right
  * The *root* is at the top
  * Nodes may have *children*: left child and/or the right child
  * A node with no children is a *leaf*
  * Binary Search Tree Property: for every node with key $k$,
    * Every node in its left-sub-tree has a key value less than $k$
    * Every node in its right-sub-tree has a key value greater than $k$
  * Search for nodes: start at the root, compare key values; if the value you're searching for is less, go to the left child, if greater go to the right child
* Demo
  * Operations
    * Search
    * Insert
    * Delete
  * Traversals:
    * Preorder: root-left-right manner
    * Inorder: left-root-right
    * Postorder left-right-root
    * BFS

### Application: Huffman Coding

* Coding Theory:
  * Add redundancy to ensure information is not lost over a noisy channel
  * Compression: you want to either remove *redundant* formation or reduce its size in order to make it smaller
  * Lossy compression: mp3s, mp4s, jpeg, PNGs, etc.
  * Lossless compression: zip, gzip, huffman
  * Huffman coding:
    * English have a lot of redundancy: non-uniform distribution of letters
    * Common letters: r, s, t, l, e; less common: z, q
    * Idea: if you use a *fixed length encoding* (ASCII: all letters are 8 bits)
    * Instead: create a *variable* length encoding: more common letters will get shorter encodings, rarer characters will get longer codewords
* Problems: with a fixed length encoding, all decodings are unambiguous: block length encoding
* Variable length encoding *can* be ambiguous
* Solution: create a prefix-free encoding scheme: no codeword (encoding) appears as the prefix of another
  * Observation: with a fixed-length encoding, you automatically have a prefix free code!
* Idea:
  * Build a tree (greedily):
  * First compute the frequency or count of all characters in a file
  * Associate each letter/character with a tree node (eventually a leaf in a binary tree) along with its frequency
  * Iteratively combine trees by combining the least weighted trees until you have formed a single tree
  * When you combine, the weight of the new tree is equal to the sum of its left/right child's weight

### Review: Heaps

  * a min heap is a binary tree such that the key at every node is less than both its children
  * A min heap has the fullness property: all nodes are present except for possibly the last level which is full to the left
  * As a consequence:
    * The minimum element is always at the root
    * The fullness property ensures that the depth $d = O(\log{n})$
  * Two operations become efficient ($O(\log{n})$):
    * getMin(): retrieve the root element, BUT you need to fix the heap
    * insert(): always insert at the "last" (next available) spot (last level, as far left as you can), heapify upward: swap with the parent until the heap property is satisfied

## Balanced Binary Search Trees

* Regular Binary Search Trees may become unbalanced
* THe operations could degrade into $O(n)$ operations because the height is $O(n)$
* Solution: Balanced Binary Search Tree: reconfigures itself if it ever becomes too unbalanced
* AVL Trees and 2-3 Trees
* AVL Trees rebalance themselves if they become unbalanced
* The *height* of a node $u$ in a tree denoted $h(u)$ is the length of the longest path to any descendent leaf
  * Depth: measure with respect to the root
  * Height: measure with respect to leaves
    * The height of a leaf is 0
    * The height of an empty tree is -1 (by convention)
    * The height of a tree itself is the height of its root node
* The *balance factor* of a node $u$ denoted $bf(u)$ is the height of its left-subtree minus the height of its right-subtree
  * A balance factor of zero indicates a well-balanced tree
  * A negative balance factor indicates skew to the RIGHT
  * A positive balance factor indicates skew to the LEFT
* Example: 8, 4, 7, 3, 2, 5, 1, 10, 6
* Summary:
  * Searches are exactly the same
  * Insertions may result in an unbalanced tree needing a left, right, or left-right, or right-left rotation
  * Rebalancing gives an $d = O(\log{n})$
  * Deletions: a bit more complicated

## 2-3 Trees or Simple B-Trees

* Nodes may contain more than one key
* 2-3 Trees: each node can have 1 or 2 keys
* A node with 1 key (a regular old BST node) has two children
* A node with 2 keys has three children
* All nodes except for nodes at the last level have *all children*
* Searching: regular old search, but you may have to determine if you left, middle or right
* Insertion
  * Always done in a leaf
  * If it is a 2 node (1 key) it becomes a 3 node (2 keys)
  * If it is a 3-node, you promote the middle key up, potentially overflowing the parent
  * Insertion may propagate all the way back up to the root node
  * Analysis: if a 2-3 tree has $n$ keys, what is the minimum/maximum depth?
  * In general:
  $$\sum_{i=0}^n x^i = \frac{x^{n+1}-1}{x-1}$$

## Hashing

* Offers *potential* for *amortized* constant-time operations
* Hash-based data structures (sets, hash tables, maps), off $O(1)$ *amortized* operations

Basic Ideas

* elements are stored in a contiguous array
* Random access is cheap and easy (efficient)
* In general, we don't know where each element is stored
* We establish a *hash function*: object -> integer
$$h: \mathbb{Z} \rightarrow \mathbb{Z}_m$$
* Recall: $\mathbb{Z}_m = \{0, 1, 2, \ldots, m-1\}$
* The hash value (modded out) gives you the index at which to store something!
* $m$ here is the size of your array or "table"

## Collisions

* When two elements have the same hash value, they *collide*; "collision"
* How do you resolve these collisions?
* Linear Probing: you simply check the next available cell and insert at the next unoccupied table cell
  * Probing is no longer possible if the array is full
  * As the array gets fuller, the probability of a collision increases, meaning that the complexity devolves into $O(n)$
  * At some point, the fullness makes probing inefficient; you need to *reshash* the table: create a new array of a larger size, rehash all of the previous values

## Reashing

* At some point the performance will degrade: with more and more elements, all the cells become full or dirty or the secondary data structures become "large"
* To resolve this, we rebuild a *new* larger hash table with a new, different hash function
* We *rehash* every single element to this new table: $O(n)$ BUT it is a one-time/infrequent cost
* This is a basic time/space tradeoff:
* You generally keep track of a *load factor*: a value used to determine when you rehash
  * $n / m$ where $n$ is the number of elements (or dirty bits) in the table, $m$ is the size of the array/table
  * $n/m$ is the percentage that it is full
  * A common default: $.75$: once the array is 75% full, you rehash to a bigger (double sized) new array
* This gives you a tradeoff:
  * You can tolerate a low load factor: okay with wasting space to get performance
  * Large tables = fewer collisions = faster operations = more space/more wasted space
  * Smaller tables = higher load factors = more collisions = slower performance = less wasted space
* Also there is such a thing as a "perfect hash function"

## Other Collisions Resolutions

* You can use "chaining": each "cell" is associated with *another data structure*!: linked list or a tree, or, etc.

```text








```

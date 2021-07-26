# Computer Science III
## CSCE 310 - Summer 2021
### Data Structures

Motivating review: Huffman coding

### Huffman Coding

* Coding Theory:
  * Add redundancy to a signal to ensure that information is not lost in a "noisy" channel
  * Compression: want to remove or reduce information for efficient storage
  * Examples: zip files (lossless), JPEGS, MP4s, MP3s, (lossy) etc
  * Huffman coding: lossless (mostly used on text) compression algorithm
  * Common characters are encoded with 'shorter' codewords and rarer characters are encoded with longer codewords (variable length encoding scheme)

#### Background

* An encoding is a mapping of symbols (characters) to binary strings
* A block encoding is a mapping that maps all symbols to codewords (bit strings) of the same length (ASCII)
* In general, block length encodings require codewords of length $\log_2(n)$
* Alternatively: you can use a variable length encoding scheme where each codeword may be of a different length
* Problem: a variable length encoding may be ambiguous.  we need to use a *prefix-free* encoding scheme
* Goal: compression: associate "common" or "high frequency" symbols with shorter codewords and "rarer" or "low frequency" symbols with longer codewords

## Review: Heaps

* a min heap is a binary tree such that the key at every node is less than both its children
* A min has the fullness property: all nodes are present except for possibly the last level which is full to the left
* As a consequence:
  * The minimum element is always at the root
  * The fullness property ensures that the depth $d = O(\log{n})$
* Two operations become efficient ($O(\log{n})$):
  * getMin(): retrieve the root element, BUT you need to fix the heap
  * insert(): always insert at the "last" (next available) spot (last level, as far left as you can), heapify upward: swap with the parent until the heap property is satisfied
* Priority Queues, Heap Sort

### Review: Binary Search Trees

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
  * Problem: Regular binary search trees may be unbalanced
  * Goal: develop and use *balanced* trees: trees whose depth is $O(\log{n})$

### AVL Trees

* The *height* of a node $u$ in a tree, denoted $h(u)$ is the length of the longest path to any of its descendant leaves
* Depth is with respect to the root, height is with respect to the leaves
* The height of a leaf is 0
* the height of an empty tree is -1
* The height of a tree itself is the height of its root node
*  The *balance factor* of a node $u$, denoted $bf(u)$ is the height of its left sub-tree minus the height of its right subtree
  * A balance factor of 0 indicates a well-balanced tree node
  * A negative balance factor indicates a skew to the right
  * A positive balance factor indicates a skew to the left
* An AVL Tree is a BST such that the balance factor of all nodes is -1, 0, or +1
* due to the balance, we get a guarantee of a depth that is $O(\log{n})$
* An AVL Tree guarantees this property by using *rotations*

## B-Trees

* Nodes may contain more than one key
* Every node may have at most $m$ children
* Every node except the root has at least $\lceil m/2 \rceil$ children
* The root has at least 2 children unless it is a leaf
* Non-leaf nodes with $k$ children have $k-1$ keys
* All leaves appear at the same level and are non-empty
* Focus on a special case: 2-3 tress, $m = 3$
  * Every node may have 1 or 2 keys and thus 2 or 3 children
* A "two node" is a node containing 1 key $k$ with 2 children (regular binary tree node)
* A "three node" is a node containing 2 keys $k_1, k_2$ and 3 children
* Insertion:
  * Always done in a leaf
  * If it is a 2-node, it becomes a 3-node
  * If it is a 3-node, you promote the middle key element up, potentially overflowing hte parent

## Hashing

* Balanced BSTs guarantee all operations are $O(\log{n})$
* Hash-based data structures (sets, hash tables, maps), off $O(1)$ *amortized* operations

Basic Ideas

* Elements are stored in a contiguous fixed-sized array
* Easy, "free" random access to elements based on their index
* The actual index/location of each element $x$ is determined by using a *hash function*, $h(x)$
* As long as the hash function is easy to compute, then the index is easy to compute and efficient
* Generally, you use a key instead of the actual object: it is sufficient to consider integers as both input and output to a hash function
* An Object's state can generally be used to provide a non-unique integer representation of the object called a "hash code"
* Generally, a hash function will map:
$$h: \mathbb{Z} \rightarrow \mathbb{Z}_m$$
* $\mathbb{Z}_m = \{0, 1, 2, ..., m-1\}$
* That allows the hash function to map to indices 0 thru m-1 (to an array of size $m$)
* Demo



```







```

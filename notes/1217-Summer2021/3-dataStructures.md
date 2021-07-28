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

## Collision Resolutions

### Open Addressing

* If a collision occurs, you can simply map it to a second value in another location (index)
* Linear Probing: go to the next adjacent cell/index and if it is empty, use it (keep going until you find a free cell)
* Quadratic Probing: use a quadratic function to "probe" for another open location/index
* You generally "wrap" around to the start of the array when you reach the end
* You could also use a secondary hash function to "rehash" it
* Other considerations
  * If the hash table is full, you need to deal with that somehow
  * If you want to support deletion of elements, you will need to keep track of which cells have been used before
  * As the table gets fuller and fuller, collisions are much more likely: all operations become inefficient, O(n) for searching, insertion, deletion

## Chaining:

* Instead of probing for a different cell, you store multiple elements at the same location/index
* To store multiple elements, you need another data structure
* Each cell is a reference to another data structure such as a linked list or a Balanced BST
* Instead of probing, the element is simply added to the secondary data structure
* If you insert a LOT of elements, then it really isn't any better than the secondary data structure you're using
  * Ex: searching becomes O(n)

## Re-Hashing

* At some point the performance will degrade: with more and more elements, all the cells become full or dirty or the secondary data struture becomes large
* To resolve this, you periodically *rehash* and rebuild the table
* You create a larger array with a different hash function to remap/rehash all of the elements
* Rehashing is generally $O(n)$
* Over the lifetime of the data structure, the *average* performance is quite good.
  * For most operations, it will be O(1)
  * Occasionally, you will need to rehash giving O(n)
* You generally keep track of a *load factor* to decide when to rehash the table: $n / m$
  * $n$ is the number of elements in the hash table
  * $m$ is the size of the hash table
  * Example: $n/m = .75$ (table is 75% full)
* Generally this means that a hash table is a time-space tradeoff data structure:
  * Smaller table -> more collisions -> slower access/insert/etc. = less wasted space
  * Larger table -> fewer collisions -> faster operations, but MORE wasted space

## Midterm

* The miderm PDF handout will be auto-posted to Canvas at midnight
* You will have 24 hours in which to complete it and turn in a PDF of it to Canvas
* You are to work individually, no partners, no collaboration at any level
* 100 points, 5 questions, 10% of your grade
* No livestream on Tuesday: instead extended zoom office hours

```







```

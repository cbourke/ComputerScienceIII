
# Computer Science III
## CSCE 310 - Summer 2020
### More Data Structures

* Lists, sets, etc.: array-based lists, linked lists
* Stacks, Queues, Deques

### Tree Review 

* Trees are acyclic graphs
* Binary Search Trees:
  * Each node contains a key
  * Oriented top to bottom
  * Root is at the top
  * leaves are at the bottom
  * Each node may have a parent, a left child and/or a right child
  * BST Property: for each node $u$ with key $k$
    * The key values of the nodes in $u$'s left tree are all less than $k$
    * The key values of the nodes in $u$'s right tree are all greater than $k$
  * Insertion, deletion, retrieval are all proportional to the depth of the tree, $O(d)$
  * You *can* have degenerative trees such that the depth $d \in O(n)$
  * Goal: develop a tree that can *rebalance* itself so that no left/right side is *too* much larger than the other
  * Balanced BSTs have a guarantee of $d \in O(\log{n})$
  
### AVL Trees

* The *height* of a node $u$ in a tree denoted $h(u)$ is the longest path to any of its descendant leaves
* Depth is with respect to the root, but the height is with respect to its leaves
* The height of a leaf is 0
* The height of an empty tree is -1
* The height of a tree is the height of its root (same definition as the depth of a tree)

* The *balance factor* of a node $u$, denoted $bf(u)$ is the height of its left child/tree minus the height of its right child/tree
  * A balance factor of 0 indicates a perfect balance
  * A positive balance factor indicates a skew to the left
  * A negative balance factor indicates a skew to the right
* In general, an AVL tree is a BST such that all nodes have a balance factor of 0, 1, or -1
* Because of the balance factors, you can show that the depth of an AVL tree is always $d \in O(\log{n})$
  * Thus, insertion, deletion, retrieval are all $O(\log{n})$
  * Observe that the rotations are all $O(1)$ operations: you're simply swapping around references/pointers
  * Insertions will only make local changes
  * Updating heights/balance factors is $O(d)$
  * Deletions may cause ripple rotations up the tree, but each one is only $O(1)$ and so all of them would be $O(\log{n})$

## B-Trees

* Every node may have at most $m$ children
* Every node except the root has at least $\lceil m/2 \rceil$ children
* The root has at least 2 children unless it is a leaf
* Non-leaf nodes with $k$ children have $k-1$ keys
* All leaves appear at the same level and are non-empty
* Focus on $m = 3$: 
  * 2-3 Trees
  * Every node may have 1 or 2 keys (2 or 3 children)
* A "two node" is a node containing 1 key $k$ with two children (the usual binary search tree node)
* a "three node" is a node containing 2 keys, $k_1, k_2$ and 3 children
* Insertion:
  * Always done in a leaf
  * If it is a 2 node, then you make it into a 3 node
  * If it is a 3 node, you promote the middle element up, potentially overflowing the parent etc.
* Deletion: you grab the min the righter tree or the max in the lefter tree
  * Observation: such an element is always in a leaf!  
  * Thus, we may need to exchange a key at the bottom
* Analysis: claim is that a 2-3 tree has depth $d \in O(\log{n})$

### Huffman Coding

* Coding Theory: 
  * Adding redundancy to ensure that information is not lost in a "noisy" channel
  * Compressing information (lossy or non-lossy) to reduce its size
    * JPEGS, MPEGS, MP4s, MP3s
* Loss-less coding: encode text so that
  * Common characters are encoded with shorter codewords (bit strings); less common characters are encoded with longer codewords
  * No information will be lost, but
  * potentially, we will encode a file (text) into a smaller file
  * ASCII text: some English characters are less common than others
  * Build a codeword tree: a tree that ensures that common characters have a shorter codeword while less common characters have a longer codeword
  * A tree ensures that we have a prefix-free encoding such that no codeword is the prefix of another codeword

Basics

* Let $\Sigma$ be an *alphabet* of size $n$, for our purposes, $\Sigma = \{0, 1\}^*$ (the set of all binary strings)
* A coding is a mapping of a character set to $\Sigma$
* A block encoding maps characters to fixed length codewords: example: ASCII
  * `'A'` maps to `01000001` (65 in decimal)
* A block encoding scheme requires $\log_2{n}$ bits per character, regardless of their *frequency*
* Alternative: variable length encoding scheme: more common characters are given shorter codewords, less common are give longer code words
* Payoff: your average codeword length is reduced; you end up with compression (English 25-40% smaller files)
* Problem: such encodings need to be prefix free!
* Solution: build a tree with characters at the leaves
  * Every path from the root to a leaf is unique
  * associate 0 and 1 with left/right traversals: the path from any root to any leaf defines a codeword.
  * Associate common (more frequent) characters with "shallow" leaves, less frequent characters with "deeper" leaves

Idea

* Start by computing the frequencies of all the characters in a particular file
* Create $n$ single node trees, each associated with one character and its frequency
* Start combining subtrees by combining the least weighted trees first
  * When you combine a tree, you create a new root node and give it a weight that
  is the sum of the weight of its two subtrees
* Stop when you have only 1 tree left; Huffman Tree

### Hashing

* Balanced BSTs: offer $O(\log{n})$ operations (insert, retrieve, delete)
* Hash-based data structures (sets, tables, maps) offer $O(1)$ *amortized* operations

Basic Ideas

* Elements are stored in a contiguous fixed-size array
* Easy, "free" random access (index-based)
* The location of each element or object is computed using a *hash function*
* Object (state) $\rightarrow$ integer $x$ $\rightarrow$ $h(x) = y$, $y$ will be used as an index to store/retrieve the object
* As long as the hash function $h$ is easy to compute, then the index is also easy to compute (and efficient)
* BUT: we have to ensure that the hash function maps all possible objects/values to the array
  $$h: \mathbb{Z} \rightarrow \mathbb{Z}_m$$
* $m$ is the size of our array, $\mathbb{Z}_m = \{0, 1, 2, \ldots, m-1\}$
* In general, hash functions map a large domain to a small codomain
* Data integrity, crypto: digital signatures, etc.
* Assume we start with integers
* Demo

Collisisions

* Because hash functions are not 1-1, some elements (integers) will map to the same value
* Meaning: some objects will be "stored" in the same index
* When two objects or values map to the same hash value it is known as a collision
* When this happens, we need a way to *resolve* the collision: Collision Resolution

## Open Addressing

* If a collision occurs, you can simply map the second value to some other location
* You can use Linear Probing, a secondary hash function, or some combination, quadratic probing, etc.
* Linear Probing: simply look to the next available "cell" in your array
  * To accommodate deletion, every cell that is eventually occupied will need to have a "dirty bit" set
  * Initially with an emptier hash table, operations are very efficient, $O(1)$ (assuming not too many collisions)
  * But, as the table gets fuller or more of its dirty bits get set to true, then performance is no better than a regular array (list)
  
## Chaining:

* instead of probing you can "hang" another data struture off of each index
* Example: a linked list
* Or: you can use any data structure to store all elements that map to the same hash value (BST)
* Still the same problem: as more elements are stored in the data structures, it becomes no better than the data structures used

## Re-Hashing

* At some point performance will degrade: create a larger table
* REquires creating a new array and *rehashing* all of the elements into this new array
* Rehashing is generally $O(n)$ BUT it is not done very often 
* So over the lifetime of the data structure, the average performance is quite good and can be seen as $O(1)$ (amortized)
* Generally you use a *load factor* to decide when to rehash: $n / m$ where $n$ is the number of elements in the table, $m$ is the size of the table
  * Load factor: the percent that the table is full
  * Example: if the load factor reaches .75 (75% full), then rehash
  
* General:
  * Smaller table -> more collisions -> slower access/insert BUT less wasted space
  * Larger tables -> fewer collisions -> faster access/insert BUT more wasted space
  * Time/space tradeoff: you can make operations faster by using more memory, you can use less memory by making operations slower

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

```text










```


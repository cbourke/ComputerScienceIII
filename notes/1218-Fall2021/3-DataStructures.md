# Computer Science III
## CSCE 310 - Fall 2021
### Data Structures

## Review

* Binary Trees
  * Parent
  * Left/Right child
* Binary Search Trees
  * Key in the left child is < than the parent
  * Key in the right child is > than the parent
* Traversals:
  * Preorder: root-left-right manner
  * Inorder: left-root-right
  * Postorder left-right-root
  * BFS
* Heaps

### Huffman Coding

* Coding Theory:
  * Add redundancy to data (or a signal) to ensure that information is not lost over a noisy channel
  * Compression: want to *remove* redunant information or reduce information for efficient storage or transmission
  * zip files, rar, tar, etc.
  * MP4s, JPEG, PNGs - lossy compression: remove unnecessary data or approximate the data
  * Want: lossless compression/encoding: every piece of data is recoverable
  * Huffman Coding
    * English has a lot of redundancy; non-uniform distributions on letters
    * r, s, t, l, e are far more common than z, q
    * Idea: we won't encode letters using a fixed-length (block) encoding scheme (such as ASCII)
    * Instead: we'll encode common characters with a *shorter codeword* and less common characters with *longer* codewords (and omit any characters that don't even appear)

### Trees: A Review


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
* The *height* of a node $u$ in a tree denoted $h(u)$ is the length of the longest path to any descendent leaf
* Depth: measure with respect to the root
* Height: measure with respect to leaves
  * The height of a leaf is 0
  * The height of an empty tree is -1 (by convention)
  * The height of a tree itself is the height of its root node
* The *balance factor* of a node $u$ denoted $bf(u)$ is the height of its left-subtree minus the height of its right-subtree
  * A balance factor of 0 indicates a well-balanced subtree
  * A negative balance factor indicates the tree is unbalanced to the *right*
  * A positive balance factor indicates the tree is unbalanced to the *left*
* An AVL Tree is a binary search tree such that the balance factor of all nodes is -1, 0, 1
* Due to the balanced nature of an AVL tree, we have a guarantee that $d = O(\log{n})$
* Deletion:
  * Initially same as a regular BST:
  * A deletion may cause the subtree to be unbalanced
  * A rebalance cascade may propagate all the way back up to the root
  * Each rebalance/rotation is only $O(1)$
  * A deletion may end up being $O(d)$ but since it is balanced, $d = O(\log{n})$

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
* Searching a 2-3 tree: regular old search, instead of just left-right, you go left or center or right
* Insertion:
  * Always done in a leaf
  * If it is a 2-node, it becomes a 3-node
  * If it is a 3-node, you promote the middle key element up, potentially overflowing the parent
* Balanced BSTs: guaranteed $O(\log{n})$ insertion, search, deletion

## Hashing

* Offers *potential* for *amortized* constant-time operations

```c






```

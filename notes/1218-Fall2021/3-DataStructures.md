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

## Huffman Coding

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

## Trees: A Review


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

## Review: Heaps

* a min heap is a binary tree such that the key at every node is less than both its children
* A min heap has the fullness property: all nodes are present except for possibly the last level which is full to the left
* As a consequence:
  * The minimum element is always at the root
  * The fullness property ensures that the depth $d = O(\log{n})$
* Two operations become efficient ($O(\log{n})$):
  * getMin(): retrieve the root element, BUT you need to fix the heap
  * insert(): always insert at the "last" (next available) spot (last level, as far left as you can), heapify upward: swap with the parent until the heap property is satisfied



```c






```

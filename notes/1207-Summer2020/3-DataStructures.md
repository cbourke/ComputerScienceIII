
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






```text










```


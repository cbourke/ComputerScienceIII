
# Computer Science III
## CSCE 310H - Fall 2021
### Computation

## Introduction

Can Computers solve anything?

Consider the following statement:

"Algorithms Solve Problems"

* The statement is plain old English: dictionary words with dictionary definitions
* We need much more rigorous definitions and words in order to make the same statement

"Turing Machines Decide Languages"

## Languages

* Let $\Sigma = \{0, 1\}$ (alphabet)
* A string or word over $\Sigma$ is a finite sequence of symbols from $\Sigma$
  * `0` or `1`
  * `101010010`, `0000111`, `000`, `0000`
  * $\lambda$ is the empty string
* The set of all finite strings over $\Sigma$ is denoted as $\Sigma^*$
  $$\Sigma^* = \{\lambda, 0, 1, 00, 01, 10, 11, 000, \ldots \}$$
* A *language* is a subset $L \subseteq \Sigma^*$
* A language may be a finite set or an infinite set but all the strings it contains are *finite strings*

Claim: languages are equivalent to problems

* An instance of a *decision problem* involves a configuration of data (input) as well as a yes/no question
  * Given a graph $G$ is it acyclic or not?
  * Given an integer $x$ is it prime or not?
* Problems (inputs) can always be encoded in binary
* Example:  
$$L = \{ G | \textrm{$G$ is an acyclic graph}\}$$
* A graph $G$ would be a member of this set if it did not have a cycle; a graph $G$ would NOT be a member of this set if it did contain a cycle
* Given $G$, does it contain a cycle or not => Is $G \in L$ or $G\not\in L$
* We can then change the question/problem into a language question/problem:
* Encode a graph $G$ into binary: $\langle G \rangle$ (this is a binary encoding of a graph $G$)
* Define a language:
$$L = \{ \langle G\rangle | \textrm{$G$ is an encoding of an acyclic graph}\}$$
* $L$ consists of finite strings!  Each finite string $x \in L$ represents an acyclic graph $G$
* The finite strings that are NOT in $L$:
  * Encodings of graphs $G$ that contain a cycle or
  * Encodings that are invalid under whatever encoding scheme you came up with!
* Other types of problems (technical detail)
  * Optimization problems: Given a graph $G$ and two vertices, $x, y$ what is the length of the shortest path between them?
  * Encoding: $\langle G, x, y, k \rangle$: this encoding will be *in* the language if there exists a path $x$ to $y$ in $G$ of length $k$
  * Counting problems: Given a graph $G$ and two vertices, $x, y$ how many distinct paths are there from $x$ to $y$?  
  * Encoding: $\langle G, x, y, k \rangle$: this encoding will be *in* the language if there are $k$ paths between $x$ and $y$
  * Function problems: Given $G, x, y$ *output* the shortest path $x$ to $y$ (a sequence of vertices)
  * Encoding:
  $$\langle G, x, y, z\rangle$$
  Is $G$ a graph such that the shortest path from $x$ to $y$ contains $z$ as an intermediate vertex.

## Computational Models

* To start, we'll look at Finite State Automatons
* An FSA is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$
  * $Q$ is a set of finite *states*
  * $\Sigma$ is our alphabet
  * $\delta: Q \times \Sigma \rightarrow Q$
  * $q_0 \in Q$ is an initial state
  * $F \subseteq Q$ is a set of *accepting states*
* An FSA defines a language:
  * On an input $x \in \Sigma^*$ it transitions from the initial state to other stats depending on each bit
  * Read-once (read only)
  * once fully read, if the machine ends in an accept state, it accepts $x$, if in a reject state, it rejects
  * We say that an automaton $A$ decides a language $L$ if for all inputs $x$, it accepts if and only if $x\in L$

## Turing Machines

* A TM is a 7 tuple $(Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej})$
    * $Q$ is a finite set of states
    * $\Sigma$ is the input alphabet, $\Gamma$ is the output alphabet (they may be the same )
    * Transition function:
      $$\delta: Q \times \Sigma \times \Gamma \rightarrow Q \times \Gamma, \times \{L, R, -\}^2$$
    * $q_0$ is an initial state, $q_{acc}$ is an accepting state, and $q_{rej}$ is a rejecting state

* A Turing Machine decides a language $L$ if and only if it halts on all inputs and accepts/rejects if $x \in L$/$x\not\in L$
  * A TM only decides a language if it *halts on all inputs*!!!

* Are Turing Machines = Computers = Algorithms?
* Can Algorithms solve any problem? => Can Turing Machines decide any language?
* Answer: NO
* The Church-Turing Thesis: "Turing Machines = Algorithms"
* You can come up with problems (actual real, practical problems) such that no turing machine decides that language!


```text




```


# Computer Science III
## CSCE 310H - Fall 2022
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
* A string or word over $\Sigma$ is a finite sequence of symbols from $\Sigma$:
  * `0`, `1`
  * `101110101`, `0000`, `00`, `001`, `01`
  * Empty string: $\lambda$
* With repsect to strings, the basic operation is concatenation
  * Therefore, the "additive" identity is the empty string:
  * for any word, $w$, $w + \lambda = w = \lambda + w$
* The finite strings over a finite alphabet are countable:
  $$\Sigma^* = \{\lambda, 0, 1, 00, 01, 10, 11, 000, 001, \ldots\}$$
* A *language* is a subset $L \subseteq \Sigma^*$
* A language may be a finite set or it may be an infinite set
* BUT all the members or elements of a language are *finite strings*

### Languages = Problems

* An instance of a *decision problem* involves a configuration of data (input) as well as a yes or no question
  * Given a graph $G = (V, E)$ is it acyclic or not?
  * Given an integer, $x$ is it prime or composite?  
* Claim: languages are equivalent to problems
* Example:  
$$L = \{ G | \textrm{$G$ is an acyclic graph}\}$$
* You simply need to encode the problem using some binary encoding scheme
* We use the shorthand `\langle G \rangle`: $\langle G \rangle$ (this is an encoding of the graph $G$ in binary); $\LaTeX$ note: it is not the same as $<G>$
* Given $G$ does it contain a cycle or not means asking the question, $\langle G \rangle \in L$
* The finite strings that are NOT in $L$:
  * Encodings of graphs $G$ that contain a cycle or
  * Encodings that are invalid under whatever encoding scheme you came up with!
* Another decision problem: given $G, x, y$ where $x, y \in V$, does there exist a path from $x \rightsquigarrow y$
  * How would this be encoded?
  * $\langle G, x, y \rangle$
* Other types of problems (technical detail)
  * Optimization problems: Given a graph $G$ and two vertices, $x, y$ what is the length of the shortest path between them?
  * Encode $G, x, y$ and another value: $k$ and ask the question:
  Given $\langle G, x, y, k \rangle$: does there exist a path $x \rightsquigarrow y$ of length $k$?
  To find the lenght of the actual shortest path: ask different questions
    * $\langle G, x, y, 1 \rangle \in L$
    * $\langle G, x, y, 2 \rangle \in L$
    * $\langle G, x, y, 3 \rangle \in L$
  * Even better:
    * What is the largest possible value of $k$?  
      * If weighted: the sum of all weights
      * If non-weighted: $n-1$
    * If you have a lower bound: 1 *and* an upper bound of $W$
    * Then you can do even better: do a binary search for the "best" solution
* Functional problems:
  * Given a graph $G$ and two vertices $x, y$: want a list of vertices that represent the shortest path between them
  * Encode: $\langle G, x, y, z\rangle$: in the shortest length path from $x \rightsquigarrow y$ is $z$ the next vertex?
  * To build the path:
    * $\langle G, x, y, z\rangle$ for each $z$ until you get a yes
    * $\langle G, z, y, z'\rangle$ you repeat this series of questions until you've formulated a path

## Computational Models

* To start, we'll look at Finite State Automatons
* An FSA is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$
  * $Q$ is a set of finite *states*
  * $\Sigma$ is our alphabet
  * $\delta: Q \times \Sigma \rightarrow Q$
  * $q_0 \in Q$ is an initial state
  * $F \subseteq Q$ is a set of *accepting states*
* The transition function, $\delta$ takes the current state as well as the next input bit and then transitions to another state
* Input is read bit by bit (but only once and only one way) and transitions are made to other states
* If at the end of the input, you are in an accept state, you accept the input
* If at the end of the input, you are in an reject state, you reject the input
* A FSA defines a language by accepting strings: the language defined by a FSA is the set of all strings that it accepts
* Finite state automatons can only accept "regular languages" which can be defined using a *regular expression*
* However, many languages are NOT regular

## Turing Machines

* A TM is a 7 tuple $(Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej})$
    * $Q$ is a finite set of states
    * $\Sigma$ is the input alphabet, $\Gamma$ is the output alphabet (they may be the same )
    * Transition function:
      $$\delta: Q \times \Sigma \times \Gamma \rightarrow Q \times \Gamma, \times \{L, R, -\}^2$$
    * $q_0$ is an initial state, $q_{acc}$ is an accepting state, and $q_{rej}$ is a rejecting state
* A Turing Machine decides a language $L$ if and only if it halts on all inputs and accepts/rejects iff $x \in L$ or $x\not\in L$
* A TM only decides a language if it *halts on all inputs*!!!
* Are Turing Machines = Computers = Algorithms?
* The above is the "Church-Turing Thesis"?
* A programming language is "Turing complete" if it can express a program for any Turing Machine
* The real question: is there a Turing Machine (TM) for any and all possible languages?
* NO
* There are problems that have no algorithmic solutions
* THere are languages that are NOT decidable by any TM

### Diagonalization

* Using Cantor's Diagonalization proof we can show that TMs are *countable* but languages are *uncountable*
* There are some problems that are *undecidable* by a Turing Machine
* There are some problems that are *unsolvable* by an algorithm/computer
* Ex: Halting Problem

## Computational Complexity












```text









```

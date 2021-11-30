
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
* You can come up with problems (actual real, practical problems) such that no Turing machine decides that language!

### Diagonalization

* Using Cantor's Diagonalization proof we can show that TMs are *countable* but languages are *uncountable*

### Halting problem

* Halting Problem: given a TM $M$ and an input $x$ does $M(x)$ halt?
* Claim: no TM exists to decide the halting problem

## Computational Complexity

* *Given* an algorithm we can analyze its complexity (Big-O): $O(1), O(n), O(n^2)$ (all polynomial), $O(2^n)$ (exponential), etc.
* For Turing Machines:
  * In a TM "time" is measured by the number of transitions from one state to the next until you halt (and accept or reject)
  * In a TM "memory" is the number of tape cells used in the work tape
  * We can bound both time and memory by functions; $T(n), M(n)$
  * The size of the input, $n$ is the number of bits/symbols in the input tape
* You can bound the number of transitions by some function,
  $$T(n) \in O(f(n))$$
* This allows you to define *complexity classes*: $\mathsf{P}$ is *deterministic polynomial time*
* The complexity class $\mathsf{P}$ consists of all *problems* such that there is a deterministic Turing Machine that runs in polynomial time with respect to any input
  * $\mathsf{P}$ is a set of *problems* ie a set of *languages* NOT a set of algorithms
  * To show that a problem is in $\mathsf{P}$ you need to come up with a poly-time algorithm that solves/decides that problem!
  * Complexity classes are classes of PROBLEMS (langages) not algorithms
  * The existence of an algorithm *shows* that a problem is in $\mathsf{P}$ but..
  * If we didn't have any algorithm for a problem, we wouldn't know what complexity class it is in
  * Just because we don't know a polytime algorithm for a problem, doesn't mean it is *not* in $\mathsf{P}$!
  * Examples: finding the shortest path in a graph, computing a MST, sorting, etc. are all *problems* in P
  * To show that a problem is in $\mathsf{P}$ all you need to do is come up with an algorithm that runs in polynomial time
  * What is determinism?   ANy computation that has the same result on the same input is determinsitic

### Nondeterminisic Computation

* This is not "randommess", it is not a "real" computational model
* Nondeterminism is a *theoretical* model of computation
* It works in two phases:
  * Guessing phase: it guesses a solution to a given problem (nondetermistic phase)
  * Verification phase: given the guess, it verifies if it is a "valid" solution or not (if it is, it is known as a "certificate" or "witness")
  * The overall machine accepts if *any* possible computational branch/guess is valid
* Having a nondeterministic polynomial time Turning machine (algorithm) allows us to define $\mathsf{NP}$: nondeterministic polynomial time
* It consists of all problems such that there is a nondeterministic algorithm that solves it in polynomial time

### Comparison

* What is the relation between $\mathsf{P}$ and $\mathsf{NP}$?
* Trivially, by definition:
  $$\mathsf{P} \subseteq \mathsf{NP}$$
* Any problem that can be solved in deterministic polynomial time can be solved in nondeterministic polytime by simply ignoring the nondeterminisitc phase
* Observation: if you use an *exponential* amount of time, you can always simulate a polynomial amount of nondeterminism:
  $$\mathsf{NP} \subseteq \mathsf{EXP}$$
* The million dollar question:
$$\mathsf{P} = \mathsf{NP}?$$
* Most think not:
  $$\mathsf{P} \neq \mathsf{NP}$$
* Ie there are problems that are *not solvable* by *any* deterministic polytime algorithms!
* Are there problems that are inherently more difficult than other problems?
* To answer this question, we need a framework for comparing the relative difficulty of problems
* We already have a framework to compare the relative complexity of *algorithms*



```text







```

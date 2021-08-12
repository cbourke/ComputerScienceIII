
# Computer Science III
## CSCE 310 - Summer 2021
### Computation

## Introduction

Consider the following statement;

"Algorithms Solve Problems"

* The statement is plain old English: dictionary words with dictionary definitions
* We need much more rigorous definitions and words in order to make the same statement

"Turing Machines Decide Languages"

## Languages

* Let $\Sigma = \{0, 1\}$ (alphabet)
* A string or word over $\Sigma$ is a finite sequence of symbols from $\Sigma$
  * `0`, `1`, `101101010`, `0000001`
  * $\lambda$ is the empty string
* A set of all finite strings over $\Sigma$ is denoted as $\Sigma^*$
  $$\Sigma^* = \{\lambda, 0, 1, 00, 01, 10, 11, 000, \ldots \}$$
* A *language* is a subset of $L \subseteq \Sigma^*$
* A language may be finite or infinite, but the strings it contains are all finite

Claim: languages are equivalent to problems

* An instance of a *decision problem* involves a configuration of data (input) as well as a yes/no question
  * Given a graph $G$ is it acyclic or not?
  * Given an integer $x$ is it prime or not?
* Problems can be encoded as binary
  $$\{ G | \textrm{$G$ is an acyclic graph}\}$$
* All you do is encode the input: $G \rightarrow \langle G\rangle$
* "Is $G$ acyclic" $\rightarrow$ is $\langle G\rangle \in L$ where
  $$\{ \langle G\rangle | \textrm{$G$ is an acyclic graph}\}$$
* $x \in L$ if $x$ validly encodes a graph $G$ that contains no cycles otherwise $x \not\in L$
* Other types of problems can also be encoded as a language:
  * Optimization Problems: to make the problem into a decision problem (yes/no problem), you can always encode additional information:
    $$\langle G, x, y, k\rangle$$
  Is $G$ a graph that has a path from $x$ to $y$ of length $k$?
  * Functional Problems: suppose you know there is a shortest/longest path, you want to *output* the that path
    $$\langle G, x, y, z\rangle$$
  Is $G$ a graph such that the shortest path contains an intermediate vertex $z$?

## Computational Models

* To start, let's look at a very simple model: Finite State Automatons
* An FSA is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$
  * $Q$ is a set of finite *states*
  * $\Sigma$ is our alphabet
  * $\delta: Q \times \Sigma \rightarrow Q$
  * $q_0 \in Q$ is an initial state
  * $F \subseteq Q$ is a set of *accepting states*
* A FSA defines a language:
  * On input $x$, it reads bit by bit and transitions a state for each input bit.  
  * When the input is fully read, it ends in some state
  * IF that state is accepting, the string is in the language defined by the FSA
  * If that state is accepting, the string is NOT in the language

## Turing Machines

* A TM is a 7 tuple $(Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej})$
    * $Q$ is a finite set of states
    * $\Sigma$ is the input alphabet, $\Gamma$ is the output alphabet (they may be the same )
    * Transition function:
    $$\delta: Q \times \Sigma \times \Gamma \rightarrow Q \times \Gamma, \times \{L, R, -\}^2$$
    * $q_0$ is an initial state, $q_{acc}$ is an accepting state, and $q_{rej}$ is a rejecting state

* A Turing Machine decides a language $L$ if and only if it halts on all inputs and accepts/rejects if $x \in L$/$x\not\in L$

* Can Computers/Algorithms/Turing Machines solve any problem?
* Can Turing Machines decide any (and all) languages?
* NO.
* There are languages such that no Turing Machine exists that decides them.

### Diagonalization

* Observe: all TMs $M$ have a finite (binary string) representation, $\langle M \rangle$
* All TMs can be enumerated
* All languages *cannot* be enumerated
* The set of all TMs is countable
* The set of all languages is uncountable
* There are languages that have no TM that decides them

## The Halting Problem

* Are there *practical* problems that no algorithm can solve (*for all inputs*)?
* Halting Problem: given a TM $M$ and an input $x$ does $M(x)$ halt?
* Claim: no TM exists to decide the halting problem
* Rice's Theorem: in general, given a TM $M$ answering any non-trivial property of the language decided by $M$ is not decidable

### Complexity Classes

* Among problems that *are* solvable (decidable): which ones are "easily" solve and which are "hard" to solve?
* In a TM, an elementary operation is a transition from one state to another (time)
* In a TM, the number of output tape cells written to can be considered its memory resource (memory)
* For a TM, the input size is the number of bits in the input, $|x| = n$
* You an say that a TM takes
  * $T(n)$ time and
  * $Mem(n)$ memory
* You can then bound the number of transitions by a polynomial (or really any other function):
  $$T(n) \in O(p(n))$$
* This allows you to define *complexity classes*: $\mathsf{P}$ is *deterministic polynomial time*
* $\mathsf{P}$ consists of all problems (languages) that are decidable by a deterministic polynomial time TM
* Examples: finding the shortest path in a graph, computing a MST, sorting, etc. are all *problems* in P
* To show that a problem is in $\mathsf{P}$ all you need to do is come up with an algorithm that runs in polynomial time
* What is determinism?   ANy computation that has the same result on the same input is determinsitic

### Nondeterministic Computations

* It is not a "real" computational model; it is a theoretical one
* All nondeterminisitc algorithms have two phases:
  * Guessing phase: guess a solution (in nondeterministic polynomial time)
  * Verify the solution: accept if it is valid (making the guess a "certificate")
  * Overall the machine accepts if at least one computational path accepts
* The set of all languages $L$ that are decidable by a nondeterministic polynomial time Turning Machine is called $\mathsf{NP}$
("nondeterminisitic polynomial time")

### Comparison

* THe $\mathsf{P}$ vs $\mathsf{NP}$ problem asks: is
$$\mathsf{P} = \mathsf{NP}$$
or not?
* Most believe they are not equal: that an exponential amount of determinisitic time is *required* to simulate non-determinisim
* It is easy to see that  
$$\mathsf{P} \subseteq \mathsf{NP}$$
* Most think that there are problems that are in $\mathsf{NP}$ that do not have a determinisitic polynomial time solution

### Reductions

* Goal: we want to establish the relative complexity of problems (NOT algorithms)
* RElative complexity of algorithms can be done with big-O analysis
* We want to deal with *problems* (languages), not algorithms
* In general: you can use or adopt a (supposed) solution for one problem $B$ to solve another problem $A$
  * $A$ is no more complex than $B$
  * $A$ is no harder to solve than $B$
  * $B$ is just as complex (or even more complex or "hard to solve") than $A$ is
  * We are NOT making $A$ simpler
  * We are "reducing" $A$ to $B$
  * "I don't know how to solve $A$ but if I know how to solve $B$ I could solve $A$ so I've reduced the problem of solving $A$ to the problem of solving $B$ "
  * $A \leq_{P} B$

### Motivating Example

* Essentially reductions use other algorithms to solve other problems


### Polynomial Time Mapping Reductions

* Ultimately we want to map input instances of one problem to input instances of another problem
* We only want to use the power of polynomial time deterministic algorithms to compute our mapping
* We don't want to "cheat" by hiding the complexity in the reduction itself
* Definition: Let $P_1$ and $P_2$ be problems.  We say that $P_1$ reduces to $P_2$ and write
  $$P_1 \leq_{\mathsf{P}} P_2$$
if there exists a function $f$ such that
  * $f$ maps all yes instances of $P_1$ to yes instances of $P_2$ (no instances likewise)
  * and $f$ is computable by a deterministic polynomial time algorithm
* A problem is in the complexity class $\mathsf{NP}$ if it is decidable by a nondeterministic polynomial time TM
* A problem is $\mathsf{NP}$-complete if *every problem* in $\mathsf{NP}$ reduces to it
* Fact: (Cook/Levin): the SAT problem is $\mathsf{NP}$-complete
* WHy is this useful: it gives us a framework for establishing the relative difficulty of problems
* Showing that a problem is $\mathsf{NP}$-complete gives you evidence that it is very difficult and to solve it you should look at heuristics/other methods
* It gives us a way to understand $\mathsf{P}$ and $\mathsf{NP}$: if we can show even ONE polynomial time algorithm for ONE $\mathsf{NP}$-complete problem: then we've collapsed the entire landscape

### Proving $\mathsf{NP}$-completeness

* 5 step process: you want to show that a problem $P$ is $\mathsf{NP}$-complete

1. Show that $P$ is in $\mathsf{NP}$: by coming up with a nondeterministic polytime algorithm for it
2. You select a known $\mathsf{NP}$-complete problem to reduce *from* to your problem $P$
3. You come up with a mapping reduction that maps yes instances of the $\mathsf{NP}$-complete problem to yes instances of your problem $P$
4. You prove your reduction is correct (it preserves solutions)
5. You show that your reduction is computable in deterministic polynomial time

### Reduction from SAT to Clique

1. Show that the clique problem: given a graph $G$ and an integer $k$, does $G$ have a clique of size $k$ or not? is in $\mathsf{NP}$
2. Select a known $\mathsf{NP}$-complete prolbem to reduce FROM: SAT (3-CNF)
3. Define a reduction: given a 3-CNF formula, we want to produce a graph such that the formula is satisfiable if and only if the graph has a clique of a certain size:
  * Given a 3-CNF formula with $k$ clauses, $C_1 \wedge C_2 \wedge \cdots \wedge C_k$ with each clause having 3 variables or their negation
  * Create a graph $G$:
  * there will be $3k$ vertices, one for each literal in each clause
  * Edges: draw an edge between two vertices if
    - they are in different clauses and are
    - *consistent*: they are not the negation of each other
4. Prove the reduction is correct: formula is satisfiable if and only if $G$ has a clique of size $k$
5. Show the reduction can be computed in determinisitic polynomial time:
  * outputting $3k$ vertices
  * outputting at most $3k \choose 2$ edges
  * both are polynomial in $k$ the number of clauses which is bounded by $n$, the number of variables

## Reduction Examples

####  Vertex Cover

Given: a graph $G=(V,E)$ and an integer $k$, does there exist a vertex cover $V' \subseteq V$ of size $|V'| = k$?

A *vertex cover* is a set of vertices such that every edge has at least 1 end point in $V'$; the set of vertices "covers" all the edges:
  $$\forall e=(x, y) \in E [ x \in V' \vee y \in V']$$

1. Show that vertex cover is in $\mathsf{NP}$
2. select a known $\mathsf{NP}$-complete problem to reduce *from*: Clique
3. Need to come up with a reduction from an instance of clique to an instance of vertex cover:
  $$\langle G, k\rangle \rightarrow \langle \overline{G}, n-k\rangle$$
4. G has a clique of size $k$ if and only if $\overline{G}$ has a vertex cover of size $n-k$.  Proof?
5. The mapping is computable in determinisitic polynomial time


```text












```

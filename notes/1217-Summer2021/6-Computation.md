
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

```text







```

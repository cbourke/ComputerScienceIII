
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

* Given an algorithm, you can analyze its complexity using Big-O analysis
  * Selection Sort: $O(n^2)$
  * Quick Sort: $O(n\log{n})$
  * Both of these are algorithms that solve the "sorting problem"
* For Turing Machines:
  * "Time" is measured by the number of transitions from one state to another for a given input before it halts (and accepts or rejects)
  * "memory" is measured with respect to the amount of "work tape" used in the computation of an input
  * The input size of a Turing Machine is the number of bits in the input tape: $x$, $|x| = n$ (the length of the input $x$)
* It makes sense to bound a Turing Machine just like an algorithm:
  * $T(n) = O(f(n))$ is a time bound on the running time of a Turing Machine
* This allows us to define *complexity classes*
  * NOTE: complexity classes are with respect to *problems* NOT algorithms!
  * Algorithms are proof that a problem lies within a complexity class!
* The complexity class *deterministic polynomial time*, denoted $\mathsf{P}$ is the class of all problems such that there exists a deterministic TM that decides the problem
* $\mathsf{P}$ is the set of all languages that are *decidable* by a deterministic TM that runs in polynomial time, $f(n) \in O(n^k)$
  * Example: Is the sorting problem in $\mathsf{P}$?
  * Yes: the existence of selection sort/quick sort proves that you can solve the problem in polynomial time
  * 0-1 Knapsack problem: is that in $\mathsf{P}$? Who knows, no one has come up with a polytime algorithm for it (yet).
* Another complexity class: $\mathsf{EXP}$ are all languages decidable by a TM that runs in *exponential time*: $f(n) \in O(2^n)$
  * Is the sorting problem in $\mathsf{EXP}$?  Yes
  * Is 0-1 Knapsack in $\mathsf{EXP}$?  Yes
* Observation:
  $$\mathsf{P} \subseteq \mathsf{EXP}$$
* Keep in mind that these complexity classes are *sets of languages*

### Nondeterminisic Computation

* This is not "randomness", it is not a "real" computational model
* Nondeterminism is a *theoretical* model of computation
* Nondeterminism works in two phases:
  * Guessing Phase: it guesses a solution to a given problem nondeterministically (polynomial time)
  * Verification phase: given the guess, it verifies if it is a "valid" solution or not (if it is a valid solution, the solution is called a "certificate") also has to be polynomial
  * Overall, a nondeterministic TM accepts an input if *any* possible computational branch or guess is a valid certificate


## Reductions

* Goal: we want to establish the relative complexity of problems (*not* algorithms)
* Definition: Let $P_1$ and $P_2$ be problems (languages).  We say that $P_1$ reduces to $P_2$ and write
  $$P_1 \leq_{\mathsf{P}} P_2$$
if there exists a function $f$ such that
  * $f$ maps all yes instances of problem $P_1$ to yes instances of $P_2$
  * $f$ is computable in deterministic polynomial time $\mathsf{P}$ (subscript)
* Interpretation:
  * These are "mapping" reductions: they map one problem to another
  * If you have a solution to problem $P_2$ then you have a solution to $P_1$
* Interpretation: if $P_1 \leq_{\mathsf{P}} P_2$:
  * $P_1$ is no more difficult/hard/complex tan $P_2$
  * $P_2$ is *at least* as difficult/hard/complex as $P_1$
  * It *could* be that they have an equal complexity
  * It *could* be that $P_2$ is *strictly* harder/more complex (but we don't know)
* Observations:
  * "Reduction" is not reducing complexity; it is not making things "easier"
  * "Reduction" simply means you are translating or mapping one problem to another
  * ONLY IF you have a solution to the second problem, do you have a solution to the first
  * If you have a solution to the first problem and a reduction to the second problem: who cares?  It does not give you a solution to the second problem
  * The power of the reduction (the mapping) CANNOT be more powerful than the problems themselves
    * Ex: if the reduction itself (mapping) were allowed an exponential amount of time $\mathsf{EXP}$, then you could solve any problem in exponential time and "cheat" on the reduction
  * Possible: you end up reducing multiple problems into one

### Completeness

* A problem $P$ is in the complexity class $\mathsf{NP}$ if it is decidable by a nondeterministic polynomial time TM
* A problem $A$ is $\mathsf{NP}$-complete if *every problem* in $\mathsf{NP}$ reduces to it!
  * Every problem in $\mathsf{NP}$ reduces to it
  * It reduces to any other $\mathsf{NP}$-complete problem!
* Observation: if you have a solution to even a *single* $\mathsf{NP}$-complete problem, you have a solution to *every* $\mathsf{NP}$ problem!
* Observation: if your so-called solution, runs in deterministic polynomial time, then you've shown that $\mathsf{P} = \mathsf{NP}$
* However, it is very unlikely that is the case, more likely is that $\mathsf{P} \neq \mathsf{NP}$
* Examples of $\mathsf{NP}$-complete
  * 0-1 Knapsack Problem
  * Hamiltonian Path/cycle problem
  * Satisfiability
  * Hundreds of others
* To prove a problem is $\mathsf{NP}$-complete, you need a starting point: you need to establish the *first* $\mathsf{NP}$-complete problem
  * Suppose $L_\mathsf{NP}$ is $\mathsf{NP}$-complete.
  * EVERY problem in $\mathsf{NP}$ reduces to $L_\mathsf{NP}$
  * If you want to show a different problem, $B$ is $\mathsf{NP}$-complete it is enough to show:
    $$L \leq_{\mathsf{P}} B$$
* Starting Point: Satisfiability: Cook-Levin first showed that a "canonical" $\mathsf{NP}$-compelete problem reduced to satisfiabiliity:
$$L_\mathsf{NP} = \{ \langle M, x \rangle | M \text{ is a nondeterministic Turming machine that accepts x in a polynomial amount of time}\}$$
* Cook Levin Showed:
  $$L_\mathsf{NP} \leq_{\mathsf{P}} SAT$$
* Reduce SAT to the Clique problem




```text









```

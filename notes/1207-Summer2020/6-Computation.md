
# Computer Science III
## CSCE 310 - Summer 2020
### Computability

## Introduction

Consider the following statement:

"Algorithms Solve Problems"

* This statement is intuitive but plain old English
* It is not mathematically rigorous at all
* Above is a *dictionary* definition of each word
* We need a better (more rigorous) mathematical statement:

"Turing Machines Decide Languages"

## Languages

* Let $\Sigma = \{0, 1\}$ (alphabet)
* A string or word over $\Sigma$ is a finite sequence of symbols from $\Sigma$; Examples:
  * `0`, `1`, `10100010101`, `0000001`
  * $\lambda$ is the "empty string"
* The set of all finite strings over $\Sigma$ is denoted as $\Sigma^*$
* A *language* is a subset $L \subseteq \Sigma^*$

Claim: languages are equivalent to problems

* An instance of a *decision problem* involves a configuration of data (input) as well as a yes/no question
  * Given a graph $G$ is it acyclic or not?
  * Given an integer $x$ is it prime or not?
* You can define a language the encodes or models a problem and then your decision question becomes: given an input $x$ is it in the language or not?
  * $x$ is a yes instance if $x \in L$
  * $x$ is a no instance if $x \not\in L$
* Examples:
  $$\{ G | \textrm{$G$ is an acyclic graph}\}$$ 
* To reconcile a problem with our definition: take a problem and turn it into a language, we need an *encoding*
* Given (say) a graph $G$, you can produce an encoding $\langle G \rangle$ of the graph $G$
* You do this all the time: any problem can be encoded in binary, thus problems are the same thing as languages
$$\{ \langle G\rangle | \textrm{$G$ is an acyclic graph}\}$$ 
* Technical note: all invalid encodings are ignored (not in the language)
* Given a language $L$ and an input string $x$, "solving" the language simply means determining whether or not $x$ is in $L$
* These definitions/terminology only take care of decision problems: problems that have a yes or no answer
  * Optimization problems: what is the value of the MST of $G$ (output: a number)
  * Functional problems: you not only want to know if there is a Hamiltonian path or not, but if so, what is it (output: a path)
* Consider the following language:

$$\{ \langle G, w\rangle | \textrm{$G$ is a graph whose MST has a weight of at most $w$}\}$$ 

## Computational Models

* To start, let's consider a simple *Finite State Automaton* 
* An FSA is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$
  * $Q$ is a set of finite *states*
  * $\Sigma$ is our alphabet
  * $\delta: Q \times \Sigma \rightarrow Q$
  * $q_0 \in Q$ is an initial state
  * $F \subseteq Q$ is a set of *accepting states*
* A FSA defines a language: 
  * On an input string $x$, it reads it bit by bit and transitions to a new state according to $\delta$
  * If at the end of the input string the machine is in an accept state, we accept the string and say that $x \in L_A$
  * If at the end of the input string, 
  the machine is in a reject state, we reject the input and say that $x \not\in L$
  * The input is read-only, one-way read only (you cannot reverse the reading)
  * No extra storage (memory) or data structure
  * Extremely simple (but still powerful) model of computation
* A finite state machine *decides* a language if it:
  1. Always terminates on any input and
  2. For all inputs $x \in L$ it accepts and for all inputs $x \not\in L$ it rejects

## Turing Machines

* A TM is a 7 tuple $(Q, \Sigma, \Gamma, \delta, q_0, q_{acc}, q_{rej})$
  * $Q$ is a finite set of states
  * $\Sigma$ is the input alphabet, $\Gamma$ is the output alphabet (they may be the same )
  * Transition function:
  $$\delta: Q \times \Sigma \times \Gamma \rightarrow Q \times \Gamma, \times \{L, R, -\}^2$$
  * $q_0$ is an initial state, $q_{acc}$ is an accepting state, and $q_{rej}$ is a rejecting state

* A Turing Machine decides a language $L$ if and only if it halts on all inputs and accepts/rejects if $x \in L$/$x\not\in l$

## Computability

* "Can TMs solve any problem?"
* "Can TMs decide any language"
* Absolutely NOT
* There are languages, interesting languages that you can *prove* no TM exists to solve them/decide them
* Example: No TM exists to solve the *halting problem*
* Halting Problem: Given a TM $M$ and an input $x$, does $M(x)$ halt?  

### Proof

* Claim: no TM $H$ exists that given $M, x$ outputs whether or not $M(x)$ halts
* By way of contradiction: assume that such a machine $H$ exists
* $H(\langle M,x \rangle)$:
  * halt and accept (output 1) if $M(x)$ halts
  * halt and reject (output 0) if $M(x)$ does not halt
* Consider running a machine on itself: $M(M)$ or using an encoding, $\langle M, M \rangle$
  * Not that weird to run a program on itself: OS's run programs
  * Emulators 
* Now let's make another TM: $Q$ that takes one input (another TM)
* $Q(\langle M \rangle)$:
  * halt and accept if $H(\langle M, M \rangle) = 0$
  * go into an infinite loop if $H(\langle M, M \rangle) = 1$
* Now, run $Q$ on itself: $Q(Q)$
* $Q(\langle Q \rangle)$:
  * halt if $H(\langle Q, Q \rangle) = 0$
  * does not halt if $H(\langle Q, Q \rangle) = 1$
* Contradiction!
* No such machine $H$ can exist for all TMs and for all inputs $x$
* Rice's Theorem: in general, given a TM $M$ answering any non-trivial property of the language decided by $M$ is not decidable 

### Another perspective

* Observe: all TMs $M$ have a finite (binary string) representation, $\langle M \rangle$
* All TMs can be enumerated
* All languages *cannot* be enumerated
* The set of all TMs is countable
* The set of all languages is uncountable
* There are languages that have no TM that decides them
* Turing's proof is essential: "I am lying"

### Complexity Classes

* In a TM the elementary operation is a transition to a new state ("clock tick" or "time stamp")
* In a TM the amount of memory used is equal to the number of tape cells written/rewritten
* In a TM the input size is the size of the input string, $x$: $|x| = n$
* You can say that a TM takes
  * $T(n)$ time and
  * $M(n)$ memory
* If you can bound the number of transitions by a polynomial:
  $$T(n) \in O(p(n))$$
for all inputs $x$ then you can say that the machine is a *deterministic polynomial time* Turing Machine
* The set of all languages that are decidable by a deterministic polynomial time Turing Machine is denoted as $\mathsf{P}$
* What is determinism? any computation that on the same input has the same computation and same output

### Nondeterministic Computations

* Nondeterminism is not a "real" computational model; it is a theoretical one
* What is the computational power of quantifiers: $\exists, \forall$
* A nondeterministic algorithm has two phases:
  * Guessing phase: guess a solution to the input
  * Verification phase: verify that the solution is correct
* A nondeterministic Turning Machine will accept the input $x$ if *any* of its possible computation guesses accepts
* If both phases operate in polynomial time, we say that it is a nondeterministic polynomial time Turning Machine
* The set of all languages $L$ that are decidable by a nondeterministic polynomial time Turning Machine is called $\mathsf{NP}$
("nondeterminisitic polynomial time") 

### Comparison

* Is nondeterminism more powerful than determinism?
* What is the relationship between $\mathsf{P}$ and $\mathsf{NP}$?
* Observation: any nondeterministic polytime computation can be *simulated* with an exponential amount of deterministic time
* With respect to polynomial time, we can observe:
  $$\mathsf{P} \subseteq \mathsf{NP}$$
* Is nondeterminism *more* powerful than determinism?
  $$\mathsf{P} \subsetneq \mathsf{NP}$$
ie $\mathsf{P} \neq \mathsf{NP}$
* Is nondeterminism *equivalent* to determinism?
  $$\mathsf{P} = \mathsf{NP}$$

### Reductions

* Goal: we want to establish the relative complexity of problems
* Relative complexity of algorithms can be done easily with algorithm analysis 
  * Quicksort is better than selection sort
  * Algorithms only establish an *upper bound* on the complexity of a problem
  * Coming up with algorithms is difficult
  * How do you know that no algorithm exists
  * How do you know that no *better* algorithm exists
* Complexity classes model resources that Turing Machines use
* Establishing the relative inherent complexity of a problem requires another framework: reductions
* In general: if you can use or adapt a (supposed) solution for problem $B$ to solve another problem, $A$ then:
  * $A$ is no more complex than $B$
  * $A$ is no harder to solve than $B$
  * $B$ is just as complex (but it could be even more complex) than $A$
  * $A$ *reduces* to $B$
  * NOT making $A$ simpler
  * Intuitively you are "reducing" an "easier" problem to a "harder" problem
  * "I don't know how to solve $A$, but if I 
  could solve $B$ I could solve $A$, so I've reduced the problem of
  solving $A$ to the problem of solving $B$"

### Motivating Example

* Essentially reductions are using solutions (algorithms or functions) to solve other problems

### Polynomial Time Reductions

* Let $P_1$ and $P_2$ be problems.  We say that $P_1$ reduces to $P_2$ and write 
  $$P_1 \leq_{\mathsf{P}} P_2$$
if there exists function $f$ such that 
  * $f$ maps all yes instances of $P_1$ to yes instances of $P_2$ (no instances likewise)
  * and $f$ is computable by a deterministic polynomial time algorithm

* A problem is $\mathsf{NP}$-complete if *every problem* in $\mathsf{NP}$ reduces to it
* Fact: (Cook/Levin): the satisfiability problem is $\mathsf{NP}$-complete

### Proving $\mathsf{NP}$-completeness

* 5 step process: you want to show that a problem $P$ is $\mathsf{NP}$-complete

1. Show that $P$ is in $\mathsf{NP}$: by coming up with a nondeterministic polytime algorithm for it
2. You select a known $\mathsf{NP}$-complete problem to reduce *from* to your problem $P$
3. You come up with a mapping reduction that maps yes instances of the $\mathsf{NP}$-complete problem to yes instances of your problem $P$
4. You prove your reduction is correct (it preserves solutions)
5. You show that your reduction is computable in deterministic polynomial time

* Reductions are useful:
  * a single polytime algorithm for any $\mathsf{NP}$-complete problem implies that $\mathsf{P} = \mathsf{NP}$
  * Showing that a problem is $\mathsf{NP}$-complete means you've shown it is very difficult to solve

### Reducing SAT to Clique

1. Show that the clique problem: given a graph $G$ and an integer $k$, does $G$ have a clique of size $k$ or not? is in $\mathsf{NP}$
2. Select a known $\mathsf{NP}$-complete prolbem to reduce FROM: SAT (3-CNF)
3. Define a reduction:
  * Given a 3-CNF formula with $k$ clauses, $C_1 \wedge C_2 \wedge \cdots \wedge C_k$ with each clause having 3 variables or their negation
  * Create a graph $G$:
  * Vertices: $3k$ vertices, one for each literal in each clause
  * Edges: draw an edge between vertices if they are in different clauses and are *consistent* (they are not the negation of each other)
4. Prove that the reduction is correct: $\phi$ is satisfiable if and only if $G$ has a clique of size $k$
5. Show that the reduction is computable by a deterministic polynomial time algorithm

## Reduction Examples

#### Independent Set

Given: a graph $G=(V,E)$ and an integer $k$, does there exist an independent set $I \subseteq V$ of size $|I| = k$?

An *independent set* is a set of vertices such that no two vertices are connected by an edge:
  $$\forall x, y \in I [(x,y) \not\in E]$$

####  Vertex Cover

Given: a graph $G=(V,E)$ and an integer $k$, does there exist a vertex cover $V' \subseteq V$ of size $|V'| = k$?

A *vertex cover* is a set of vertices such that every edge has at least 1 end point in $V'$; the set of vertices "covers" all the edges:
  $$\forall e=(x, y) \in E [ x \in V' \vee y \in V']$$
  
```text









```

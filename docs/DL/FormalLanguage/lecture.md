# Lectures

## Language Model and Formal Language

ACL tutorial 4

big promises

- understanding reasoning abilities
- generalization ablities
- inductive bias
- tractability
- algorithms
- connect phenomena to human languages

neural language models - expressiblity - formal language

useful tools
- RNN: sequntial automata
- Transformer: circuits

Definition

a language model p is a distribution on *\Sigma. 

Two language models are equal if p(y) = q(y) for all y on *\Sigma. 

Any language model can be written as an autogressive one.

tightness: for arbituary language model, the sum of all p(y) < 1 can happen. If the sum of all p(y) = 1, it is tight.

A minimum non-tight example: To set the probablity of EOS as 0, thus the generation might never stop.

special features of automaton: parity, hierachy detection

simplist RNN: Elman RNN

RNNs can be both as language models / recognizors (to classify grammatical or not)

RNNs work like language model (TODO: photo)

infinite state automata - with unbounded precision and computation time

a turing machine is equivalent to a two-stack pushdown automaton. (tape = two-stacks)

Theorem: an infinite-precision RNNs with unbounded computation time are Turing complete.

implies:
- TODO: photo
- we need the hidden states to encode the stacks

stack = neuron

drawbacks: 
- numbers are in finite precision
- RNNs stop within finite time


## improvement theoretical model: RNNS with bounded computation time and finite precision

Theorem: Finite-precision real-time RNNs are equivalent to FSAs (without stacks, taking the training and inference procedure apart. )

clear:
- any finite-precision RNN will define a finite number of states
- it can thus be represented by a FSA
- an upper bound RNNs can do at most what finite-state automata can

=> Elman RNNs can simulate deterministic FSAs (any non-deterministic FSA can be => deterministic ones)

main differences:
- automaton: tabular rules
- RNNs: matrix multiplications

Any simple family of automata can efficient simulation of RNNs?

TODO: photo

Some FSA with |Q| states can be compressed into an RNN with O(log|Q|) hidden states.

Takeaways:

- stacks can be represented by linear functions.
  
an RNN can end up in any rung of the NC hierarchy depending on 
- whether allowing unbounded processing time
- whether allowing unbounded precision

QAs:

- RNNs poor trainability leads to poor performance on learning recursivity.


## How to turn an RNN into a classifier

the missing bit: 

probablistic finite-state automata also compute probalisties

Beyond Binary States: LSTMs and counting

Counter machine: 

TODO: photo, position on NC hierarchy

no model currently reach the computation ability of Turing machine. Some advanced models (e.g. ChatGPT) happen to recognize some programs.


LSTM as a counter machine, the memory cell works as the counter. set (TODO: some parameters) as 1 and the updating function of mem cells are as the counter.


## Transformers and formal language theory, part on encoder

bolean circuits, definition:

- directed: acyclicle computational graph
- input: binary (0 or 1)
- nodes: basic boolean functions
- output: binary (0 or 1)

runtime without parallelism

definition (depth): longest path from input to output
runtime with parallelism (?)


need sth dependent on input time

formal models: Boolean circuits

- AC^0
- TC^0
- NC^1

(what is ACC here)

formal models: first order logic (how did this appear)

TODO: photo, NC hierarchy interact with language classes

does circuits recognize parity? 

decisions to make: attention, softmax

uniformity: 

dependence on
- number of parameters


unique hard attention: 

linear temporal logic

TODO: photo on example of L=\Sigma\*ab\Sigma\*


## adding sequentiality to Transformers, chain-of-thought, part of decoder

- during training get all the sentence all at once
- during inference, one token at a time


so far, only deterministic automata

non-deterministic

takeaways
- 


QAs
- the Turing machines can move head left-to-right and right-to-left. if taking that into account, we might
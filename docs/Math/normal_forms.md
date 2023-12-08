# 各种Normal Forms

## Conjunctive Normal Form (CNF)

conjunction of one or more clauses

```
(A or ~B or ~C) and (~D or E or F)
```

## Disjunctive Normal Form

```
（A and ~B and ~C）or (~D and E and F)
```

## Algebraic Normal Form

one more terms are combined into terms by AND, and one more terms are combined by XOR

```
a XOR b XOR (a AND b) XOR (a AND b AND c)
```

## Negation Normal Form (NNF)

if the negation operator is only applied to variables and the only other allowed Boolean operators are conjunctions and disjunctions

```
~A and B
```

## Chomsky Normal Form

formal language theory 假的

```
A → BC
A → a
S → ε
```

[Category:Normal forms (logic)](https://en.wikipedia.org/wiki/Category:Normal_forms_(logic))
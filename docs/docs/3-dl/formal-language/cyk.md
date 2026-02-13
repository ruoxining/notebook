# CYK Algorithm

Cocke-Younger-Kasami algorithm (CYK/CKY) is a parsing algorithm for context-free grammars. 

## Algorithm

Let `w` be the `n` length string to be parsed. `G` represents the set of rules in the grammar with a starting state `S`. Suppose the index starts from 1.

- Construct a table: DP for size `n * n`.
- Boarder case: If `w=e` (empty string) and `S -> e` is a rule in G then we accept the string else we reject.
- Find a terminal for each leaf:
    for i = 1 to n:
        for each variable A:
            we check if A -> b is a rule and b = w_i for some i, if so place A in cell [n, i] in table.
- Annotate possible rule for each node:
    for l = 2 to n:
        for i = 1 to n-l+1:     # from the first node to the most distant node that the current length can reach)
            j = i+l-1           # the most distant node
            for k = i to j-1:   # for each future node
                for each rule A -> BC:
                    we check if (i, k) cell contains B and (k+1, j) cell contains C, if so we put A in cell (i, j) in table.

- Decide if the top node `S`.

## Example

Given a sentence `baaba` and a grammar

```
S -> AB | BC
A -> BA | a
B -> CC | b
C -> AB | a 
```

TODO


## Efficiency

The importance of CYK algorithm stems from its efficiency. It is obvious from the pseudocode that the time complexity is $$O(n^3 \dot |G|)$$, where $$|G|$$ is the number of rules in the grammar.

## References

- [Wikipedia - CYK algorithm](https://en.wikipedia.org/wiki/CYK_algorithm#:~:text=In%20computer%20science%2C%20the%20Cocke,Schwartz.){target="_blank"}
- [CYK Algorithm for Context Free Grammar](https://www.geeksforgeeks.org/cyk-algorithm-for-context-free-grammar/){target="_blank"}

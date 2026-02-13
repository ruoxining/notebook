# Backtracking 回溯

Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate (backtracks) as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## Pseudocode

In order to apply backtracking to a specific class of problems, one must provide the data `P` for the particular instance of the problem that is to be solved, and six procedural `parameters`, `root`, `reject`, `accept`, `first`, `next`, and `output`.

These produres should take the instance data P as a parameter and should do the following.

- `root(P)`: return the partial candidate at the root of the search tree.
- `reject(P, c)`: return true only if the partial candidate c is not worth completing.
- `accept(P, c)`: return true if c is a solution of P, and false otherwise.
- `fisrt(P, c)`: generate the first extension of candidate c.
- `next(P, c)`: generate the next alternative extension of a candidate, after the extension s.
- `output(P, c)`: use the solution c of P, as appropriate to the application.

where `P` is the search-tree structured data, and `c` and `s` are the roots of the search tree.

```
procedure backtrack(P, c) is 
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s <- first(P, c)
    while s != NULL do
        backtrack(P, s)
        s <- next(P, s)
```



## Commonly applied examples

- Eight queens puzzle
- Crosswords
- Verbal arithmetic
- Sudoku
- Peg solitaire
- Parsing
- Knapsack problem



## References

- [Wikipedia - Backtracking](https://en.wikipedia.org/wiki/Backtracking){target="_blank"}

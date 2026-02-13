# Markov Process



## Example

Value iteration, no time left.

$$

V_0(RF) = max{E(RF, a) + \gamma Pr(s\prime | RF, a) V(s\prime) }

$$

Since it is the last state, there is no sum of the later steps (or sum of 0 and 1).

I think the last V(s\prime) term should also be 0 (?).

Dynamic programming: from the last step to the previous ones.



## Horizon Effect

- finite h
- infinite h



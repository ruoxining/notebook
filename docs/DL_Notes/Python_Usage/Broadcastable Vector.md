Broadcasting is a mechanism which allows tensors with different numbers of dimensions to be added or multiplied together by (virtually) replicating the smaller tensor along the dimensions that it is lacking. 

One tensor is broadcastable to another if the following rules hold.
- Each tensor has at least one dimension.
- When iterating over the dimension size, starting at the trailing dimension, the dimension sizes must either be equal, one of them is 1, or one of them does not exist.

Examples
Same shapes are always broadcastable.
```Python
x = torch.empty(5,7,3)
y = torch.empty(5,7,3)
```

If one of the vectors does not have at least one dimension, they are not broadcastable.
```Python
x = torch.empty((0,))
y = torch.empty(2,2)
```

Lining up is from right to left.
x and y can line up trailing dimensions
```Python
x = torch.empty(5, 3, 4, 1)
y = torch.empty(   3, 1, 1)
```
1st trailing dimension: x and y both have dim 1
2nd trailing dimension: y has 1
3rd trailing dimension: x = y
4th trailing dimension: y's dimension does not exist
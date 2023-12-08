# Python面向对象语法

## Class
常见运算符重载方法
![](../asset/python.png)

## operator at(@)
An `@` at the beginning of a line is used for a class and function decorator.
Example:
```Python
class Pizza(object):
    def __init__(self):
        self.toppings = []

    def __call__(self, topping):
        # When using '@instance_of_pizza' before a function definition
        # the function gets passed onto 'topping'.
        self.toppings.append(topping())

    def __repr__(self):
        return str(self.toppings)

pizza = Pizza()

@pizza
def cheese():        # this function passes to topping()
    return 'cheese'
@pizza
def sauce():
    return 'sauce'

print pizza
# ['cheese', 'sauce']
```

```Python
def decorator(func):
   return func

@decorator
def some_func():
    pass
```
is equivalent to this code
```Python
def decorator(func):
    return func

def some_func():
    pass

some_func = decorator(some_func)
```

## \*\*kwargs
kwargs is a parameter in Python's functions, which takes an arbitrary numbers of parameters. 
Usage:
```Python
def print_keyword_args(**kwargs):
	# kwargs is a dict of the keyword args passed to the function
	for key, value in kwargs.iteritems():
		print "%s = %s" % (key, value)
print_keyword_args(first_name="John", last_name="Doe")
```
Output:
first_name = John
last_name = Doe

### 数组拷贝
```Python
s1 = [[]] * 3 ## 是浅拷贝
s1[1].append('xyx')    ## [['xyx'], ['xyx'], ['xyx']]

s2 = [[] for _ in 3]   ## 是深拷贝
s2[1].append('xyx')    ## [[], ['xyx'], []]

```
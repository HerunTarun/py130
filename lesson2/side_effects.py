# problem 1
bar = 42
qux = [1, 2, 3]
baz = 3

def foo(lst):
    value = lst.pop() # side effect through mutation
    print(f'popped {value} from the list') # side effect through input/output
    return value + bar + baz

foo(qux)

# problem 2
def sum(a, b):
    print(a + b)
    return a + b
# you have a side effect, so not a pure function

def sum(a, b):
    a + b
# you implicitly return None, not a pure function - WRONG
# The fact that the return value is always the same
# regardless of the arguments doesn't change its status
# as a pure function.

def sum(a, b):
    return a + b
# no side effects, useful return value based on arguments, \
# you're a pure function

import random

def sum(a, b):
    return a + b + random.random()
# you access random.random, which does have a side effect,
# and it propagates through this function, giving us an unreliable return value
# You're not a pure function

def sum(a, b):
    return 3.1415
# you're not a pure function because you're not returning a useful value WRONG
# Useful vs not useful is about good design
# pure vs impure is about side effects and consistency
# thus, since this function returns a consistent value for the same arguments,
# and has no side effects, it's a pure function.
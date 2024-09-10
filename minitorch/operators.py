"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable


def mul(x, y):
    return x * y

def id(x):
    return x

def add(x, y):
    return x + y

def neg(x):
    return -x

def lt(x, y):
    return x < y

def eq(x, y):
    return x == y

def max(x, y):
    return x if x > y else y

def is_close(x, y):
    return abs(x - y) < 1e-2

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x)) if x >= 0 else math.exp(x) / (1.0 + math.exp(x))

def relu(x):
    return max(x, 0)

def log(x):
    return math.log(x)

def exp(x):
    return math.exp(x)

def log_back(x, y):
    return y / x

def inv(x):
    return 1 / x

def inv_back(x, y):
    return - y / x ** 2

def relu_back(x, y):
    return y * (1 if x > 0 else 0)

def map(x, function):
    out = []
    for i in range(len(x)):
        out.append(function(x[i]))
    return out
        
def zipWith(x, y, function):
    out = []
    for i in range(len(x)):
        out.append(function(x[i], y[i]))
    return out

def reduce(x, function):
    if len(x) == 0:
        return 0.0
    out = x[0]
    for i in range(1, len(x)):
        out = function(x[i], out)
    return out

def negList(x):
    return map(x, neg)

def addLists(x, y):
    return zipWith(x, y, add)

def sum(x):
    return reduce(x, add)

def prod(x):
    return reduce(x, mul)


# TODO: Implement for Task 0.3.

#!/usr/bin/env python3.6
from functools import reduce
def multiply(x,y):
    return x*y
def prod(L):
    result=reduce(multiply,L)
    return result
print('3*5*7*9=',prod([3,5,7,9]))    

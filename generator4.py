#!/usr/bin/env python3.6
def normalize(name):
    a=name.capitalize()
    return a
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)


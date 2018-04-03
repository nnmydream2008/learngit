#!/usr/bin/env python3.6
def product(*args):
    count=1
    for number in args:
        count=count*number
    print(count)
product(3,6,9)

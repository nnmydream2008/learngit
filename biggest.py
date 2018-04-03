#!/usr/bin/env python3.6
def choose_big(x,y,z):
    if x>=y:
        bignumber=x
    else:
        bignumber=y
    if z>=bignumber:
        bignumber=z
        print('The biggest number is %d'%z)
        return 'END'
    else:
        print('The biggest number is %d'%bignumber)
        return 'END'


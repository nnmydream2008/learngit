#!/usr/bin/env python3.6
def choose_big1(x):
    Bignumber=0
    l=len(x)
    Bignumber=x[0]
    for i in range(l):
        if x[i]>=Bignumber:
            Bignumber=x[i]
    print('The biggest number what you input is:%d'%Bignumber)      

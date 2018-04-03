#!/usr/bin/env python3.6
import sys
sys.setrecursionlimit(1000000)
newlist=[]
def choose_small(x):
    Smallnumber=x[0]
    for number in x:
        if number<=Smallnumber:
            Smallnumber=number
    newlist.append(Smallnumber)
    x.remove(Smallnumber)
    a=len(x)
    if a!=0:
        choose_small(x)
    else:
        print('The sorting list(from samll to big) is:\n%s'%newlist)


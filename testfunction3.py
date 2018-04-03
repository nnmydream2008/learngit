#!/usr/bin/env python3.6
from sorting import choose_small
e=1
l=[]
while e>0:
    Input=input('Please input your number into the list(End by input end):')
    if Input=='end':
        e=-1
    else:
       l.append(int(Input))
print('The list which you input is:')
print(l)
choose_small(l)



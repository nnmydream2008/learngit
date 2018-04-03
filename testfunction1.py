#!/usr/bin/env python3.6
from biggest1 import choose_big1
a=[]
e=1
while e>0:
    Input=input('Please input your number(END by input end):')
    if Input=='end':
        e=-1 
    else:
        Input=int(Input)
        a.append(Input)
print('There are numbers what you input:')
print(a)
choose_big1(a)     


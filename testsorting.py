#!/usr/bin/env python3.6
from sorting import choose_small
from random import randint
import time
l=[]
for i in range(3001):
    num=randint(1,10000)
    l.append(num)
print('The list which computer create is:\n%s'%l)
x=time.time()
choose_small(l)
y=time.time()
usetime=y-x
print('The computer use %.2f second to sorting the list'%usetime)
    

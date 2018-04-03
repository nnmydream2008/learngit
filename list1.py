#!/usr/bin/env python3.6
L1=['Hello','World',18,'Apple',None]
L2=[]
for x in L1:
    if isinstance(x,str):
       L2.append(x)
L3=[s.lower() for s in L2 ]
print(L3)

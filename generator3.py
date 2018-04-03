#!/usr/bin/env python3.6
def triangles(x):
    L=[1]
    while True:
        yield L
        L=[L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        if len(L)>10:
            break
a=triangles(10)
for i in a:
   print(i)
   

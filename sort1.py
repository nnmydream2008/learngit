#!/usr/bin/env python3.6
L=[('bob',75),('about',92),('Zoo',66),('Credit',88)]
print(L)
def by_name(t):
    return t[0].lower()
L2=sorted(L,key=by_name)
print('By_name:',L2)
def by_score(t):
    return t[1]
L3=sorted(L,key=by_score,reverse=True)
print('By_score:',L3)

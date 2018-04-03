#!/usr/bin/env python3.6
def is_palindrome(n):
    L=list(map(int,str(n)))
    L1=L[0:]
    L2=L[::-1]
    if L1==L2:
        return True
    else:
        return False  
L=list(filter(is_palindrome,range(1,1000)))
print(L)              

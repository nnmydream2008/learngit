#!/usr/bin/env python3.6
from functools import reduce
def fn1(x,y):
    return x*10+y
def fn2(x):
    return x/1000
def fn(x,y):
    return x+y
def str2float(s):
    L=list(s)
    L.pop(3)
    L1=L[0:3]
    L2=L[3:]
    return fn(reduce(fn1,map(int,L1)),fn2(reduce(fn1,map(int,L2))))
#print('The str number is:%s'%Str)
#print('The float number is:',str2float(Str))
if abs(str2float('123.456')-123.456)<0.00001:
    print('test success!!!')
else:
    print('test failed!')   

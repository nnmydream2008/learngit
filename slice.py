#!/usr/bin/env python3.6
def trim(x):
    L=[]
    a=len(x)
    if x==[]:
        L=x
    elif x[0]==' ' and x[-1]==' ':
        L=x[1:a-1]
    elif x[0]==' ':
        L=x[1:]
    elif x[-1]==' ':
        L=x[0:a-1]
    else:
        L=x
    str_convert=' '.join(L)
    print('The slice string without blank space is %s'%str_convert)
Input=input('Please input your string:')
s=[]
for i in Input:
    s.append(i)
print('The string which you input is:%s'%Input)
trim(s)
     


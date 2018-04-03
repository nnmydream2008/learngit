#!/usr/bin/env python3.6
def findMinAndMax(x):
    output=[]
    minnumber=x[0]
    maxnumber=x[0]
    for number in x:
        if number<=minnumber:
            minnumber=number
    output.append(minnumber)
    for number in x:
        if number>=maxnumber:
            maxnumber=number
    output.append(maxnumber)
    t=tuple(output)
    print('The minnumber and maxnumber is ')
    print(t)
a=1
L=[]
while a>0:
    Input=input('Please input int into list(End by input end):')
    if Input=='end':
        a=-1
    else:
        i=int(Input)
        L.append(i)
if len(L)==0:
    print('The minnumber and maxnumber is \n(None,None)')
else:
    findMinAndMax(L)

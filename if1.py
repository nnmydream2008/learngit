#!/usr/bin/env python3.6
#height=1.75
#weight=80.5
name=input('Please input your name:')
height=float(input('Please input your height:'))
weight=float(input('Please input your weight:'))
x=height*height
bmi=weight/x
print('%s,your bmi is %f'%(name,bmi))
if bmi<18.5:
    print('%s,too light!'%name)
elif bmi>=18.5 and bmi<25:
    print('%s,normal!'%name)
elif bmi>=25 and bmi<28:
    print('%s,overweight!'%name)
elif bmi>=28 and bmi<32:
    print('%s,obesity!'%name)
else:
    print('%s,serious obesity!'%name)

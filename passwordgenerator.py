#!/usr/bin/env python3.6
from random import randint
element=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%']
length=int(input('Please input how long password\'length(8-16) you want to create:'))
password=[]
count=length
while count>0:
    i=randint(0,len(element)-1)
    password.append(element[i])
    count=count-1
print('The password which system create is:',"".join(password))

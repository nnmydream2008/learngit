#!/usr/bin/env python3.6
import os
l1=list(range(1,11))
print(l1)
l2=[x*x for x in range(1,11) if x%2==0]
print(l2)
l3=[d for d in os.listdir('.')]
print(l3)

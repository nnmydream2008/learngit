#!/usr/bin/env python3.6
g=((x * x for x in range(10)))
print(g)
for i in range(1,11):
    print(next(g))

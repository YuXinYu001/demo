#!/usr/bin/python3
# -*- coding: utf-8 -*-

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))

import math

def quadratic(a, b, c):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int , float)):
        sq = (b**2-4*a*c)
    else:
        return None
    if sq >= 0:
        x1 = (-b + math.sqrt(sq)) / (2*a)
        x2 = (-b - math.sqrt(sq)) / (2*a)
        return x1,x2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, 'a'))

def product(*arg):
    if len(arg) == 0:
        return None
    prd = 1
    for n in arg:
        if not isinstance(n, (int, float)):
            continue
        prd *= n
    return prd

print(product(5))
print(product(5,6))
print(product(5,1,7))
print(product(5,1,7,'a'))
print(product())

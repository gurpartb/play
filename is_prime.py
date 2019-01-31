#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:10:58 2019

@author: gurpartapbhatti
"""
from primes import is_prime

print('Enter a positive integer.\nI\'ll tell you if its a prime.')
print('Or enter 0 to exit')
n = input()
i = int(n)
while i != 0:
    s = n + ' is '
    if not is_prime(i):
        s += 'not '
    print(s + 'a prime integer.')
    n = input()
    i = int(n)
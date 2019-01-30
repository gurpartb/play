#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:10:58 2019

@author: gurpartapbhatti
"""
from primes import is_prime

print("Enter a positive integer.\nI'll tell you if its a prime.", end = '')
n = input()
i = int(n)
while i != 0:
    print(n + ' is', end = ' ')
    if not is_prime(i):
        print('not', end = ' ')
    print('a prime integer.')
    print('Enter 0 to exit', end = '')
    n = input()
    i = int(n)
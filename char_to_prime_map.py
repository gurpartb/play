#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:00:46 2019

@author: gurpartapbhatti
"""
from primes import n_primes

print("Enter a positive integer 'n'.\nI'll return the n primes.")
print('Or enter 0 to exit')
n = input()
i = int(n)
while i != 0:
    p = n_primes(i)
    print('{', end = '')
    for j in range(len(p)-1):
        print( '\''+chr(97 + j)+'\''+':' + str(p[j]),end = ', ')
    print('\''+chr(97+len(p)-1)+'\'' + ':' + str(p[len(p)-1]), end = '')
    print('}')
    n = input()
    i = int(n)
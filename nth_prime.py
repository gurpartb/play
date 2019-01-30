#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:07:45 2019

@author: gurpartapbhatti
"""
from primes import nth_prime
from grammar import suffix
    
print("Enter a positive integer 'n'.\nI'll return the nth prime.")
print('Or enter 0 to exit', end = '')
n = input()
i = int(n)
while i != 0:
    j = nth_prime(i)
    print(n+suffix(i) +' prime is '+ str(j), end = '')
    n = input()
    i = int(n)
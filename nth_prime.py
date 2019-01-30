#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:07:45 2019

@author: gurpartapbhatti
"""
from primes import nth_prime

def suffix(i):
    if i == 2:
        return 'nd'
    if i == 3:
        return 'rd'
    j = str(i)
    if int(j[len(j)-1]) == 1 and i != 11:
        return 'st'
    return 'th'
    
print("Enter a positive integer 'n'.\nI'll return the nth prime.", end = '')
n = input()
i = int(n)
while i != 0:
    j = nth_prime(i)
    print(n+suffix(i) +' prime is '+ str(j))
    print('Enter 0 to exit', end = '')
    n = input()
    i = int(n)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:10:58 2019

@author: gurpartapbhatti
"""

def is_prime(i):
    if i <= 1:
        return False
    j = 2
    p = True
    while p == True and j*j <= i:
        if i % j == 0:
            p = False
        j += 1
    return p
    
i = 1
print("Enter a positive integer.\nI'll tell you if its a prime.", end = '')
while i != 0:
    n = input()
    i = int(n)
    print(n + ' is', end = ' ')
    if not is_prime(i):
        print('not', end = ' ')
    print('a prime integer.')
    print('Enter 0 to exit', end = '')
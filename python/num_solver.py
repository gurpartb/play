#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:20:45 2019

@author: gurpartapbhatti
"""

def legal_n():
    for i in range(1,10):
        if i not in l:
            return i

s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
l = [1, 2, 5, 0, 5, 6, 7, 8, 9]
print(l)
# find the zero
for i in range(9):
    if l[i] == 0:
        l[i] = legal_n()
        
print(l)

# replace it with fist legal number starting from 1 to 9
# legal numbers are [1,9] and not repeated
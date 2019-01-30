#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:47:35 2019

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

def nth_prime(i):
    j = 1
    c = 0
    while c < i:
        j += 1
        if is_prime(j):
            c += 1
    return j
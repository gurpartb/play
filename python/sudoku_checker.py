#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:39:11 2019

@author: gurpartapbhatti
"""

def check_row():
    return True
    
def check_col():
    return True
    
def check_square():
    return True

#l = [[1, 2, 3, 4, 5, 6, 7, 8, 9],[ 4, 5, 6, 1, 2, 3, 7, 8, 9], [7, 8, 9, 4, 5, 6, 1, 2, 3]]

l = [[0]*9]*9
print(len(l), 'len')
for i in range(len(l)):
    for j in range(len(l[i])):
        l[i][j]=1

print(l)
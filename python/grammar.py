#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:56:15 2019

@author: gurpartapbhatti
"""

def suffix(i):
    if i == 2:
        return 'nd'
    if i == 3:
        return 'rd'
    j = str(i)
    if int(j[len(j)-1]) == 1 and i != 11:
        return 'st'
    return 'th'
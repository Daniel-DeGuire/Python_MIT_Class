# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:28:28 2024

@author: dande
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))
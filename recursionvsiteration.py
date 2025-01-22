# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:03:30 2024

@author: dande
"""

# Iteration vs Recursion

# iteration

def factorial_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod 


# recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
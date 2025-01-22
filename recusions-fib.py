# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:24:39 2024

@author: dande
"""

def fib(x):
    """ assumes x aaan int >= 0
    returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
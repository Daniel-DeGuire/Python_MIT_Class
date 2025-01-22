# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:21:49 2024

@author: dande
"""

def sq(func, x):
 y = x**2
 return func(y)

def f(x):
 return x**2

calc = sq(f, 2)
print(calc)
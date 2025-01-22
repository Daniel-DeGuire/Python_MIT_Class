# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:54:32 2024

@author: dande
"""

def is_even( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0
print("All numbers between 0 and 20: even or not")
for i in range(20):
   if is_even(i):
       print(i, "even")
   else:
       print(i, "odd")
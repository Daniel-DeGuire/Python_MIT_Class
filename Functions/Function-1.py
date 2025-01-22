# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:16:08 2024

@author: dande
"""

def is_even ( i ):
    """
    Input: i, is positive int
    Returns True if i is even, otherwise False
    """
    print("inside is_even")
    return i%2 == 0
print(is_even(3))
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:03:36 2024

@author: dande
"""

# Tuples can used to return more than one value per function.
# Function, you are only allowed to return one object per function.

def quotent_and_remainder(x, y):
    q = x // y # --> Integer divison (whole number)
    r = x % y
    return (q, r)
(quot, rem) = quotent_and_remainder(4,8)

print("Quotient:", quot)
print("Remainder:", rem)





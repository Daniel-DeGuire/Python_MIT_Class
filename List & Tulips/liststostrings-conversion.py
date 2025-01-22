# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:15:44 2024

@author: dande
"""

# convert string to list with

list(s)

# split a string on a character

s.split()

# utrn a list of characters into a string


s = "I,3 cs" # s is s astring
list(s) # returns ['I', '<', '3', ' ', 'c', 's']
s.split('<') # returns['I', '3 cs']
L = ['a', 'b', 'c']  # L is a list
''.join(L) # returns "abc"
'_'join(L) # returns "a_b_c"
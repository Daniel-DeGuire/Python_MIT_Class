# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:41:12 2024

@author: dande
"""

# Tuples vs Lists -- mutable objects / tuples are immutable...square brackets vs parenthesis

a_list = []
L = [2, 'a', 4, [1,2]]
len(L) #<-- 4
L[0] #<-- 2 
L[2]+1 #<-- 5
L[3] #<-- [1,2]
L[4] #<--- gives an error
i = 2
l[i-1] # evaluates to 'a' since L[1] = 'a'
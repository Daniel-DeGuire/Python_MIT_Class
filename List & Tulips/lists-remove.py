# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:05:48 2024

@author: dande
"""

## Delete a specific index with del

del(L(index))

## Remove a element at end of list with L.pop(), returns the removed element

L.pop()

## a specific element with remove

L.remove(element)

L = [2, 1, 3, 6, 3, 7, 0]

L.remove(2) = [1, 3, 6, 3, 7, 0]
L.remove(3) = [1, 6, 3, 7, 0]
del(L[1]) = [1, 3, 7, 0]
L.pop() = [1, 3, 7]
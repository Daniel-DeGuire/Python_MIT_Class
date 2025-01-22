# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:17:09 2024

@author: dande
"""

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
        
Towers(3, 1, 3, 2)
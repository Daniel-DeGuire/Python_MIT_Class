# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:33:39 2024

@author: dande
"""

a = 1
b = a
print(a)
print(b)

warm = ['red', 'yellow', 'orange']
hot = warm #alias, changing one changes the other
hot.append('pink')
print(hot)
print(warm)
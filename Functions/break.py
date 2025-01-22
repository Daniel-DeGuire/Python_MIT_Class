# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:43:51 2024

@author: dande
"""

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)
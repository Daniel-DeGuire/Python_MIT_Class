# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:47:08 2024

@author: dande
"""

def remove_dups(L1, L2):
    L1_copy = L1[:]  # Create a shallow copy of L1
    for e in L1_copy:  # Iterate through the copy
        if e in L2:  # Check if the element is in L2
            L1.remove(e)  # Remove the element from L1
            
            
            
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]


print("Before removal:")
print("L1:", L1)
print("L2:", L2)

remove_dups(L1, L2)

print("After removal:")
print("L1:", L1)
print("L2:", L2)
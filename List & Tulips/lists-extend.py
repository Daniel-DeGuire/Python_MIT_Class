# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:01:17 2024

@author: dande
"""

## Adding + does not mutate, rather creates a new list

L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2

L3 = [2, 1, 3, 4, 5, 6]
#L1 & L2 are unchanged

L1.extend([0,6])
# L1 Mutated to [2, 1, 3, 0, 6]
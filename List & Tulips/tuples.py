# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:47:27 2024

@author: dande
"""

te = ()
t = (2, "mit", 3)
t[0] # ---> Evaluates into 2
(2, "mit", 3) + (5,6) # --->> Evaluates to (2, "mit", 3, 5 6)   --- Concat
t[1:2] #   ---> Evaluates to ("mit",) --> Comma indicates tuple object
t[1:3] #   ---> Evaluates to ("mit", 3)
len(t) #   ---> Evaluates to (3) -- How many objects are in tuple
#l[l] = 4 # Gives Error

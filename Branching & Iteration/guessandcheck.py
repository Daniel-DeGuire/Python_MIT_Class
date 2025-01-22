# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:33:45 2024

@author: dande
"""


cube = 9
for guess in range(abs(cube)+1):
     # passed all potential cube roots
    if guess**3 >= abs(cube):
        # no need to keep searching
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))

        
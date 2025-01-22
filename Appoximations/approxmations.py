# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:57:46 2024

@author: dande
"""

cube = 27
##cube = 8120601
##cube = 10000
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
## look for close enough answer and make sure
## didn't accidentally skip the close enough bound
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    print(guess)
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube, "with these parameters.")
else:
    print(guess, 'is close to the cube root of', cube)

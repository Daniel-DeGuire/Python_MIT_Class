# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:09:26 2024

@author: dande
"""

s = "abcdefgh"
for index in range(len(s)):
        if s[index] == 'i' or s[index] == 'u':
            print("There is an i or u")

for char in s:
        if char == 'i' or char == 'u':
            print("There is an i or u")
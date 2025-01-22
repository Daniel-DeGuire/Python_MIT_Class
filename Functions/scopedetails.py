# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:21:41 2024

@author: dande
"""

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x=', x)
    h()
    print(h())
    return x

x = 3
z=g(x)


"""
Global Scope

g = some code

x = 3 

z 


---

g scope

x = 3

h = some code


---

h scope

x "abc"

"""
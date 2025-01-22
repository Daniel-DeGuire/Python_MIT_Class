# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:15:07 2024

@author: dande
"""

an_letters = "awfhilmnorsxAEFHILMNORSX"

word = input("I will cheer for your! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

# i = 0
# while i < len(word):
   # char = word[i]
    #if char in an_letters:
        
for char in word:
    if char in an_letters:
        print("Give me an "+ char + "! " + char)
    else:
        print("Give me a " + char + "! : " + char)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

            
            
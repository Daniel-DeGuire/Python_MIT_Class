# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:06:34 2024

@author: dande
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        print(f"Cleaned string: {ans}")  # Print the cleaned string
        return ans  # Ensure return is outside the loop
    
    def isPal(s):
        print(f"Checking if '{s}' is a palindrome")  # Print the current string being checked
        if len(s) <= 1:  # Base case: single character or empty string
            return True
        else:
            result = s[0] == s[-1] and isPal(s[1:-1])  # Recursive check
            print(f"Is '{s}' a palindrome? {result}")  # Print the result of the check
            return result
    
    return isPal(toChars(s))  # Combine cleaning and palindrome check


print(isPalindrome("A man, a plan, a canal, Panama"))
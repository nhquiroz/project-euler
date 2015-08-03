"""
Problem 4
=========
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def reverse(s):
    return s[::-1]

def is_palindrome(x):
    y = str(x)
    return y == reverse(y)

def solution():
    for i in range(999999,100000,-1):
        if is_palindrome(i):
            for j in range(999,99,-1):
                if (i % j) == 0 and (i / j < 1000):
                    return i

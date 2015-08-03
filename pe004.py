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
    return str(x) == reverse(str(x))

def solution():
    """
    The minimun 3-digit number is 100, while the maximum is 999.
    The largest palindrome should be between 900009 and 999999.
    """
    min_num = 913
    max_num = 1000
    largest = 0
    for i in xrange(min_num, max_num):
        for j in xrange(i, max_num):
            m = i*j
            if is_palindrome(m) and (m > largest):
                largest = m
    return largest

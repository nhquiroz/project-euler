"""
Problem 3
=========
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


from math import sqrt


N = 600851475143
M = int(sqrt(N))

def is_prime(x):
    TOP = int(sqrt(x)) + 1
    """
    If x isn't a 2 multiple, you don't need to check them as divisors in the
    range between 3 (the 1st valid divisor that meets the criteria) and sqrt(x).
    """
    if (x % 2) == 0:
        return False
    for i in xrange(3, TOP,2):
        if (x % i) == 0:
            return False
    return True

def solution():
    max_factor = 1
    for i in xrange(2, M + 1):
        if (N % i) == 0 and is_prime(i):
            max_factor = i
    return max_factor

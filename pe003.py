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
    for i in xrange(2, int(sqrt(x))):
        if (x % i) == 0:
            return False
    return True

def solution():
    max_factor = 1
    for i in xrange(2, M + 1):
        if (N % i) == 0 and is_prime(i):
            max_factor = i
    return max_factor

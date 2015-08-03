"""
Problem 10
==========
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

TOP = 2000000


def is_prime(x):
    for i in xrange(2, int(sqrt(x))+1):
        if (x % i) == 0:
            return False
    return True

def not_multiple(x):
    return (x%2)!=0 and (x%3)!=0 and (x%5)!=0

def solution():
    i     = 2
    sum_  = 0
    prime = 0
    while i < TOP:
        if not_multiple(i) and is_prime(i):
            prime = i
            sum_ += prime
        i += 1
    return sum_

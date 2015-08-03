"""
Problem 7
=========
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""

"""
Solution explained
==================
The only even prime is 2, so I start checking odd primes from 7 in advance,
filtering the 3 and 5 multiples for more speed and initialize primes_quantity
in 3. Finally, I stop when I found the 10001 one.
"""


from math import sqrt

TOP = 10001


def is_prime(x):
    for i in xrange(2, int(sqrt(x))+1):
        if (x % i) == 0:
            return False
    return True

def not_multiple(x):
    return (x%2)!=0 and (x%3)!=0 and (x%5)!=0

def solution():
    i = 7
    primes_quantity = 3
    while primes_quantity != TOP:
        if not_multiple(i) and is_prime(i):
            primes_quantity += 1
        i += 1
    print "prime: " + str(i-1)
    print "number: " + str(primes_quantity)

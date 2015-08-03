# -*- coding: utf-8 -*-

"""
Problem 9
=========
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def is_pythagorean_triplet(a, b, c):
    return (a < b < c) and (a**2 + b**2 == c**2)

def solution():
    for i in xrange(1000):
        for j in xrange(1000):
            k = 1000-i-j
            if (i+j+k == 1000) and is_pythagorean_triplet(i, j, k):
                return i*j*k

"""
Problem 3
=========
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def solution():
    n = 600851475143
    res = 3
    while n > 1:
        if (n % res) == 0:
            n /= res
        else:
            res += 2
    return res

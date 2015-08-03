"""
Problem 5
=========
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


"""
Solution explained
==================
The smallest natural number divisible by all numbers from 1 to 20 must be
divisible by all prime numbers among 1 and 20 (2*3*5*7*11*13*17*19 = 9699690).
I call this number PRIME_MULTIPLE. Then, you have to lookup multiples of this
number, and check if they're divisible by everything else. I found
experimentally that it's enough to check that the number is divisible by 9 and
16 to cover the remaining divisors, so it must be divisible by 9*16 = 144.
Finally, you want the smallest one, so the first one that meets all the
criteria is returned.
"""


PRIME_MULTIPLE = 9699690


def solution():
    i = 1
    found = False
    while not found:
        j = PRIME_MULTIPLE*i
        if (j % 144) == 0:
            return j
            found = True
        i += 1

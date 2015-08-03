# -*- coding: utf-8 -*-

"""
Problem 6
=========
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def solution():
    sum_of_the_squares = 0
    square_of_the_sum  = 0
    for i in xrange(101):
        sum_of_the_squares += i**2
        square_of_the_sum  += i
    square_of_the_sum = square_of_the_sum**2
    return square_of_the_sum - sum_of_the_squares

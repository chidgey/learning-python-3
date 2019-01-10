#!/usr/bin/env python3

"""Illustrates how to reduce a sequence into a single scalar value.

    This performs much better than using a for loop.
"""

from functools import reduce


def sum_values(x1, x2):
    '''Determine the sum of a sequence'''
    return x1 + x2


def max_value(x1, x2):
    '''Determine the highest value element in a sequence'''
    highestValue = 0
    if x1 > x2:
        highestValue = x1
    else:
        highestValue = x2

    return highestValue


sumTotal: int = reduce(sum_values, [1, 2, 3, 4])
print(sumTotal)
# or we could use the built in sum function!
print(sum([1, 2, 3, 4]))

highestValue: int = reduce(max_value, [3, 6, 7, -10])
print(highestValue)
# or we could use the build in max function, way better!
print(max([3, 6, 7, -10]))

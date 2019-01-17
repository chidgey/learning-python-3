#!/usr/bin/env python3

"""Use of filters to reduce a list, also shows some type annotations."""

from typing import List

def is_odd(x):
    return x % 2 != 0

my_nums = [1, 3, 10, 45, 6, 50]

# first approach
myFilteredList: List = list(filter(is_odd, my_nums))
print(myFilteredList)

# second approach: lambdas can be used in place of a function to find odd values
myLambdaFilteredList: List = list(filter(lambda x: x % 2 != 0, my_nums))
print(myLambdaFilteredList)
#!/usr/bin/env python3

"""Strings are not mutable, meaning you cannot use indexing to change individual
    elements of a string.
"""

# string concatenation
print('P' + 'am')

# string multiplication
print('z' * 10)

# string slicing
print('Hello moon'[6:10])

# slice from the second index to the end
print('negativeIndexing'[2:])

# slice from the start upto the 7th element
print('uptobutnotincluding'[:7])

# negative indexing with string slicing
print('negativeIndexing'[-8:])

# using step size parameter of ranges, in this case, there is no step size
print('grabthewholestringusingstepsize'[::])

# takes every other letter, jumping in step size 2
print('grabthewholestringusingstepsize'[::2])

# this is cool, it steps in reverse
print('grabthewholestringusingstepsize'[::-1])

# string uppercasing
print('Hello world'.upper())

# string lowercasing
print('Hello world'.lower())

# splitting strings, by default is whitespace
print('this is my string to split'.split())

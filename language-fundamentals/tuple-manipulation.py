#!/usr/bin/env python3

"""Tuples are immutable, meaning they cannot be changed.

    We use Tuples to make sure that variables don't get modified as we
    pass them around a program in Python.

"""

# define a new Tuple
t = (1, 2, 3, 4, 5, 6, 1)

# print the type of t, it is a tuple
print(type(t))

# length of how many elements are in the tuple
print(len(t))

# first element from the tuple
print(t[0])

# take the last element in the tuple
print(t[-1])

# step over the tuple, divide by 3 steps, take each element
print(t[::3])

# count how many times the number 1 appears in the tuple
print(t.count(1))

# there are methods for intersection, union etc...
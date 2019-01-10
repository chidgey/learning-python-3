#!/usr/bin/env python3

"""Lambdas are small anonymous functions can be created with the lambda keyword."""

def make_incrementor(n):
    return lambda x: x + n

# intializes the make_incrementor with a value of 38
f = make_incrementor(38)

# adds 2 to 38 and prints the result
print(f(2))

# adds 10 to 38 and prints the result
print(f(10))

# using lambdas inline - beware the code format tool will replace these on format!
addTwoNumbers = lambda x, y : x + y
print(addTwoNumbers(2,6))
#!/usr/bin/env python3

"""Strings are not mutable, meaning you cannot use indexing to change individual
    elements of a string.
"""

def demo():
    # String insert without specifing position
    print('This is my {} {} {} string'.format('third', 'second', 'first'))

    # Will insert the string into the placeholder, note the ordinal position assignment
    print('This is my {2} {1} {0} string'.format('third', 'second', 'first'))

    # A little more readable placeholder substitution
    print('This is my {f} {s} {t} string'.format(t='third', s='second', f='first'))

    # Float formatting follows value:width.precision
    result = 100 / 777
    print('The result was {r:1.3f}'.format(r=result))

    # OLD STYLE, don't do this, but illustrates another way to inject into a literal
    print('This is %s' % 'groovy')

    # f-strings is newer Python 3.6+
    # formatted string literals, handy as they inject directly into the literal.
    name = 'Adam'
    age = 36
    print(f'Hello, {name} who is {age}')

demo()

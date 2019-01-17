#!/usr/bin/env python3

"""Demonstration of a few techniques for working with generators.

    Generators are easy to implement, memory effcient, allow infinate streams of data and
    can be pipe-lined so that a series of operations are possible with that stream of data.

    Infinate streams are possible because we evaluate the data as needed in the generator,
    as such it is yielded on demand and can generate the response procedurally.

    https://docs.python.org/3/reference/expressions.html#generator-expressions
    https://realpython.com/introduction-to-python-generators/
"""

# Use of tuples for read-only collection data.
from typing import Tuple


def daysOfTheWeek():
    """Yielding a collection from a generator, the state of this generator is remembered"""
    daysOfTheWeek: Tuple[str] = ["Monday", "Tuesday",
                                 "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for dayOfTheWeek in daysOfTheWeek:
        yield dayOfTheWeek


def echo(value=None):
    """Example of a generator-iterator method"""
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


# making use of for is the best way, as it does the enumeration for us
for dayOfTheWeek in daysOfTheWeek():
    print(dayOfTheWeek)

# we can interact directly, as this example shows.
generator = echo(1)
print(next(generator))
print(next(generator))
print(generator.send(2))
generator.throw(TypeError, "spam")
print(next(generator))
generator.close()


# use of inline generators
monthsOfTheYear: Tuple[str] = ["Jan", "Feb", "Mar",
                               "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Nov", "Dec"]

# filter all months that begin with J from the Tuple of months
monthsThatBeginWithJ = (x for x in monthsOfTheYear if x.startswith("J"))

for month in monthsThatBeginWithJ:
    print(month)

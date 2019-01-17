#!/usr/bin/env python3

"""Tuples are immutable, meaning they cannot be changed.

    We use Tuples to make sure that variables don't get modified as we
    pass them around a program in Python.

"""


def tuple_manipulation():
    """Always wrap code in a closure, if you don't the linter get's confused over scope
    and considers things constants."""
    # define a new Tuple
    my_tuple = (1, 2, 3, 4, 5, 6, 1)

    # print the type of t, it is a tuple
    print(type(my_tuple))

    # length of how many elements are in the tuple
    print(len(my_tuple))

    # first element from the tuple
    print(my_tuple[0])

    # take the last element in the tuple
    print(my_tuple[-1])

    # step over the tuple, divide by 3 steps, take each element
    print(my_tuple[::3])

    # count how many times the number 1 appears in the tuple
    print(my_tuple.count(1))

    # there are methods for intersection, union etc...

    my_tuple = 34534
    print(my_tuple)


tuple_manipulation()

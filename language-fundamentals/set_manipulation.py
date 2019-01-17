#!/usr/bin/env python3
#pylint: disable=missing-docstring

"""Sets are unordered collections of unique elements"""


def set_manipulation_test():
    # an empty set
    myset = set()

    # adding elements to a set
    myset.add(1)
    myset.add(2)
    print(myset)

    # this won't actually work, as we already have the number 1
    myset.add(1)
    print(myset)

    # taking a list, and deduplicating it by converting it into a set
    mylistwithduplicates = [1, 2, 3, 54, 1, 123, 1, 213, 3, 3]
    print(set(mylistwithduplicates))


set_manipulation_test()

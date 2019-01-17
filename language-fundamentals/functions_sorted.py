#!/usr/bin/env python3

"""Sorting various forms of data with the built in sorted function.

    https://thepythonguru.com/python-builtin-functions/sorted/
 """


def count_vowel(s):
    '''Custom function sorting, based on number of vowels in the element value'''
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0

    for i in s:
        if i in vowels:
            count = count + 1

        return count


fruits = ['lime', 'blueberry', 'plum', 'avocado']
# default sorting, in ascending order
print(sorted(fruits))

# sort by string length
print(sorted(fruits, key=len))

# reverse the sorting
print(sorted(fruits, reverse=True))

# sorted by case insensitive
print(sorted(fruits, key=str.lower))

# Sorted based upon a custom function based on the number of vowels
print(sorted(fruits, key=count_vowel))

# using some numerical list data
ages = [45, 11, 30, 20, 55]
print(sorted(ages))
print(sorted(ages, reverse=True))

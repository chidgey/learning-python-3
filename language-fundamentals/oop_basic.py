#!/usr/bin/env python3

"""Python is an object oriented programming language."""

# It's worth taking a review of the following resource to understand special methods
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# https://thepythonguru.com/python-object-and-classes/


class Parrot:
    '''This is a docstring for the parrot class'''

    # STATIC CLASS ATTRIBUTE - defined for all instances
    species = "bird"

    # constructor for instances
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the object
blu = Parrot("Blu", 10)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())


# Delete the object when we are done
del blu

# This will throw an error, as blu is no longer defined
# print(blu)

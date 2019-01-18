#!/usr/bin/env python3

"""Use a class with abstract not implemented errors to let developers
know that the class should not be used directly and requires implementation.


This pattern is good for working with different types that share a common
interface, for example: different file types, web services etc....

Use of polymorphism to help make things easier / DRY.
"""


class MyAbstractClass():

    def __init__(self, name):
        self.name = name

    def method_1(self):
        raise NotImplementedError(
            'Subclass must impement this abstract method')

    def method_2(self):
        raise NotImplementedError(
            'Subclass must impement this abstract method')


class ImplementationOfMyAbstractClass(MyAbstractClass):

    def method_1(self):
        return self.name + " from my implementation."

    def method_2(self):
        return self.name + " from my implementation."


myImplementationInstance = ImplementationOfMyAbstractClass('DemoTest')
print(myImplementationInstance.method_1())
print()
myAbstractionInstance = MyAbstractClass('AbstractionTest')
print(myAbstractionInstance.method_1())

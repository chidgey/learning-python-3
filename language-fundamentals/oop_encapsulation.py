#!/usr/bin/env python3

"""Illustrates how Python prevents tamper of private class data"""


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

    # it's possible to hide methods too, like this.
    def __myPrivateMethod(self):
        pass


c = Computer()
c.sell()

# attempts to change the price
c.__maxprice = 1000

# or attempt to call a private method
# c.__myPrivateMethod()

# will silently fail, as python protects these special members that have double underscores
# from external tamper.
c.sell()

# using setter function
c.setMaxPrice(5555)
c.sell()
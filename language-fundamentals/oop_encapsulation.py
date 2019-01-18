#!/usr/bin/env python3

"""Illustrates how Python prevents tamper of private class data."""


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_max_price(self, price):
        self.__maxprice = price

    # it's possible to hide methods too, like this.
    def __my_private_method(self):
        pass


c = Computer()
c.sell()

# attempts to change the price, but it cannot.
# c.__maxprice = 1000

# or attempt to call a private method
# c.__my_private_method()

# will silently fail, as python protects these special members that have double underscores
# from external tamper.
c.sell()

# using setter function
c.set_max_price(5555)
c.sell()

#!/usr/bin/env python3

"""Illustrates how Python can inherit members."""

# parent class


class Bird:

    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class


class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def who_is_this(self):
        print("Penguin")

    def run(self):
        print("Run faster")


# more involved example of inheritance at play
peggy = Penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()

print(isinstance(peggy, Bird))
print(issubclass(Penguin, Bird))
print(issubclass(str, Bird))

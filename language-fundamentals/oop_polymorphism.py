#!/usr/bin/env python3

"""Illustrates how Python can offer polymorphism for members."""


class Parrot:

    def fly(self):
        print("Parrot can fly " + self)

    def swim(self):
        print("Parrot can't swim " + self)

    def __str__(self):
        return "and I'm a parrot."


class Penguin:

    def fly(self):
        print("Penguin can't fly " + self)

    def swim(self):
        print("Penguin can swim " + self)

    def __str__(self):
        return "and I'm a penguin."

# common interface - is really a function that assumes our dynamic types have a fly method
# implemented. Not really robust.


def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

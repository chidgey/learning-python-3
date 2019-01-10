#!/usr/bin/env python3

"""Pass is used to define things are syntactically OK without having to implement the details.

    Useful for scaffolding as interfaces between classes and control flow are defined.
"""


def myEmptyFunction(*args):
    pass  # Remember to implement this!


class MyEmptyClass:
    pass


# the inbuilt help method is great for inspecting objects
help(myEmptyFunction)

# the inbuilt help method is great for inspecting objects
help(MyEmptyClass)
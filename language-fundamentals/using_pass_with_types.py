#!/usr/bin/env python3

"""Pass is used to define things are syntactically OK without having to implement the details.

    Useful for scaffolding as interfaces between classes and control flow are defined.
"""

class MyEmptyClass:
    """Making use of the pass statement to leave the implementation blank whilst we work on
    the details"""

    def my_custom_function_1(self):
        pass

    def my_custom_function_2(self):
        pass


def another_yet_to_be_built_function():
    """It's interesting to note that when you have a docstring, you don't need
    a pass statement for pylint"""


# the inbuilt help method is great for inspecting objects
help(MyEmptyClass().my_custom_function_1)
help(MyEmptyClass().my_custom_function_2)
help(another_yet_to_be_built_function)

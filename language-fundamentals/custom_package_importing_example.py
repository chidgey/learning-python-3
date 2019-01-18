#!/usr/bin/env python3

""" Explores various ways to import packages, modules and functions.

https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
"""

# Importing * requires the author to specifiy in the __init__.py which
# modules are imported - this style is discouraged and will fail pylint
from custom_package_importing import *
main_module.run()

# Better to use
import custom_package_importing
# which imports the package and you explictly call the module required.
# this approach helps the reader understand where the function resides.
custom_package_importing.main_module.run()

# scopes to only module 1
from custom_package_importing.sub_package_1 import module1
module1.run()

# import using alias, to prevent the module name sub_package_1
from custom_package_importing.sub_package_2 import module1 as subPackage2Module1
subPackage2Module1.run()

# import the module's function directly into this module space
from custom_package_importing.sub_package_1.module1 import run
run()

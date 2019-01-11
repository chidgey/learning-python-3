#!/usr/bin/env python3

# read more about modules at:
# https://docs.python.org/3/tutorial/modules.html#importing-from-a-package

# note that importing * requires the author to specifiy in the __init__.py for
# the module exactly what importing * means.
from MyMainPackage import *

# import the whole module
from MyMainPackage.SubPackage1 import module1

# import the whole module but due to a module name clash, rename the import
from MyMainPackage.SubPackage2 import module1 as subPackage2Module1

# import the module function directly into this space
from MyMainPackage.SubPackage2.module1 import run

# Uses the main module
main_module.run()

# runs our subpackage1 modules function
module1.run()

# this is necessary as we have name clashes in the module
subPackage2Module1.run()

# was imported directly, so doesn't need the module name.
run()
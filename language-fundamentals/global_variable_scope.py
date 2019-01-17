#!/usr/bin/env python3

"""Use of global and local variable scope"""

# globally defined
allTheMoneyInTheWorld = 2000


def listOutVariablesInScope():
    global allTheMoneyInTheWorld
    thisIsLocal: str = "localstring"
    print("\nListing all globals\n")
    print(globals())
    print("\nListing all locals\n")
    print(locals())


def addMoney():
    # If we don't tell the method the variable is global, it will assume it's local
    # and complain it cannot be found.
    global allTheMoneyInTheWorld
    allTheMoneyInTheWorld = allTheMoneyInTheWorld + 1


print(allTheMoneyInTheWorld)
addMoney()
print(allTheMoneyInTheWorld)

listOutVariablesInScope()


# LEGB Rule
# ---------
# Local, 
# Enclosing function locals, 
# Global and
# Built-in - e.g. things like len

name = 'adam'

def greet():
    name = 'jeff'
    def hello():
        print('hello ' + name)
    hello()

greet()
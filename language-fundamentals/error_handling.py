#!/usr/bin/env python3

"""Demonstrates how we can use error handing blocks to manage issues that arise
during execution of our code."""

def ask():
    while True:
        try:
            myInt = int(input('Please enter an integer '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print('Thank you, your number squared is: {}'.format(myInt**2))
            break

# example of using a while loop until the input is validated
ask()

try:
    # attempt an operation
    print('Attempting an illegal operation')
    print(10 + '10')
    #print(10 + 10)
except TypeError as theTypeError:
    # an issue occurred
    print('A type error happened! \n\n{}'.format(theTypeError))
except OSError:
    # an issue occurred
    print('OSError issue occurred!')
except:
    print('Catch all other exceptions')
else:
    # runs after the try
    print('It looks like everything went well')
finally:
    # always runs
    print('This always runs, use it to tidy up resources.')
#!/usr/bin/env python3

from random import shuffle, randint
"""Various way to control the flow of a program"""

# using if, elif and else statements
print('\nIf, elif, else example')
isHungry = False
isThirsty = True
if isHungry == True:
    print('Feed me')
elif isThirsty == True:
    print('Water me')
else:
    print('All is well')

if True:
    print('It\'s true')


# for loops also have an else clause. The else clause executes after the loop
# completes normally. This means that the loop did not encounter a break statement.
print('\nFind Prime numbers example')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# enumerating over the characters of a string, note that we use
# underscore when we don't care about the actual variable
for _ in 'Hello moon':
    print('Cool!')  # loops over each char, printing cool for each.

# unpacking tuples into elements
myList = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in myList:
    # use of fixed notation to print out tuple content
    print(f'first=a, last=c')

# dictionary unpacking - similar to tuples
d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items():
    print(key)
    print(value)


# while loops - the else statement works like an if else, i.e. if x is not < 5 then print
x = 0
while x < 5:
    print(x)
    x += 1
else:
    print('x is not less than 5')

# break, continue and pass
# break = breaks out of the current closest loop
# continue = goes to the top of the closest loop
myString = 'Hello moon - the rest of this string will not be printed as we break'
for letter in myString:
    if letter == 'o':
        continue  # skip printing if o is found
    elif letter == '-':
        break  # break the loop on finding -
print(letter)

# this gives us a tuple, so we can get the index of the letter too
for index, letter in enumerate('abcde'):
    print(index)
    print(letter)
    print('\n')

# zipping stitches together various sequences into tuples
myList1 = [1, 2, 3, 4, 5, 6]
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300]

for item in zip(myList1, myList2, myList3):
    print(item)

# testing for existence of elements in lists/sequences
print('H' in 'Hello')
print('Z' in 'Hello')

# neat little list shuffle
myList = [1, 2, 3, 4, 5, 6]
shuffle(myList)
print(myList)

# random numbers
print(randint(0, 100))

# collecting data from the user
myNumber = input('Enter a number: ')

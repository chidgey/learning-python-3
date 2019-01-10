#!/usr/bin/env python3

"""Lists are mutable, so can be changed after creation unlike strings."""

# define a list to play with
my_list = ['one', 'two', 'three', 'four']

# list concatenation
print(my_list + ['five'])

# list multiplication
print(['z'] * 10)

# list slicing
print(my_list[2:3])

# slice from the second index to the end
print(my_list[2:])

# negative indexing with list slicing
print(my_list[-2:])

# mutability allows reassignment of values within the list
my_list[3] = 'wow'

# append in place an element to the end of the list
my_list.append('five')
print(my_list)

# will pop an element off the end of the list, effectively an undo of our append above
popped_item = my_list.pop()
print(my_list)

# we can also print out what came off the list
print(popped_item)

# it's also possible to pop an element from a specific index in the list
my_list.pop(0)
print(my_list)

# sorts the list in place, no need to assign the result
my_list.sort()
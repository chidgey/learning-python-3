#!/usr/bin/env python3

"""Shows how we can map each element through a function and store the result"""

# map function, shows how to map each value into list elements
def square(num):
    return num ** 2

my_nums = [1,2,3,4,5]

# first approach: map applies to every element
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

# second approach: lambdas can be used in place of a function
myLambdaMappedList = list(map(lambda num: num ** 2, my_nums))
print(myLambdaMappedList)
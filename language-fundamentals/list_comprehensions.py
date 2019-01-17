#!/usr/bin/env python3

# append each letter into the list
myList = [character for character in 'Hello']
print(myList)

# get all the even numbers in range for the list
myList = [x for x in range(0, 11) if x % 2 == 0]
print(myList)

# using a function / calculation to generate a list
celcius = [0, 10, 20, 34.5]
farenheit = [((9/5) * temp + 32) for temp in celcius]
print(farenheit)

# its also possible to do else statements, here replacing odd numbers with the string ODD
resultList = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(resultList)

# grab all the words that start with s and print them
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)

# even number range in a list
list(range(0, 11, 2))

print([x for x in range(1, 51) if x % 3 == 0])

for word in st.split():
    if len(word) % 2 == 0:
        print(word + ' is even')

# fizz buzz exercise
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

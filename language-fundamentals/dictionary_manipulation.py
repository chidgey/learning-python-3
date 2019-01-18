#!/usr/bin/env python3

"""Dictionary manipulation, dictionaries are mutable and unordered and cannot be sorted."""

product_dictionary = {'car': 566.88,
                      'motorbike': 344.44, 
                      'data': [1, 2, 3, 4, 'ace']}
print(product_dictionary['motorbike'])

# get the last element of the sequence from the data key
print(product_dictionary['data'][-1])

# inserting new key/value into a dictionary
product_dictionary['bicycle'] = 122.44
print(product_dictionary)

print(product_dictionary.keys())
print(product_dictionary.values())
print(product_dictionary.items())

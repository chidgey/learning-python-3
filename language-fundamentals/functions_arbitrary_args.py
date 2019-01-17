#!/usr/bin/env python3


def myfunc_optional(a, b, c=0, d=0):
    '''Optional args'''
    pass


def myfunc_args(a, b, *args):
    '''Arbitrary number of args'''
    for item in args:
        print(item)


def myfunc_keyword_args(**kwargs):
    '''Keyword args allow passing of a dictionary of key/values'''
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no fruit found')


def myfunc_args_keywords_combined(*args, **kwargs):
    '''Arbitrary number of args and dictionary args'''
    print(sum(args))
    print(kwargs)

myfunc_keyword_args(fruit='apple', someOtherKey='value')

# this allows arbitrary args, and passing in a dictionary
myfunc_args_keywords_combined(1, 2, 3, 4, fruit='apple', isEdible='yes')
#!/usr/bin/env python3

"""A simple test case can be ran with commands like the following:

python -m unittest unittest-basic
python -m unittest unittest-basic.SimplisticTest
python -m unittest unittest-basic.SimplisticTest.test

There is also automatic discovery, but it works best if you follow the conventional
module naming pattern of test*.py default

python -m unittest discover

"""

import unittest

#pylint: disable=missing-docstring
class SimplisticTest(unittest.TestCase):

    def test(self):
        _a = 'a'
        _b = 'a'
        self.assertEqual(_a, _b)

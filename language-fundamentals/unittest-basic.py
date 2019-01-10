#!/usr/bin/env python3

import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)

# python -m unittest unittest-basic
# python -m unittest unittest-basic.SimplisticTest
# python -m unittest unittest-basic.SimplisticTest.test

# There is also automatic discovery, but it works best if you follow the conventional
# module naming pattern of test*.py default
# python -m unittest discover

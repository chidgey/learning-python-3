#!/usr/bin/env python3

"""In this example, the test_combined() method never runs the assertions for 
the patterns 'c' and 'd'. The test_with_subtest() method does, and correctly 
reports the additional failure. Note that the test runner still considers there 
to only be two test cases, even though there are three failures reported.
"""

import unittest


class SubTest(unittest.TestCase):

    def test_combined(self):
        self.assertRegex('abc', 'a')
        self.assertRegex('abc', 'B')
        # The next assertions are not verified!
        self.assertRegex('abc', 'c')
        self.assertRegex('abc', 'd')

    def test_with_subtest(self):
        for pat in ['a', 'B', 'c', 'd']:
            with self.subTest(pattern=pat):
                self.assertRegex('abc', pat)
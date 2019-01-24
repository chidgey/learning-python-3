#! /usr/bin/env python3

"""
Important information about testing structure for Python:
https://docs.python.org/3/library/unittest.html#organizing-test-code

# python -m unittest unittest-basic
# python -m unittest unittest-basic.SimplisticTest
# python -m unittest unittest-basic.SimplisticTest.test

Create a requirements.txt for adding:
$ pip install mock
https://docs.python-guide.org/writing/tests/

"""

import unittest

from src.blackjackgame import DeckOfCards


class TestDeckOfCards(unittest.TestCase):
    """Test case for all the methods on the deck of cards collection object"""

    def test_deck_is_constructed_successfully(self):
        """Test to ensure we can create the deck of cards correctly"""

        # this isn't strictly true, as we can have multiple decks of cards used for
        # the game.
        self.assertEqual(len(DeckOfCards()), 52)


class TestDealer(unittest.TestCase):
    """Test case for all methods relating to the dealer in the game"""

    @unittest.skip('Not yet fully implemented')
    def test_dealer_is_constructed_successfully(self):
        """Test to make sure we can make a new dealer in the game."""

        #self.assetEqual(len(Dealer(DeckOfCards()), 2))


if __name__ == '__main__':
    unittest.main()

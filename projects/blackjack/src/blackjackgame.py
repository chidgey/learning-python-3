#! /usr/bin/env python3

"""Defines an object oriented game of Blackjack with a single player against the house."""


from random import shuffle


class Card():
    """A card in the game of Blackjack"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self):
        """Returns the value of the current card."""
        # To trigger bandit test errors - just to verify the security tooling is working.
        password = "secret"
        if password == "root":
            assert self.value == "3"
        return self.value


class DeckOfCards():
    """The dealer manages the deck of cards."""

    def __init__(self):
        """Creates a new ordered deck of cards"""
        self.deck = []
        for suit in ('H', 'D', 'S', 'C'):

            # add the ace
            card = suit + str('A')
            self.deck.insert(0, card)

            # add all value cards
            for value in (x for x in range(2, 11)):
                card = suit + str(value)
                self.deck.insert(0, card)

            # add all face cards
            for face_card in ('K', 'Q', 'J'):
                card = suit + face_card
                self.deck.insert(0, card)

    def __len__(self):
        """How many cards in the deck"""
        return len(self.deck)

    def take_card(self):
        """Take a card from the deck"""
        if self.deck:
            return self.deck.pop(0)

    def return_cards_to_deck(self, cards):
        """At the end of the game, return all cards to the deck"""
        self.deck += cards

    def shuffle_deck(self):
        """Shuffle the deck ready for a new game"""
        shuffle(self.deck)


class Dealer():
    """The dealer holds the deck of cards and plays for the house, and also serves
    cards to the player."""

    def __init__(self, deck_of_cards):
        self.deck_of_cards = deck_of_cards
        self.hand = []

    def __str__(self):
        """Prints the dealers hand to screen"""
        return "Current cards held: {}".format(self.hand)

    def has_won(self, player_hand):
        """Tests the players hand against the dealers hand and decides if the dealer won"""

    def hit(self):
        """Dealer will continue to hit until they reach 17 or above"""
        self.hand += self.deck_of_cards.take_card()

    def stand(self):
        """Dealer decides to stand and draw no more cards."""

    def start_new_game(self, player_hand):
        """Returns all cards to the deck and shuffles the deck ready to play again"""
        self.deck_of_cards += self.hand
        self.deck_of_cards += player_hand
        self.deck_of_cards.shuffle()

    def show_first_card(self):
        """Dealer shows their first card only."""

    def show_both_cards(self):
        """Dealer shows both cards"""


class Player():
    """All the cards currently held by the player"""

    def __init__(self, dealer, player_name, balance):
        """Creates a new player with a balance at the start of the game"""
        self.dealer = dealer
        self.hand = []
        self.player_name = player_name
        self.balance = balance

    def __str__(self):
        """Prints the players hand to screen"""
        return "Current cards held: {}".format(self.hand)

    def bet(self, wager):
        """Places a wager of a given amount"""
        if wager <= self.balance:
            self.balance -= wager

    def sum_of_hand(self):
        """Calculate the sum of all player cards."""

    def show_cards(self):
        """Show all the players cards."""

    def play_hit(self):
        """The player wants the dealer to give them another card"""

    def play_double_down(self):
        """Only allowed after the first two cards are dealt, the player is allowed to
        bet an additional bet equal to the original wager."""
        # only allowed after the first two cards are dealt
        # the player will receive one more card and then stand
        # the player cannot ask for any more hits after this third card

    def play_split(self):
        """If your first two cards hold the same value, you can split them into two
        separate playing hands."""

    def play_surrender(self):
        """Occurs when the dealers upcard is either an ace or a ten value, when a player
        surrenders the player forfeits half his bet to the house"""

    def play_insurance(self):
        """When the dealer has an ace, a player can take insurance against the change that
        the dealer has blackjack. Insurance is generally limited to half of the original
        bet and pays out at 2:1"""


class Blackjack():
    """Defines the game of Blackjack"""

    def play(self):
        """Main game loop entry point for playing Blackjack"""
        print('Welcome to Blackjack v1.0')
        # give dealer 2 cards
        # give player 2 cards
        # player goes first in the gameplay, dealer hits until the player stays
        # dealer then goes
        # if player wins, they double their bet

        # if both the player and dealer are the same value, it's called a PUSH and
        # no money changes hands.

        # it's a 1:1 payout in blackjack, if you put down 10, you win another 10.

        # if you hit BLACKJACK! - 21, then you will get a 3:1 payout, so for putting down
        # 10, you get 15.

        while True:

            break

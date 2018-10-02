"""
    This is the blackjack game
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


test_card = Card("Two", "Hearts")
print(test_card)


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        return "Deck is {}".format('\n'.join(str(card) for card in self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card_dealt = self.deck.pop(0)
        return card_dealt


test_deck = Deck()
test_deck.shuffle()

print(test_deck)
print('Deck size {}'.format(len(test_deck.deck)))
test_card = test_deck.deal()
print('Card dealt {}'.format(test_card))
print('Deck size {}'.format(len(test_deck.deck)))


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

    def adjust_for_ace(self):
        if self.aces != 0 and self.value >= 21:
            self.value -= 10


class Player:

    def __init__(self, credit):
        self.credit = credit


class Dealer:

    def __init__(self):
        pass



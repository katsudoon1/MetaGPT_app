"""
deck.py
Deck class for shuffling and dealing cards.
"""

import random

class Deck:
    def __init__(self):
        self.cards = []

    def shuffle(self):
        self.cards = [
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
        ] * 4
        random.shuffle(self.cards)

    def deal_card(self) -> str:
        if len(self.cards) == 0:
            self.shuffle()
        return self.cards.pop()

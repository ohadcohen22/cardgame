from games_cards.Card import Card
from random import *
import random


class DeckOfCards:
    def __init__(self):
        self.list_cards = []
        suit = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}
        value = {11: "Jack", 12: "Queen", 13: 'King', 14: "Ace"}
        for i in range(2, 15):
            for j in suit:
                c = Card(i, j)
                self.list_cards.append(c)

    def shuffle(self):
        """shuffling the deck"""
        random.shuffle(self.list_cards)

    def deal_one(self):
        """taking one random card from the deck and remove it from the card"""
        a = randint(0, len(self.list_cards)-1)
        return self.list_cards.pop(a)
        # אופציה נוספת
        # i = random.choice(self.list_cards)
        # return self.list_cards.remove(i)

    def show(self):
        """show the all the deck"""
        return self.list_cards

import random


class Player:

    def __init__(self, name, cards_number=10):
        name = str(name)
        if name.isalpha():
            self.name = name
        else:
            self.name = "unnamed player"
        self.cards_number = cards_number
        self.player_hand = []

        if self.cards_number > 26:
            self.cards_number = 26

    def set_hand(self, deck):
        """giving cards to the player from the deck"""
        for i in range(self.cards_number):
            self.player_hand.append(deck.deal_one())

    def get_card(self):
        """taking card from player's deck and remove it"""
        a = random.choice(self.player_hand)
        self.player_hand.remove(a)
        return a

    def add_card(self, card):
        """adding card to the player's deck"""
        self.player_hand.append(card)

    def __str__(self):
        return f"The player name is: {self.name} his cards: {self.player_hand}"

    def show(self):
        """shows players name and his cards"""
        return self.__str__()

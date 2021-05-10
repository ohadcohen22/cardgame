class Card:
    def __init__(self, value, suit):
        if type(value) != int:
            raise TypeError("value must be int")
        if value == 1:
            self.value = 14
        if 1 > value or value > 14:
            raise TypeError("invalid value")
        self.value = value
        if type(suit) != int:
            raise TypeError("suit mist be int")
        if 1 > suit or suit > 4:
            raise TypeError("invalid suit")
        self.suit = suit

        self.values = {11: "Jack", 12: "Queen", 13: 'King', 14: "Ace"}
        self.suits = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}

    def __repr__(self):
        if 10 < self.value < 15:
            return f"{self.values[self.value]} {self.suits[self.suit]}"
        elif 0 < self.value <= 10:
            return f"{self.value} {self.suits[self.suit]}"
        else:
            return False

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True

    def __gt__(self, other):
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        else:
            return False

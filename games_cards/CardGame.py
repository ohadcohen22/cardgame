from games_cards.DeckOfCards import DeckOfCards
from games_cards.Player import Player


class CardGame:
    def __init__(self, name1, name2, num_cards=10):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.num_cards = num_cards
        self.deck = DeckOfCards()
        self.new_game()

    def new_game(self):
        """"shuffling the deck if the deck is full, giving to the players cards else giving an error """
        if len(self.deck.list_cards) == 52:
            self.deck.shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
        else:
            print("Error, deck is not full cant start a new game")

    def get_winner(self):
        """check and pronounce who is the winner return None if its draw"""
        if len(self.player1.player_hand) > len(self.player2.player_hand):
            return self.player2.name

        elif len(self.player1.player_hand) < len(self.player2.player_hand):
            return self.player1.name

        elif len(self.player1.player_hand) == len(self.player2.player_hand):
            return None

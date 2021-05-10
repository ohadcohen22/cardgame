from unittest import TestCase

from games_cards.CardGame import CardGame
from games_cards.Player import Player
from games_cards.Card import Card


class TestCardGame(TestCase):
    def setUp(self):
        print("I am setup")

    def test_card_num__init__(self):
        """checks card number will be 10 as default"""
        cg = CardGame("aa", "bb")
        self.assertEqual(cg.num_cards, 10)

    def test_new_game_checking(self):
        """checking the function is really gives cards to the players"""
        cg = CardGame('ohad', 'polly')
        self.assertEqual(len(cg.player1.player_hand), 10)
        self.assertEqual(len(cg.player2.player_hand), 10)

    def test_new_game_deck_not_full(self):
        """checks the function wont start a new game if the deck is not full"""
        cardgame = CardGame('ohad', 'polly')
        self.assertEqual(len(cardgame.player1.player_hand), 10)
        self.assertEqual(len(cardgame.player2.player_hand), 10)
        self.assertEqual(len(cardgame.deck.list_cards), 32)
        cardgame.new_game()
        self.assertNotEqual(len(cardgame.deck.list_cards), 52)

    def test_get_winner_player2_win(self):
        """checks the winner is player 2"""
        player1 = Player("ohad")
        player2 = Player("polly")
        game = CardGame(player1.name, player2.name)
        game.player1.player_hand = [Card(8, 3), Card(9, 4), Card(13, 4)]
        game.player2.player_hand = [Card(7, 3)]
        winner = game.get_winner()
        self.assertEqual(player2.name, winner)

    def test_get_winner_player1_win(self):
        """checks thw winner is player 1"""
        player1 = Player("ohad")
        player2 = Player("polly")
        game = CardGame(player1.name, player2.name)
        game.player2.player_hand = [Card(8, 3), Card(9, 4), Card(13, 4)]
        game.player1.player_hand = [Card(7, 3)]
        winner = game.get_winner()
        self.assertEqual(player1.name, winner)

    def test_get_winner_draw(self):
        """checks if the result is draw"""
        player1 = Player("ohad")
        player2 = Player("polly")
        game = CardGame(player1.name, player2.name)
        game.player2.player_hand = [Card(8, 3), Card(9, 4), Card(13, 4)]
        game.player1.player_hand = [Card(7, 3), Card(10, 4), Card(12, 4)]
        winner = game.get_winner()
        self.assertEqual(None, winner)

    def tearDown(self):
        print('I am teardown')

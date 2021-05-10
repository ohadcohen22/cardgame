from unittest import TestCase, mock
from games_cards.Player import Player
from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        print("I am setup")

    def test_invalid_name__init__(self):
        """cases when the name is not only letters"""
        player = Player("!!!")
        self.assertEqual("unnamed player", player.name)
        player = Player("123")
        self.assertEqual("unnamed player", player.name)
        player = Player("o!h!a!d123")
        self.assertEqual("unnamed player", player.name)

    def test_valid_name__init__(self):
        """checks valid name"""
        player = Player("ohad")
        self.assertEqual("ohad", player.name)

    def test_card_number__init__(self):
        """checks what happened if the cards number>26"""
        player = Player("Ohad", 29)
        self.assertEqual(player.cards_number, 26)

    @mock.patch('games_cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(11, 2))
    def test_set_hand1(self, mock_deal_one):
        """checks the player really get cards from the deck"""
        deck = DeckOfCards()
        player = Player('Ohad')
        player.set_hand(deck)
        self.assertEqual(player.player_hand.count(Card(11, 2)), 10)

    def test_set_hand_all_cards_set(self):
        """checks the game will played for 10 rounds"""
        deck = DeckOfCards()
        player = Player('Ohad')
        player.set_hand(deck)
        self.assertEqual(len(player.player_hand), player.cards_number)

    def test_get_card(self):
        """checks the function removing card from players' deck"""
        player = Player("aaa")
        player.player_hand = [Card(9, 3), Card(11, 2), Card(13, 1)]
        player.get_card()
        self.assertEqual(len(player.player_hand), 2)

    def test_add_card(self):
        """checks the function is adds card to the players' deck"""
        player = Player("aaa")
        card = Card(4, 3)
        player.add_card(card)
        self.assertIn(card, player.player_hand)

    def test_show(self):
        """checks the method are really shows the player name and deck"""
        player = Player("ohad")
        self.assertEqual(player.show(), player.__str__())

    def tearDown(self):
        print('I am teardown')

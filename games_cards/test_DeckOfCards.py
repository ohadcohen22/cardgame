from unittest import TestCase, mock
from games_cards.DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        print("I am setup")

    @mock.patch('random.shuffle', return_value=[])
    def test_shuffle(self, mock_shuffle):
        """checking the list is shuffling the deck"""
        deck = DeckOfCards()
        deck.shuffle()
        mock_shuffle.assert_called_once_with(deck.list_cards)

    def test_deal_one(self):
        """copy the deck of cards to 'a' and remove if the card we removed appears on the copied list"""
        deck = DeckOfCards()
        a = deck.list_cards.copy()
        self.assertIn(deck.deal_one(), a)

    def test_show(self):
        """checks the method are really shows the full deck"""
        deck = DeckOfCards()
        self.assertEqual(deck.show(), deck.list_cards)

    def tearDown(self):
        print("I am teardown")

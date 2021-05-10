from unittest import TestCase
from games_cards.Card import Card


class TestCard(TestCase):
    def setUp(self):
        print("I am setup")

    def test_valid__init__(self):
        """valid init check"""
        Card(14, 4)
        self.assertTrue(True)

    def test_invalid_value__init__(self):
        """cases when the value invalid"""
        try:
            Card('a', 3)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
        try:
            Card(33, 3)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

        try:
            Card(0, 3)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

        try:
            Card(14, 3)
            self.assertTrue(True)
        except TypeError:
            self.assertTrue(True)

        try:
            Card(15, 3)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_invalid_suit__init__(self):
        """cases when the suit is invalid"""
        try:
            Card(3, 'a')
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
        try:
            Card(3, 43)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
        try:
            Card(3, 5)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

        try:
            Card(3, 0)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_valid__gt__(self):
        """checking card gt from another"""
        card1 = Card(9, 4)
        card2 = Card(3, 4)
        self.assertTrue(card1 > card2)

    def test_invalid__gt__(self):
        """checking  card gt from another"""
        card1 = Card(9, 4)
        card2 = Card(3, 4)
        self.assertFalse(card1 < card2)

    def test_suit__gt__(self):
        """checking if value is equal the gt card will be the one with the gt suit"""
        card1 = Card(8, 4)
        card2 = Card(8, 3)
        self.assertTrue(card1 > card2)

    def tearDown(self):
        print("I am teardown")

import unittest
from wordbank.wordbank import WordBank
from parameterized import parameterized


class Properties:
    def __init__(self):
        self.min_word_length = 5
        self.max_word_length = 10
        self.puzzle_row_length = 13


class TestWordBank(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.wordbank = WordBank(properties=self.properties)

    @parameterized.expand([
        ('couch', True),
        ('cat', False),
        ('geographical', False)
    ])
    def test_is_valid_word(self, word, expected):
        self.wordbank.properties.min_word_length = 5
        self.wordbank.properties.max_word_length = 10
        is_valid_word = self.wordbank.is_valid_word(word)
        self.assertEqual(expected, is_valid_word)

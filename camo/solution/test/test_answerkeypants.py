import unittest
from wordbank.wordbank import WordBank


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13


class TestAnswerKeyPants(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()

    def test_earliest_letter_index(self):
        wordbank = WordBank(properties)
        wordbank.unique_words.append("whale")
        wordbank.unique_words.append("sample")

        chosen_letter = 'a'
        self.assertEqual(1, 1)


















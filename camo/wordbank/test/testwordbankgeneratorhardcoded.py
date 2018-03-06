import unittest
from wordbank.wordbankgenerator import WordBankGeneratorHardCoded, WordBank


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13


class TestWordBankGeneratorHardcoded(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()

    def test_generate_word_bank(self):
        generator = WordBankGeneratorHardCoded(self.properties)
        word_bank = generator.generate_word_bank()
        self.assertIsInstance(word_bank, WordBank)

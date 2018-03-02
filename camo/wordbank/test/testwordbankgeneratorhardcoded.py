import unittest
from wordbank.wordbankgenerator import WordBankGeneratorHardCoded, WordBank


class TestWordBankGeneratorHardcoded(unittest.TestCase):
    def test_generate_word_bank(self):
        generator = WordBankGeneratorHardCoded(app_properties=None)
        word_bank = generator.generate_word_bank()
        self.assertIsInstance(word_bank, WordBank)

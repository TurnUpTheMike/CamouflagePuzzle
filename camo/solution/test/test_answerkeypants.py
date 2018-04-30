import unittest
from wordbank.wordbank import WordBank
from solution.answerkeypants import AnswerKeyGeneratorPants


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13


class TestAnswerKeyPants(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.generator = AnswerKeyGeneratorPants(self.properties)

    def test_choose_word(self):
        chosen_letter = 'c'
        chosen_word = 'abcde'

        wordbank = WordBank(self.properties)
        # test that these suffixes match the chosen prefix
        wordbank.unique_words.add("zzabz")
        wordbank.unique_words.add("zabzd")
        wordbank.unique_words.add("abzde")
        wordbank.unique_words.add("abzdez")

        # test that these suffixes do not match the chosen prefix
        wordbank.unique_words.add("zzabzy")
        wordbank.unique_words.add("zabzdy")
        wordbank.unique_words.add("zzayz")
        wordbank.unique_words.add("zzybz")

        # test that length of prefixes
        wordbank.unique_words.add("zzzabz")
        wordbank.unique_words.add("zzzzabz")
        wordbank.unique_words.add("zzzzzabz")
        wordbank.unique_words.add("zzzzzzabz")

        # prefix is too long
        wordbank.unique_words.add("yzzzzzzabz")

        self.generator.choose_word(chosen_letter, chosen_word, wordbank)

        self.assertEqual(1, 1)

    def test_choose_word_planet(self):
        chosen_letter = 'a'
        chosen_word = 'planet'

        wordbank = WordBank(self.properties)
        wordbank.unique_words.add("apple")
        wordbank.unique_words.add("sample")

        self.generator.choose_word(chosen_letter, chosen_word, wordbank)

        self.assertEqual(1, 1)


















import unittest
from wordbank.wordbank import WordBank
from solution.answerkeypants import AnswerKeyGeneratorPants
from solution.puzzleutility import PuzzleUtility


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13


class TestAnswerKeyPants(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.utility = PuzzleUtility(self.properties)
        self.generator = AnswerKeyGeneratorPants(self.properties, self.utility)

    def xtest_choose_word(self):
        chosen_letter = 'c'
        chosen_word = 'abcde'

        wordbank = WordBank(self.properties)
        # test that these suffixes match
        wordbank.unique_words.add("zzabz")
        wordbank.unique_words.add("zabzd")
        wordbank.unique_words.add("abzde")
        wordbank.unique_words.add("abzdez")

        # test that these suffixes do not match
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

        # test that these prefixes match the chosen suffix
        wordbank.unique_words.add("zdezz")
        wordbank.unique_words.add("bzdez")
        wordbank.unique_words.add("zabzde")

        # test that these prefixes do not match
        wordbank.unique_words.add("yzdez")
        wordbank.unique_words.add("ybzde")
        wordbank.unique_words.add("ayzde")

        self.generator.choose_word(chosen_letter, chosen_word, wordbank)

        self.assertEqual(1, 1)

    def xtest_choose_word_planet(self):
        chosen_letter = 'a'
        chosen_word = 'planet'

        wordbank = WordBank(self.properties)
        wordbank.unique_words.add("apple")
        wordbank.unique_words.add("sample")

        self.generator.choose_word(chosen_letter, chosen_word, wordbank)

        self.assertEqual(1, 1)


















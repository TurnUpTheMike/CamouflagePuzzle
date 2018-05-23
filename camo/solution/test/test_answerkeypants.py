import unittest
from wordbank.wordbank import WordBank
from solution.answerkeypants import AnswerKeyGeneratorPants
from solution.puzzleutility import PuzzleUtility
from parameterized import parameterized


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13


class TestAnswerKeyPants(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.utility = PuzzleUtility(self.properties)
        self.generator = AnswerKeyGeneratorPants(self.properties, self.utility)
        self.wordbank = WordBank(self.properties)

    @parameterized.expand([
        ('e', "[a-df-z]"),
        ('a', "[b-z]"),
        ('z', "[a-y]"),
    ])
    def test_generate_not_letter_expression(self, letter, expected_expression):
        actual_expression = self.generator.generate_not_letter_expression(letter)
        self.assertEqual(expected_expression, actual_expression)

    def test_get_words_that_almost_match_suffixes_match(self):
        chosen_letter = 'c'
        chosen_word = 'abcde'

        # test that these suffixes match
        self.wordbank.unique_words.add("zzabz")
        self.wordbank.unique_words.add("zabzd")
        self.wordbank.unique_words.add("abzde")
        self.wordbank.unique_words.add("abzdez")

        # test that these suffixes do not match
        self.wordbank.unique_words.add("zzabzy")
        self.wordbank.unique_words.add("zabzdy")
        self.wordbank.unique_words.add("zzayz")
        self.wordbank.unique_words.add("zzybz")

        expected_zzabz = ('zzab','z','')
        expected_zabzd = ('zab','z','d')
        expected_abzde = ('ab','z','de')
        expected_abzdez = ('ab','z','dez')

        match_hash = self.generator.get_words_that_almost_match(chosen_letter, chosen_word, self.wordbank)

        self.assertEqual(expected_zzabz, match_hash['zzabz'].groups())
        self.assertEqual(expected_zabzd, match_hash['zabzd'].groups())
        self.assertEqual(expected_abzde, match_hash['abzde'].groups())
        self.assertEqual(expected_abzdez, match_hash['abzdez'].groups())

        self.assertNotIn('zzabzy', match_hash)
        self.assertNotIn('zabzdy', match_hash)
        self.assertNotIn('zzayz', match_hash)
        self.assertNotIn('zzybz', match_hash)

    def test_get_words_that_almost_match_prefixes_match(self):
        chosen_letter = 'c'
        chosen_word = 'abcde'

        # test that these prefixes match the chosen suffix
        self.wordbank.unique_words.add("zdezz")
        self.wordbank.unique_words.add("bzdez")
        self.wordbank.unique_words.add("zabzde")

        # test that these prefixes do not match
        self.wordbank.unique_words.add("yzdez")
        self.wordbank.unique_words.add("ybzde")
        self.wordbank.unique_words.add("ayzde")

        expected_zdezz = ('','z','dezz')
        expected_bzdez = ('b','z','dez')
        expected_zabzde = ('zab','z','de')

        match_hash = self.generator.get_words_that_almost_match(chosen_letter, chosen_word, self.wordbank)

        self.assertEqual(expected_zdezz, match_hash['zdezz'].groups())
        self.assertEqual(expected_bzdez, match_hash['bzdez'].groups())
        self.assertEqual(expected_zabzde, match_hash['zabzde'].groups())

        self.assertNotIn('yzdez', match_hash)
        self.assertNotIn('ybzde', match_hash)
        self.assertNotIn('ayzde', match_hash)

    def test_get_words_that_almost_match_prefix_length(self):
        chosen_letter = 'c'
        chosen_word = 'abcde'

        # test that length of prefixes
        self.wordbank.unique_words.add("zzzabz")
        self.wordbank.unique_words.add("zzzzabz")

        # prefix is too long
        self.wordbank.unique_words.add("yzzzzabz")

        match_hash = self.generator.get_words_that_almost_match(chosen_letter, chosen_word, self.wordbank)

        self.assertIn('zzzabz', match_hash)
        self.assertIn('zzzzabz', match_hash)
        self.assertNotIn('yzzzzzzabz', match_hash)

    def xtest_choose_word_planet(self):
        chosen_letter = 'a'
        chosen_word = 'planet'

        self.wordbank = WordBank(self.properties)
        self.wordbank.unique_words.add("apple")
        self.wordbank.unique_words.add("sample")

        match_hash = self.generator.get_words_that_almost_match(chosen_letter, chosen_word, self.wordbank)

        self.assertEqual(1, 1)


















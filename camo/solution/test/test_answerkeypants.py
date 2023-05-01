import unittest
from wordbank.wordbank import WordBank
from solution.answerkeypants import AnswerKeyGeneratorPants, AnswerKeyGeneratorTheme
from solution.puzzleutility import PuzzleUtility
from parameterized import parameterized


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13
        self.min_word_length = 5
        self.max_word_length = 13
        self.rows_to_obscure = 19


class TestAnswerKeyPants(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.utility = PuzzleUtility(self.properties)
        self.generator = AnswerKeyGeneratorPants(self.properties, self.utility)
        self.wordbank = WordBank(self.properties)
        return super().setUp()

    @parameterized.expand([
        ('e', "[abcdfghijklmnopqrstuvwxyz]"),
        ('a', "[bcdefghijklmnopqrstuvwxyz]"),
        ('z', "[abcdefghijklmnopqrstuvwxy]"),
    ])
    def test_generate_not_letter_expression(self, letter, expected_expression):
        actual_expression = self.generator.generate_not_letter_expression(letter)
        self.assertEqual(expected_expression, actual_expression)

    def test_get_words_that_almost_match_suffixes_match(self):
        chosen_letter = 'c'
        chosen_word = 'abcde'
        letter_index = self.utility.letter_ndx_of_word(chosen_word, chosen_letter)

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

        expected_zzabz = ('zzab', 'z', '')
        expected_zabzd = ('zab', 'z', 'd')
        expected_abzde = ('ab', 'z', 'de')
        expected_abzdez = ('ab', 'z', 'dez')

        match_hash = self.generator.get_words_that_almost_match(chosen_letter, letter_index, chosen_word, self.wordbank)

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
        letter_index = self.utility.letter_ndx_of_word(chosen_word, chosen_letter)

        # test that these prefixes match the chosen suffix
        self.wordbank.unique_words.add("zdezz")
        self.wordbank.unique_words.add("bzdez")
        self.wordbank.unique_words.add("zabzde")

        # test that these prefixes do not match
        self.wordbank.unique_words.add("yzdez")
        self.wordbank.unique_words.add("ybzde")
        self.wordbank.unique_words.add("ayzde")

        expected_zdezz = ('', 'z', 'dezz')
        expected_bzdez = ('b', 'z', 'dez')
        expected_zabzde = ('zab', 'z', 'de')

        match_hash = self.generator.get_words_that_almost_match(chosen_letter, letter_index, chosen_word, self.wordbank)

        self.assertEqual(expected_zdezz, match_hash['zdezz'].groups())
        self.assertEqual(expected_bzdez, match_hash['bzdez'].groups())
        self.assertEqual(expected_zabzde, match_hash['zabzde'].groups())

        self.assertNotIn('yzdez', match_hash)
        self.assertNotIn('ybzde', match_hash)
        self.assertNotIn('ayzde', match_hash)

    def test_get_words_that_almost_match_prefix_length(self):
        chosen_letter = 'c'
        chosen_word = 'abcde'
        letter_index = self.utility.letter_ndx_of_word(chosen_word, chosen_letter)

        # test that length of prefixes
        self.wordbank.unique_words.add("zzzabz")
        self.wordbank.unique_words.add("zzzzabz")

        # prefix is too long
        self.wordbank.unique_words.add("yzzzzabz")

        match_hash = self.generator.get_words_that_almost_match(chosen_letter, letter_index, chosen_word, self.wordbank)

        self.assertIn('zzzabz', match_hash)
        self.assertIn('zzzzabz', match_hash)
        self.assertNotIn('yzzzzzzabz', match_hash)

    def test_choose_word_planet(self):
        chosen_letter = 'a'
        chosen_word = 'planet'

        self.wordbank.unique_words.add("potator")
        self.wordbank.unique_words.add("sample")

        self.generator.flag_match_counts = False
        letter_index = self.utility.letter_ndx_of_word(chosen_word, chosen_letter)
        mashed_word = self.generator.choose_word(chosen_letter, letter_index, chosen_word, self.wordbank)

        self.assertEqual(('samplanet', 5), mashed_word)

    def test_generate_answer_key(self):
        # A
        self.wordbank.add_word("planet")
        self.wordbank.add_word("apple")
        self.wordbank.add_word("sample")
        # B
        self.wordbank.add_word("bubble")
        self.wordbank.add_word("trouble")
        self.wordbank.add_word("thumb")
        # C
        self.wordbank.add_word("practice")
        self.wordbank.add_word("cactus")
        self.wordbank.add_word("tractor")
        # D
        self.wordbank.add_word("candle")
        self.wordbank.add_word("bland")
        self.wordbank.add_word("doctor")
        # E
        self.wordbank.add_word("treacherous")
        self.wordbank.add_word("eternity")
        self.wordbank.add_word("episode")
        # F
        self.wordbank.add_word("perfect")
        self.wordbank.add_word("feather")
        self.wordbank.add_word("staff")
        # G
        self.wordbank.add_word("laugh")
        self.wordbank.add_word("gather")
        self.wordbank.add_word("lugage")
        # H
        self.wordbank.add_word("beach")
        self.wordbank.add_word("hopeful")
        self.wordbank.add_word("brother")
        # I
        self.wordbank.add_word("guitar")
        self.wordbank.add_word("instinct")
        self.wordbank.add_word("light")
        # J
        self.wordbank.add_word("jungle")
        self.wordbank.add_word("project")
        self.wordbank.add_word("justice")
        self.wordbank.add_word("jester")
        # K
        self.wordbank.add_word("blanket")
        self.wordbank.add_word("clock")
        self.wordbank.add_word("trick")
        # L
        self.wordbank.add_word("color")
        # M
        self.wordbank.add_word("smile")
        # N
        self.wordbank.add_word("stamina")
        # O
        self.wordbank.add_word("blood")
        # P
        self.wordbank.add_word("protect")
        # Q
        self.wordbank.add_word("sequence")
        self.wordbank.add_word("queen")
        self.wordbank.add_word("liquor")
        # R
        self.wordbank.add_word("partner")
        # S
        self.wordbank.add_word("respect")
        # T
        self.wordbank.add_word("flatten")
        # U
        self.wordbank.add_word("hundred")
        self.wordbank.add_word("unique")
        self.wordbank.add_word("plateau")
        # V
        self.wordbank.add_word("alive")
        self.wordbank.add_word("volcano")
        self.wordbank.add_word("vivid")
        # W
        self.wordbank.add_word("below")
        self.wordbank.add_word("weather")
        self.wordbank.add_word("whether")
        self.wordbank.add_word("world")
        self.wordbank.add_word("wealth")
        self.wordbank.add_word("power")
        # X
        self.wordbank.add_word("expert")
        self.wordbank.add_word("extra")
        self.wordbank.add_word("suffix")
        # Y
        self.wordbank.add_word("player")
        self.wordbank.add_word("yellow")
        self.wordbank.add_word("portray")
        self.wordbank.add_word("belly")
        self.wordbank.add_word("young")
        self.wordbank.add_word("pantry")
        # Z
        self.wordbank.add_word("zebra")
        self.wordbank.add_word("pizza")
        self.wordbank.add_word("puzzle")
        self.wordbank.add_word("plaza")

        # self.wordbank.print_wordbank()

        # Generate the AnswerKey
        # self.generator.flag_verbose = True
        self.generator.flag_match_counts = False
        answerkey = self.generator.generate_answer_key(self.wordbank)

        # answerkey.print_answerkey()

        # assert we have answers for all letters
        for letter in "abcdefghijklmnopqrstuvwxyz":
            self.assertIn(letter, answerkey.answers)
            self.assertIn(letter, answerkey.answers_unmodified)

            # the real answer is a substring of the mashed up answer
            real_answer = answerkey.answers_unmodified[letter]
            mashed_answer = answerkey.answers[letter]
            # print("{} : {}".format(letter, mashed_answer))
            self.assertIn(real_answer, mashed_answer)
















import unittest
from parameterized import parameterized
from solution.puzzle import PuzzleGenerator


class Properties:
    def __init__(self):
        self.min_word_length = 5
        self.max_word_length = 10
        self.puzzle_row_length = 13


class PuzzleGeneratorA(PuzzleGenerator):
    def create_letter_to_append(self):
        return 'A'


class TestPuzzleGenerator(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.generator = PuzzleGeneratorA(self.properties)

    @parameterized.expand([
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (8, 1),
        (9, 2),
        (10, 3),
        (11, 4),
        (12, 5),
        (13, 6)
    ])
    def test_earliest_letter_index(self, word_length, expected):
        index = self.generator.earliest_letter_index(word_length)
        self.assertEqual(expected, index)

    @parameterized.expand([
        (0, "AAAAAA"),
        (1, "AAAAA"),
        (2, "AAAA"),
        (3, "AAA"),
        (4, "AA"),
        (5, "A"),
        (6, "")
    ])
    def test_create_left_padding(self, letter_index, expected):
        actual = self.generator.create_left_padding(letter_index)
        self.assertEqual(expected, actual)

    @parameterized.expand([
        (6, 13, ""),
        (6, 12, "A"),
        (5, 12, ""),
        (6, 11, "AA"),
        (5, 11, "A"),
        (4, 11, ""),
        (6, 10, "AAA"),
        (5, 10, "AA"),
        (4, 10, "A"),
        (3, 10, ""),
        (6, 9, "AAAA"),
        (5, 9, "AAA"),
        (4, 9, "AA"),
        (3, 9, "A"),
        (2, 9, ""),
        (6, 8, "AAAAA"),
        (5, 8, "AAAA"),
        (4, 8, "AAA"),
        (3, 8, "AA"),
        (2, 8, "A"),
        (1, 8, ""),
        (6, 7, "AAAAAA"),
        (5, 7, "AAAAA"),
        (4, 7, "AAAA"),
        (3, 7, "AAA"),
        (2, 7, "AA"),
        (1, 7, "A"),
        (0, 7, ""),
        (5, 6, "AAAAAA"),
        (4, 6, "AAAAA"),
        (3, 6, "AAAA"),
        (2, 6, "AAA"),
        (1, 6, "AA"),
        (0, 6, "A"),
        (4, 5, "AAAAAA"),
        (3, 5, "AAAAA"),
        (2, 5, "AAAA"),
        (1, 5, "AAA"),
        (0, 5, "AA"),
    ])
    def test_create_right_padding(self, letter_index, word_length, expected):
        actual = self.generator.create_right_padding(letter_index, word_length)
        self.assertEqual(expected, actual, "letter_index = {} word_length = {}".format(letter_index, word_length))

    def test_create_letter_to_append(self):
        self.generator = PuzzleGenerator(self.properties)
        random_letter_1 = self.generator.create_letter_to_append()
        random_letter_2 = self.generator.create_letter_to_append()
        random_letter_3 = self.generator.create_letter_to_append()

        # The same letter three times in a row is not random
        self.assertFalse(random_letter_1 == random_letter_2 and random_letter_1 == random_letter_3)




















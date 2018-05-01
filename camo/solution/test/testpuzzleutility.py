import unittest
from parameterized import parameterized
from solution.puzzleutility import PuzzleUtility


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13


class TestPuzzleUtility(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.util = PuzzleUtility(self.properties)

    @parameterized.expand([
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
    def test_earliest_possible_index_choice(self, word_length, expected_earliest):
        actual_earliest = self.util.earliest_possible_index_choice(word_length)
        self.assertEqual(expected_earliest, actual_earliest)

    @parameterized.expand([
        ("planet", "p", 0),
        ("planet", "l", 1),
        ("planet", "a", 2),
        ("planet", "n", 3),
        ("abracadabra", "a", 5),
        ("abracadabra", "b", 8),
        ("abracadabra", "r", 9),
        ("abracadabra", "c", 4),
        ("abracadabra", "d", 6)
    ])
    def test_letter_ndx_of_word(self, word, letter, expected_index):
        actual_index = self.util.letter_ndx_of_word(word, letter)
        self.assertEqual(expected_index, actual_index)

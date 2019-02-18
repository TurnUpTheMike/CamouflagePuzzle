import unittest
from solution.puzzleletterstats import PuzzleLetterStats


class TestPuzzleLetterStats(unittest.TestCase):
    def setUp(self):
        self.generator = PuzzleLetterStats(None, None)

    def test_reset_letter_bank(self):
        self.assertEqual(self.generator.letter_bank_default, self.generator.letter_bank,
                         "Expect the letter_bank to be equivalent to the letter_bank_default after construction")
        self.generator.create_letter_to_append()
        self.assertNotEqual(self.generator.letter_bank_default, self.generator.letter_bank,
                            "Expect the letter_bank to be altered after create_letter_to_append")
        self.generator.reset_letter_bank()
        self.assertEqual(self.generator.letter_bank_default, self.generator.letter_bank,
                         "Expect the letter_bank to be equivalent to the letter_bank_default after reset_letter_bank")

    def test_create_letter_to_append_removes_letter_choice(self):
        letter_choice = self.generator.create_letter_to_append()
        self.assertEqual(-1, self.generator.letter_bank.find(letter_choice),
                         "Expect the chosen letter to not be in the letter_bank after it is chosen")


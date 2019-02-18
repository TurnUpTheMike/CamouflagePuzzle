import unittest
import os
from packaging.puzzlepackager import PuzzlePackager, SolutionPackager
from solution.puzzle import Puzzle
from solution.answerkey import AnswerKey
from solution.puzzleutility import PuzzleUtility


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        self.puzzle_template = parent_directory + "/puzzle_template.html"
        self.puzzle_output_dir = ""
        self.puzzle_pdf_name = "testing_puzzle.pdf"
        self.answerkey_txt_name = "answerkey_{}.txt"
        self.dir_of_answer_keys = current_directory


class TestPuzzlePackager(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()
        self.puzzle = self.get_test_puzzle()

    def get_test_puzzle(self):
        puzzle = Puzzle()
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")

        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")

        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")

        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")

        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")
        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")

        puzzle.puzzle_rows.append("ABCDEFGHIJKLM")

        return puzzle

    def integration_test_puzzle_to_html(self):
        packager = PuzzlePackager(properties=self.properties)
        packager.puzzle_to_html(self.puzzle)
        # html = packager.puzzle_to_html(self.puzzle)
        # print("-------------------------")
        # print(html)
        # print("-------------------------")
        packager.write_puzzle(self.puzzle)


class TestSolutionPackager(unittest.TestCase):
    def setUp(self):
        self.properties = Properties()
        self.utility = PuzzleUtility(self.properties)
        self.packager = SolutionPackager(self.properties, self.utility)

    def get_test_puzzle(self):
        puzzle = Puzzle()
        puzzle.puzzle_rows.append("ABCPRACTICELM")
        puzzle.puzzle_rows.append("ABCDEFBUBBLEM")
        puzzle.puzzle_rows.append("ABCCANDLEJKLM")
        puzzle.puzzle_rows.append("ABCDEBANANALM")
        return puzzle

    def get_test_answerkey(self):
        answerkey = AnswerKey()
        answerkey.answers['a'] = 'banana'
        answerkey.answers['b'] = 'bubble'
        answerkey.answers['c'] = 'practice'
        answerkey.answers['d'] = 'candle'
        return answerkey

    def test_puzzle_to_string(self):
        puzzle = self.get_test_puzzle()
        answerkey = self.get_test_answerkey()

        output_string = self.packager.puzzle_to_string(puzzle, answerkey)

        self.assertIn(answerkey.answers['a'].upper(), output_string)
        self.assertIn(answerkey.answers['b'].upper(), output_string)
        self.assertIn(answerkey.answers['c'].upper(), output_string)
        self.assertIn(answerkey.answers['d'].upper(), output_string)

    def test_get_answerkey_filename(self):
        expected_filename = "no_timestamp.txt"
        self.packager.properties.answerkey_txt_name = expected_filename

        actual_filepath = self.packager.get_answerkey_filename()
        expected_filepath = os.path.join(self.packager.properties.dir_of_answer_keys, expected_filename)
        self.assertEqual(expected_filepath, actual_filepath)

    def test_get_answerkey_filename_with_timestamp(self):
        expected_filename = "timestamp_{}.txt"
        self.packager.properties.answerkey_txt_name = expected_filename

        actual_filepath = self.packager.get_answerkey_filename()
        expected_filepath = os.path.join(self.packager.properties.dir_of_answer_keys, expected_filename)
        self.assertNotEqual(expected_filepath, actual_filepath)
        self.assertIn("timestamp_", actual_filepath)

    def integration_test_write_solution(self):
        puzzle = self.get_test_puzzle()
        answerkey = self.get_test_answerkey()

        self.packager.write_solution(puzzle, answerkey)
        self.assertEqual(1, 1)
















































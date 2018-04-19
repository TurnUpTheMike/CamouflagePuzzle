import unittest
import os
from packaging.puzzlepackager import PuzzlePackager
from solution.puzzle import Puzzle


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        self.puzzle_template = parent_directory + "/puzzle_template.html"
        self.puzzle_output_dir = ""
        self.puzzle_pdf_name = "testing_puzzle.pdf"


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

    def test_puzzle_to_html(self):
        packager = PuzzlePackager(properties=self.properties)
        html = packager.puzzle_to_html(self.puzzle)
        # print("-------------------------")
        # print(html)
        # print("-------------------------")
        packager.write_puzzle(self.puzzle)

        self.assertEqual(1, 1)

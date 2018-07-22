from solution.puzzle import Puzzle
from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles


class PuzzleValidator:
    def __init__(self, wordbank, puzzle):
        self.puzzle = puzzle
        self.wordbank = wordbank

    def is_valid_puzzle(self):
        print("Inside is_valid_puzzle")

        print("--------------------------------")
        return True

    def possible_solutions_for_row(self, puzzle_row):
        solutions = []
        return solutions

    def validator_error_details(self):
        print_messages = [
            "The Puzzle is not valid",
            "-----------------------------"
        ]
        return "\n".join(print_messages)

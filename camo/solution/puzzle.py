import string
import random
from solution.puzzleutility import PuzzleUtility


class Puzzle:
    def __init__(self):
        self.puzzle_rows = []

    def print_puzzle(self):
        print("----------{}---------".format(self.__class__.__name__))
        for row in self.puzzle_rows:
            print(row)
        print("---------------------------")


class PuzzleGenerator:
    def __init__(self, properties, utility):
        self.properties = properties
        self.util = utility

    def generate_puzzle(self, answerkey):
        puzzle = Puzzle()

        for letter in "abcdefghijklmnopqrstuvwxyz":
            word = answerkey.answers[letter]
            puzzle_row_text = self.create_puzzle_row(letter, word)
            puzzle.puzzle_rows.append(puzzle_row_text)

        # Randomize the rows
        random.shuffle(puzzle.puzzle_rows)

        return puzzle

    def create_puzzle_row(self, letter, word):
        word_length = len(word)
        letter_index = self.util.letter_ndx_of_word(word, letter)

        left_padding = self.create_left_padding(letter_index)
        right_padding = self.create_right_padding(letter_index, word_length)
        puzzle_pieces = [left_padding, word, right_padding]

        row_text = ''.join(puzzle_pieces)
        return row_text.upper()

    def create_left_padding(self, letter_index):
        padding_length = self.util.chosen_letter_index - letter_index
        if padding_length <= 0:
            return ''

        return self.create_padding_text_of_length(padding_length)

    def create_right_padding(self, letter_index, word_length):
        padding_length = self.util.chosen_letter_index - (word_length - 1 - letter_index)
        if padding_length <= 0:
            return ''

        return self.create_padding_text_of_length(padding_length)

    def create_padding_text_of_length(self, padding_length):
        text = []
        for x in range(0, padding_length):
            text.append(self.create_letter_to_append())
        return ''.join(text)

    def create_letter_to_append(self):
        return random.choice(string.ascii_uppercase)

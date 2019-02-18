from solution.puzzle import PuzzleGenerator
import random


class PuzzleLetterStats(PuzzleGenerator):
    def __init__(self, properties, utility):
        super().__init__(properties, utility)
        # Create a letter bank that represents letter counts by letter frequency statistics
        self.letter_bank_default = 'EEEEEEEEEEEAAAAAAAAARRRRRRRIIIIIIIOOOOOOOTTTTTTNNNNNNSSSSSLLLLLCCCCUUUDDDPPPMMMHHHGGBBFFYWKV'
        self.letter_bank = self.letter_bank_default

    def reset_letter_bank(self):
        self.letter_bank = self.letter_bank_default

    def create_puzzle_row(self, letter, word, answerkey):
        word_length = len(word)
        letter_index = answerkey.letter_ndx_of_word(word, letter, self.util.chosen_letter_index)

        left_padding = self.create_left_padding(letter_index)
        self.reset_letter_bank()
        right_padding = self.create_right_padding(letter_index, word_length)
        puzzle_pieces = [left_padding, word, right_padding]

        row_text = ''.join(puzzle_pieces)
        return row_text.upper()

    def create_letter_to_append(self):
        letter_choice = random.choice(self.letter_bank)
        self.letter_bank = self.letter_bank.replace(letter_choice, '')
        return letter_choice

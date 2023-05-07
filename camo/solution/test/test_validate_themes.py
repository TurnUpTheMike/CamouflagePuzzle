import unittest
import os
from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles
from solution.puzzleutility import PuzzleUtility
from solution.answerkeypants import AnswerKeyGeneratorTheme
from camouflage import Camouflage

class Properties:
    def __init__(self):
        cwd = os.path.dirname(os.path.abspath(__file__)) + '/../..'
        # needed for the wordbank
        self.puzzle_row_length = Camouflage.PUZZLE_ROW_LENGTH
        self.dir_negative_bank = cwd + Camouflage.DEFAULT_DIR_NEGATIVE_BANK
        self.dir_of_word_bank_src = cwd + Camouflage.DEFAULT_DIR_WORD_BANK_SRCS
        # needed for answerkeygenerator
        self.rows_to_obscure = 10
        self.dir_of_theme = cwd + Camouflage.THEME_DIRECTIORY
        self.theme = Camouflage.DEFAULT_THEME_NAME
        self.min_word_length = Camouflage.MIN_WORD_LENGTH
        self.max_word_length = Camouflage.MAX_WORD_LENGTH
        

"""
    These are integration tests that validate the format of the lib/theme directory
"""
class TestValidateThemes(unittest.TestCase):
    
    def setUp(self) -> None:
        self.properties = Properties()
        return super().setUp()
    
    def test_validate_themes(self):
        print("Validate Themes")

        wordbank_generator = WordBankGeneratorFlatFiles(self.properties)
        wordbank = wordbank_generator.generate_word_bank()

        puzzle_util = PuzzleUtility(self.properties)
        
        answerkey_generator = AnswerKeyGeneratorTheme(self.properties, puzzle_util)
        answerkey_generator.flag_match_counts = False
        
        # Test just one theme
        #self.assert_valid_theme(answerkey_generator, wordbank, 'retirement_theme.csv')

        # Test all of the themes in the theme directory
        for _, _, files in os.walk(self.properties.dir_of_theme):
            for filename in files:
                self.assert_valid_theme(answerkey_generator, wordbank, filename)
                print(f'Theme {filename} is valid')
        
        print('All Themes Valid')
        
    def assert_valid_theme(self, answerkey_generator, wordbank, theme_filename):
        self.properties.theme = theme_filename
        answerkey = answerkey_generator.generate_answer_key(wordbank)
        #answerkey.print_answerkey()

        # Every letter in the answerkey has a word
        for letter in "abcdefghijklmnopqrstuvwxyz":
            self.assertIn(letter, answerkey.answers_unmodified, f'Letter {letter} is missing in theme {theme_filename}')
            self.assertIn(answerkey.answers[letter], answerkey.letter_ndx_lookup)

        # Some of the words were obscured
        rows_obscured = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if answerkey.answers_unmodified[letter] != answerkey.answers[letter]:
                rows_obscured = rows_obscured + 1

        #print(f'rows obscured {rows_obscured}')
        self.assertGreater(rows_obscured, 0)

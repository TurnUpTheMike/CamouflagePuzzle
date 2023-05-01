import argparse
import os
from wordbank.wordbankgenerator import WordBankGeneratorHardCoded
from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles
from wordbank.alangenerator import WordBankGeneratorAlan
from wordbank.wordbank import Discriminator
from solution.answerkey import AnswerKeyGenerator
from solution.answerkeypants import AnswerKeyGeneratorPants, AnswerKeyGeneratorTheme
from solution.puzzle import PuzzleGenerator
from solution.puzzleletterstats import PuzzleLetterStats
from packaging.puzzlepackager import PuzzlePackager, SolutionPackager
from solution.puzzleutility import PuzzleUtility
from validator.validator import PuzzleValidator


class Camouflage:
    DEFAULT_DIR_ANSWER_KEYS = "/out/answer_keys"
    DEFAULT_DIR_NEGATIVE_BANK = "/out/negativebank"
    DEFAULT_DIR_WORD_BANK_SRCS = "/lib/word_bank_src"
    MIN_WORD_LENGTH = 5
    MAX_WORD_LENGTH = 10
    PUZZLE_ROW_LENGTH = 13
    DEFAULT_WORD_BANK_GENERATOR = 'flatfiles'
    DEFAULT_ANSWER_KEY_GENERATOR = 'pants'
    DEFAULT_PUZZLE_GENERATOR = 'singleletterstats'
    DEFAULT_PUZZLE_PACKAGER = 'pdf'
    DEFAULT_SOLUTION_PACKAGER = 'txt'
    PUZZLE_TEMPLATE = "/packaging/puzzle_template.html"
    DEFAULT_PUZZLE_OUTPUT_DIR = "./out/puzzles_to_play"  # current working director
    PUZZLE_PDF_NAME = "puzzle_{}.pdf"
    ANSWERKEY_TXT_NAME = "answerkey_{}.txt"
    GENERATOR_ROWS_OBSCURED = 10
    THEME_DIRECTIORY = "./lib/theme"
    DEFAULT_THEME_NAME = "theme_name.csv"

    def __init__(self):
        self.util = None

    def run(self):
        args = self.create_argument_parser()

        print("------ARGS-----")
        print(args)
        print("---------------")
        self.util = PuzzleUtility(args)

        wordbank_generator = self.get_wordbank_generator(args)
        wordbank = wordbank_generator.generate_word_bank()
        if args.display_wordbank:
            wordbank.print_wordbank()

        answerkey_generator = self.get_answerkey_generator(args)
        answerkey = answerkey_generator.generate_answer_key(wordbank)
        answerkey.print_answerkey()

        puzzle_generator = self.get_puzzle_generator(args)
        puzzle = puzzle_generator.generate_puzzle(answerkey)
        puzzle.print_puzzle()

        puzzle_validator = PuzzleValidator(properties=args, wordbank=wordbank, utility=self.util)
        if puzzle_validator.is_valid_puzzle(puzzle=puzzle, answerkey=answerkey) is False:
            print(puzzle_validator.validator_error_details())
            puzzle.print_puzzle_for_test()
            answerkey.print_answerkey_for_test()
            return

        if args.do_package_puzzle:
            print("Packaging Puzzle artifacts")
            solution_packager = self.get_solution_packager(args)
            solution_packager.write_solution(puzzle, answerkey)
            packaging_service = self.get_puzzle_packager(args)
            packaging_service.write_puzzle(puzzle)
        else:
            print("No artifacts created")

    def create_argument_parser(self):
        parser = argparse.ArgumentParser(description='Camoflauge Puzzle',
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        cwd = os.path.dirname(os.path.abspath(__file__))

        # Puzzle Characteristics
        parser.add_argument('--min-word-length', dest='min_word_length', type=bool,
                            default=Camouflage.MIN_WORD_LENGTH)
        parser.add_argument('--max-word-length', dest='max_word_length',
                            default=Camouflage.MAX_WORD_LENGTH)
        parser.add_argument('--puzzle-row-length', dest='puzzle_row_length',
                            default=Camouflage.PUZZLE_ROW_LENGTH)

        # Generator choices
        parser.add_argument('--bank-generator', dest="bank_generator", type=str,
                            help="options: hardcoded | flatfiles | alan",
                            default=Camouflage.DEFAULT_WORD_BANK_GENERATOR)
        parser.add_argument('--answerkey-generator', dest="answer_key_generator", type=str,
                            help="options: azfirstitem | pants",
                            default=Camouflage.DEFAULT_ANSWER_KEY_GENERATOR)
        parser.add_argument('--puzzle-generator', dest="puzzle_generator", type=str,
                            help="options: randompadding, singleletterstats",
                            default=Camouflage.DEFAULT_PUZZLE_GENERATOR)
        parser.add_argument('--puzzle-packager', dest="puzzle_packager", type=str,
                            help="options: pdf",
                            default=Camouflage.DEFAULT_PUZZLE_PACKAGER)
        parser.add_argument('--solution-packager', dest="solution_packager", type=str,
                            help="options: txt",
                            default=Camouflage.DEFAULT_PUZZLE_PACKAGER)

        # Input Sources
        parser.add_argument('--dir-answer-keys', dest='dir_of_answer_keys', type=str,
                            default=cwd + Camouflage.DEFAULT_DIR_ANSWER_KEYS,
                            help="The directory where answer keys are written to")
        parser.add_argument('--dir-word-bank', dest='dir_of_word_bank_src', type=str,
                            default=cwd + Camouflage.DEFAULT_DIR_WORD_BANK_SRCS,
                            help="A directory where word bank text sources are read from")
        parser.add_argument('--dir-negative-bank', dest='dir_negative_bank', type=str,
                            default=cwd + Camouflage.DEFAULT_DIR_NEGATIVE_BANK,
                            help="A directory of text sources to exclude words from the bank")
        parser.add_argument('--puzzle-template', dest='puzzle_template', type=str,
                            default=cwd + Camouflage.PUZZLE_TEMPLATE,
                            help="The html file that is a template for the puzzle output")
        parser.add_argument('--theme', dest='theme', type=str,
                            default=Camouflage.DEFAULT_THEME_NAME,
                            help="theme_name.csv should be found in the /lib/theme/ directory")
        parser.add_argument('--theme-dir', dest='dir_of_theme', type=str,
                            default=Camouflage.THEME_DIRECTIORY,
                            help="/lib/theme")

        # Output Sources
        parser.add_argument('--puzzle-output-dir', dest='puzzle_output_dir', type=str,
                            default=Camouflage.DEFAULT_PUZZLE_OUTPUT_DIR,
                            help="The directory to write the pdf puzzle to")
        parser.add_argument('--puzzle-pdf-name', dest='puzzle_pdf_name', type=str,
                            default=Camouflage.PUZZLE_PDF_NAME,
                            help="The name of the pdf to create")
        parser.add_argument('--answerkey-txt-name', dest='answerkey_txt_name', type=str,
                            default=Camouflage.ANSWERKEY_TXT_NAME,
                            help="The name of the txt to create for the answerkey")

        # Generator Specific Flags
        parser.add_argument('--rows-obscured', dest="rows_to_obscure", type=str,
                            help="number: 0 - 26",
                            default=Camouflage.GENERATOR_ROWS_OBSCURED)

        # Debug Flags
        parser.add_argument('--do-package-puzzle', action='store_true',
                            help="Will create a pdf of the puzzle")
        parser.add_argument('--display-wordbank', action='store_true',
                            help="Whether to print the wordbank to the console")
        parser.add_argument('--environment-home', action='store_false',
                            help="true: windows   false: linux")

        arguments = parser.parse_args()
        return arguments

    def get_wordbank_generator(self, args):
        """
        A factory method to create an instance of a WordBankGenerator
        :param args:
        :return: WordBankGeneratorBase
        """

        if args.bank_generator == 'hardcoded':
            return WordBankGeneratorHardCoded(args)
        elif args.bank_generator == 'flatfiles':
            return WordBankGeneratorFlatFiles(args)
        elif args.bank_generator == 'alan':
            discriminator = Discriminator(min_length=args.min_word_length, max_length=args.max_word_length)
            return WordBankGeneratorAlan(args, discriminator)

        return WordBankGeneratorHardCoded(args)

    def get_answerkey_generator(self, args):
        """
        A factory method to create an instance of an AnswerKeyGenerator
        :param args:
        :return:
        """

        if args.theme != Camouflage.DEFAULT_THEME_NAME:
            return AnswerKeyGeneratorTheme(args, self.util)

        if args.answer_key_generator == 'azfirstitem':
            return AnswerKeyGenerator(args, self.util)
        elif args.answer_key_generator == 'pants':
            return AnswerKeyGeneratorPants(args, self.util)
        elif args.answer_key_generator == 'theme':
            return AnswerKeyGeneratorTheme(args, self.util)

        return AnswerKeyGenerator(args, self.util)

    def get_puzzle_generator(self, args):
        """
        A factory method to create an instance of a PuzzleGenerator
        :param args:
        :return:
        """

        if args.puzzle_generator == 'randompadding':
            return PuzzleGenerator(args, self.util)
        elif args.puzzle_generator == 'singleletterstats':
            return PuzzleLetterStats(args, self.util)

        return PuzzleGenerator(args, self.util)

    def get_puzzle_packager(self, args):
        """
        A factory method to package the puzzle with
        :return:
        """

        if args.puzzle_packager == 'pdf':
            return PuzzlePackager(args)

        return PuzzlePackager(args)

    def get_solution_packager(self, args):
        """
        A factory method to package the answerkey with
        :return:
        """

        if args.puzzle_packager == 'txt':
            return SolutionPackager(args, self.util)

        return SolutionPackager(args, self.util)


if __name__ == '__main__':
    print("Starting Camoflauge Puzzle Creator")

    camouflage = Camouflage()
    camouflage.run()

    print("El Fin")

import argparse
import os
from wordbank.wordbankgenerator import WordBankGeneratorHardCoded
from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles
from wordbank.alangenerator import WordBankGeneratorAlan
from wordbank.wordbank import Discriminator
from solution.answerkey import AnswerKey, AnswerKeyGenerator
from solution.puzzle import Puzzle, PuzzleGenerator
from packaging.puzzlepackager import PuzzleToPDF
from solution.puzzleutility import PuzzleUtility


class Camoflague:
    DEFAULT_DIR_ANSWER_KEYS = "/out/answer_keys"
    DEFAULT_DIR_WORD_BANK_SRCS = "/lib/word_bank_src"
    MIN_WORD_LENGTH = 5
    MAX_WORD_LENGTH = 10
    PUZZLE_ROW_LENGTH = 13
    DEFAULT_WORD_BANK_GENERATOR = 'hardcoded'
    DEFAULT_ANSWER_KEY_GENERATOR = 'azfirstitem'
    DEFAULT_PUZZLE_GENERATOR = 'randompadding'
    DEFAULT_PUZZLE_PACKAGER = 'pdf'
    PUZZLE_TEMPLATE = "/packaging/puzzle_template.html"
    DEFAULT_PUZZLE_OUTPUT_DIR = ""  # current working director
    PUZZLE_PDF_NAME = "testing_puzzle.pdf"

    def run(self):
        args = self.create_argument_parser()

        print("------ARGS-----")
        print(args)
        print("---------------")

        wordbank_generator = self.get_wordbank_generator(args)
        wordbank = wordbank_generator.generate_word_bank()
        wordbank.print_wordbank()

        answerkey_generator = self.get_answerkey_generator(args)
        answerkey = answerkey_generator.generate_answer_key(wordbank)
        answerkey.print_answerkey()

        puzzle_generator = self.get_puzzle_generator(args)
        puzzle = puzzle_generator.generate_puzzle(answerkey)
        puzzle.print_puzzle()

        packaging_service = self.get_puzzle_packager(args)
        packaging_service.write_puzzle(puzzle)

    def create_argument_parser(self):
        parser = argparse.ArgumentParser(description='Camoflauge Puzzle',
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        cwd = os.path.dirname(os.path.abspath(__file__))

        # Puzzle Characteristics
        parser.add_argument('--min-word-length', dest='min_word_length', type=bool,
                            default=Camoflague.MIN_WORD_LENGTH)
        parser.add_argument('--max-word-length', dest='max_word_length',
                            default=Camoflague.MAX_WORD_LENGTH)
        parser.add_argument('--puzzle-row-length', dest='puzzle_row_length',
                            default=Camoflague.PUZZLE_ROW_LENGTH)

        # Generator choices
        parser.add_argument('--bank-generator', dest="bank_generator", type=str,
                            help="options: hardcoded | flatfiles | alan",
                            default=Camoflague.DEFAULT_WORD_BANK_GENERATOR)
        parser.add_argument('--answerkey-generator', dest="answer_key_generator", type=str,
                            help="options: azfirstitem",
                            default=Camoflague.DEFAULT_ANSWER_KEY_GENERATOR)
        parser.add_argument('--puzzle-generator', dest="puzzle_generator", type=str,
                            help="options: azfirstitem",
                            default=Camoflague.DEFAULT_PUZZLE_GENERATOR)
        parser.add_argument('--puzzle-packager', dest="puzzle_packager", type=str,
                            help="options: azfirstitem",
                            default=Camoflague.DEFAULT_PUZZLE_PACKAGER)

        # Input Sources
        parser.add_argument('--dir-answer-keys', dest='dir_of_answer_keys', type=str,
                            default=cwd + Camoflague.DEFAULT_DIR_ANSWER_KEYS,
                            help="The directory where answer keys are written to")
        parser.add_argument('--dir-word-bank', dest='dir_of_word_bank_src', type=str,
                            default=cwd + Camoflague.DEFAULT_DIR_WORD_BANK_SRCS,
                            help="A directory where word bank text sources are read from")
        parser.add_argument('--puzzle-template', dest='puzzle_template', type=str,
                            default=cwd + Camoflague.PUZZLE_TEMPLATE,
                            help="The html file that is a template for the puzzle output")

        # Output Sources
        parser.add_argument('--puzzle-output-dir', dest='puzzle_output_dir', type=str,
                            default=Camoflague.DEFAULT_PUZZLE_OUTPUT_DIR,
                            help="The directory to write the pdf puzzle to")
        parser.add_argument('--puzzle-pdf-name', dest='puzzle_pdf_name', type=str,
                            default=Camoflague.PUZZLE_PDF_NAME,
                            help="The name of the pdf to create")

        # Debug Flags
        parser.add_argument('--do-package-puzzle', action='store_true',
                            help="Will create a pdf of the puzzle")

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
        util = PuzzleUtility(args)

        if args.answer_key_generator == 'azfirstitem':
            return AnswerKeyGenerator(args, util)

        return AnswerKeyGenerator(args, util)

    def get_puzzle_generator(self, args):
        """
        A factory method to create an instance of a PuzzleGenerator
        :param args: 
        :return: 
        """
        util = PuzzleUtility(args)

        if args.puzzle_generator == 'randompadding':
            return PuzzleGenerator(args, util)

        return PuzzleGenerator(args, util)

    def get_puzzle_packager(self, args):
        """
        A factory method to package the puzzle with
        :return: 
        """

        if args.puzzle_packager == 'pdf':
            return PuzzleToPDF(args)

        return PuzzleToPDF(args)

if __name__ == '__main__':
    print("Starting Camoflauge Puzzle Creator")

    camoflague = Camoflague()
    camoflague.run()

    print("El Fin")

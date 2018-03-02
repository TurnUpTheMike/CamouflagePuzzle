import argparse
import os
from wordbank.wordbankgenerator import WordBankGeneratorHardCoded
from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles


class Camoflague:
    DEFAULT_DIR_ANSWER_KEYS = "/out/answer_keys"
    DEFAULT_DIR_WORD_BANK_SRCS = "/lib/word_bank_src"
    MIN_WORD_LENGTH = 5
    MAX_WORD_LENGTH = 10
    PUZZLE_LINE_LENGTH = 13
    DEFAULT_WORD_BANK_GENERATOR = 'flatfiles'

    def run(self):
        args = self.create_argument_parser()

        print("------ARGS-----")
        print(args)
        print("---------------")

        wordbank_generator = self.get_word_bank_generator(args)
        wordbank = wordbank_generator.generate_word_bank()

        # print("----------WORD BANK---------")
        # print(wordbank.hash_by_letter)
        # print("----------------------------")

    def create_argument_parser(self):
        parser = argparse.ArgumentParser(description='Camoflauge Puzzle',
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        cwd = os.path.dirname(os.path.abspath(__file__))

        parser.add_argument('--min-word-length', dest='min_word_length', type=bool,
                            default=Camoflague.MIN_WORD_LENGTH)
        parser.add_argument('--max-word-length', dest='max_word_length',
                            default=Camoflague.MAX_WORD_LENGTH)
        parser.add_argument('--puzzle-row-length', dest='puzzle_row_length',
                            default=Camoflague.PUZZLE_LINE_LENGTH)
        parser.add_argument('--bank-generator', dest="bank_generator", type=str,
                            help="options: hardcoded | flatfiles",
                            default=Camoflague.DEFAULT_WORD_BANK_GENERATOR)
        parser.add_argument('--dir-answer-keys', dest='dir_of_answer_keys', type=str,
                            default=cwd + Camoflague.DEFAULT_DIR_ANSWER_KEYS,
                            help="The directory where answer keys are written to")
        parser.add_argument('--dir-word-bank', dest='dir_of_word_bank_src', type=str,
                            default=cwd + Camoflague.DEFAULT_DIR_WORD_BANK_SRCS,
                            help="A directory where word bank text sources are read from")

        arguments = parser.parse_args()
        return arguments

    def get_word_bank_generator(self, args):
        """
        A factory method to create an instance of a WordBankGenerator
        :param args:
        :return: WordBankGeneratorBase
        """

        if args.bank_generator == 'flatfiles':
            return WordBankGeneratorFlatFiles(args)

        return WordBankGeneratorHardCoded(args)

if __name__ == '__main__':
    print("Starting Camoflauge Puzzle Creator")

    camoflague = Camoflague()
    camoflague.run()

    print("El Fin")

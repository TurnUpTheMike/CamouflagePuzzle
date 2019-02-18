import os
import re
from wordbank.wordbankgenerator import WordBankGeneratorBase
from wordbank.wordbank import WordBank


class WordBankGeneratorFlatFiles(WordBankGeneratorBase):
    def __init__(self, properties):
        super().__init__(properties)
        self.word_bank = None
        self.negative_word_bank = set()
        self.verbose = True

    def generate_word_bank(self):
        self.create_negative_word_bank(self.properties.dir_negative_bank)

        self.word_bank = WordBank(self.properties)
        self.read_word_bank_sources(self.properties.dir_of_word_bank_src)

        return self.word_bank

    def read_word_bank_sources(self, dir_word_bank_src):
        for path, dirs, files in os.walk(dir_word_bank_src):
            for filename in files:
                if self.is_valid_source_file_name(filename):
                    self.verbose_print("Reading file " + os.path.join(path, filename))
                    self.read_source_file(os.path.join(path, filename))

    def read_source_file(self, filename):
        with open(filename, "r") as file_handle:
            file_contents = file_handle.read()
            for original_word in file_contents.split():
                word = self.format_word(original_word)

                if word not in self.negative_word_bank:
                    self.negative_word_bank.add(word)
                    self.word_bank.add_word(word)

    def format_word(self, word):
        """
        Takes the input word and formats it to a word that can be in an answer key
        """
        lowered_word = word.lower()
        lettered_word = re.sub("[^a-z]", "", lowered_word)
        return lettered_word

    def create_negative_word_bank(self, dir_answer_keys):
        """
        Clears the negative_word_bank
        Populates the negative_word_bank from the dir_of_answer_keys
        :return:
        """
        self.negative_word_bank = set()

        for path, dirs, files in os.walk(dir_answer_keys):
            for filename in files:
                if self.is_valid_source_file_name(filename):
                    self.read_negative_word_bank_file(os.path.join(path, filename))

    def read_negative_word_bank_file(self, filename):
        """
        Reads a file
        Formats each word
        Adds it to the negative_word_bank
        """
        with open(filename, "r") as file_handle:
            file_contents = file_handle.read()
            for word in file_contents.split():
                formatted_word = self.format_word(word)
                self.negative_word_bank.add(formatted_word)

    def is_valid_source_file_name(self, filename):
        """
        the filename is a text file that we can read words out of
        """
        return filename.endswith(".txt")

    def verbose_print(self, msg):
        if self.verbose:
            print(msg)

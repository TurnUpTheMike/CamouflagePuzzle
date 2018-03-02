import os
import re
from wordbank.wordbankgenerator import WordBankGeneratorBase
from wordbank.wordbank import WordBank


class WordBankGeneratorFlatFiles(WordBankGeneratorBase):
    def __init__(self, app_properties):
        super().__init__(app_properties)
        self.word_bank = None
        self.negative_word_bank = None

    def generate_word_bank(self):
        print("Enter FlatFiles Generator")
        self.create_negative_word_bank(self.properties.dir_of_answer_keys)

        print("--------Negative Bank---------")
        print(self.negative_word_bank)
        print("------------------------------")

        self.read_word_bank_sources(self.properties.dir_of_word_bank_src)

        self.word_bank = self.populate_test_word_bank()
        return self.word_bank

    def populate_test_word_bank(self):
        bank = WordBank(app_properties=self.properties)
        bank.hash_by_letter = {
            'a': ['banana'],
            'b': ['bubble'],
            'c': ['practice'],
            'd': ['candle'],
            'e': ['treacherous'],
            'f': ['perfect'],
            'g': ['laugh'],
            'h': ['beach'],
            'i': ['guitar'],
            'j': ['trajectory'],
            'k': ['blanket'],
            'l': ['color'],
            'm': ['smile'],
            'n': ['stamina'],
            'o': ['blood'],
            'p': ['partner'],
            'r': ['quilt'],
            'q': ['morning'],
            's': ['respect'],
            't': ['flatten'],
            'u': ['hundred'],
            'v': ['alive'],
            'w': ['below'],
            'x': ['expert'],
            'y': ['player'],
            'z': ['zebra']
        }
        return bank

    def read_word_bank_sources(self, dir_word_bank_src):
        for path, dirs, files in os.walk(dir_word_bank_src):
            for filename in files:
                if self.is_valid_source_file_name(filename):
                    print("Reading file " + os.path.join(path, filename))
                    self.read_source_file(os.path.join(path, filename))

    def read_source_file(self, filename):
        file_handle = open(filename, "r")
        file_contents = file_handle.read()
        for original_word in file_contents.split():
            word = self.format_word(original_word)

            if word not in self.negative_word_bank:
                self.negative_word_bank[word] = True
                print("Adding Word " + word)

    def format_word(self, word):
        """
        Takes the input word and formats it to a word that can be in an answer key
        :param word: 
        :return: 
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
        self.negative_word_bank = {}

        for path, dirs, files in os.walk(dir_answer_keys):
            for filename in files:
                if self.is_valid_source_file_name(filename):
                    self.read_negative_word_bank_file(os.path.join(path, filename))

    def read_negative_word_bank_file(self, filename):
        """
        Reads a file
        Formats each word
        Adds it to the negative_word_bank
        :param filename: 
        :return: 
        """
        file_handle = open(filename, "r")
        file_contents = file_handle.read()
        for word in file_contents.split():
            formatted_word = self.format_word(word)
            self.negative_word_bank[formatted_word] = True

    def is_valid_source_file_name(self, filename):
        """
        the filename is a text file that we can read words out of
        :param filename: 
        :return: 
        """
        return filename.endswith(".txt")

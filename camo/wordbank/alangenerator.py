from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles
from wordbank.wordbank import WordBankAlan


class WordBankGeneratorAlan(WordBankGeneratorFlatFiles):
    def __init__(self, app_properties, discriminator):
        super().__init__(app_properties)
        self.word_bank = None
        self.discriminator = discriminator

    def generate_word_bank(self):
        print("Enter WordBankGeneratorAlan")
        self.create_negative_word_bank(self.properties.dir_of_answer_keys)

        self.word_bank = WordBankAlan(self.discriminator, self.properties.puzzle_row_length)
        self.read_word_bank_sources(self.properties.dir_of_word_bank_src)

        return self.word_bank

    def read_source_file(self, filename):
        file_handle = open(filename, "r")
        file_contents = file_handle.read()
        for original_word in file_contents.split():
            word = self.format_word(original_word)
            self.word_bank.add_word(word)

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
            self.discriminator.is_valid_word(formatted_word)


class WordBank:

    def __init__(self, properties):
        self.properties = properties
        self.unique_words = set()
        self.hash_by_letter = {i: set() for i in "abcdefghijklmnopqrstuvwxyz"}
        self.chosen_letter_position = self.properties.puzzle_row_length / 2

    def add_word(self, word):
        if not self.is_valid_word(word):
            return

        self.unique_words.add(word)
        word_length = len(word)

        for ndx, letter in enumerate(word):
            if word_length - ndx > self.chosen_letter_position:
                continue   # the word is too long for a letter this early in the word

            if ndx > self.chosen_letter_position:
                continue   # the word is too long for a letter this far back in the word

            self.hash_by_letter[letter].add(word)

    def is_valid_word(self, word):
        if len(word) < self.properties.min_word_length:
            return False

        if len(word) > self.properties.max_word_length:
            return False

        if word in self.unique_words:
            return False

        return True

    def remove_word(self, word):
        """
        Remove a word from the wordbank
        :param word: 
        :return: 
        """
        for letter in word:
            if word in self.hash_by_letter[letter]:
                self.hash_by_letter[letter].remove(word)

    def print_wordbank(self):
        print("------------{}-----------".format(self.__class__.__name__))
        for letter in "abcdefghijklmnopqrstuvwxyz":
            print("{}: {}".format(letter, self.hash_by_letter[letter]))
        print("--------------------------------------")


class WordBankAlan():
    def __init__(self, discriminator, puzzle_line_length):
        self.discriminator = discriminator
        self.chosen_letter_position = puzzle_line_length / 2
        self.hash_by_letter = {i: set() for i in "abcdefghijklmnopqrstuvwxyz"}

    def add_word(self, word):
        if not self.discriminator.is_valid_word(word):
            return

        word_length = len(word)
        for ndx, letter in enumerate(word):
            if word_length - ndx > self.chosen_letter_position:
                continue   # the word is too long for a letter this early in the word

            if ndx > self.chosen_letter_position:
                continue   # the word is too long for a letter this far back in the word

            self.hash_by_letter[letter].add(word)

    def remove_word(self, word):
        """
        Remove a word from the wordbank
        :param word: 
        :return: 
        """
        for letter in word:
            if word in self.hash_by_letter[letter]:
                self.hash_by_letter[letter].remove(word)

    def print_wordbank(self):
        print("------------{}-----------".format(self.__class__.__name__))
        for letter in "abcdefghijklmnopqrstuvwxyz":
            print("{}: {}".format(letter, self.hash_by_letter[letter]))
        print("--------------------------------------")


class Discriminator:
    def __init__(self, *, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        self.seen = set()

    def is_valid_word(self, word):
        if len(word) < self.min_length:
            return False

        if len(word) > self.max_length:
            return False

        if word in self.seen:
            return False

        self.seen.add(word)
        return True

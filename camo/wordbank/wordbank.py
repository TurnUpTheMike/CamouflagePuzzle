
class WordBank:

    def __init__(self, app_properties):
        self.properties = app_properties
        self.unique_words = set()
        self.hash_by_letter = {i: [] for i in "abcdefghijklmnopqrstuvwxyz"}

    def add_word(self, word):
        if not self.is_valid_word(word):
            return

        self.unique_words.add(word)
        chosen_letter_position = self.properties.puzzle_row_length / 2
        word_length = len(word)

        for ndx, letter in enumerate(word):
            if word_length - ndx > chosen_letter_position:
                continue   # the word is too long for a letter this early in the word

            if ndx > chosen_letter_position:
                continue   # the word is too long for a letter this far back in the word

            self.hash_by_letter[letter].append(word)

    def is_valid_word(self, word):
        if len(word) < self.properties.min_word_length:
            return False

        if len(word) > self.properties.max_word_length:
            return False

        if word in self.unique_words:
            return False

        return True


class PuzzleUtility:
    """
    These are common functions that multiple classes use
    """

    def __init__(self, properties):
        self.properties = properties

        # which column of the puzzle row grid that the "chosen letter" will appear
        self.chosen_letter_index = self.properties.puzzle_row_length // 2

    def letter_ndx_of_word(self, word, letter):
        """
        the earliest letter in the word that the letter exists
        more than word.find this accounts for long words where the letter might not fit at the beginning of the word  
        :param word: 
        :param letter: 
        :return: 
        """
        word_length = len(word)
        earliest_index = self.earliest_possible_index_choice(word_length)
        letter_index = word.find(letter, earliest_index)
        return letter_index

    def earliest_possible_index_choice(self, word_length):
        """
        The word may be too long for the chosen letter to fit every letter index
        This is the earliest index of the word that the chosen letter can be
        :param word_length: 
        :return: 
        """
        if self.chosen_letter_index > word_length - 1:
            return 0

        return (word_length - 1) - self.chosen_letter_index

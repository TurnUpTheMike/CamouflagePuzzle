

class AnswerKey:
    def __init__(self):
        self.answers = {}

    def print_answerkey(self):
        print("------------{}-----------".format(self.__class__.__name__))
        for letter in "abcdefghijklmnopqrstuvwxyz":
            print("{}: {}".format(letter, self.answers[letter]))
        print("--------------------------------------")

    def print_answerkey_for_test(self):
        print("-----------AnswerKey for test----------")
        print("answers = {")
        for letter in "abcdefghijklmnopqrstuvwxyz":
            print("\"{}\": \"{}\",".format(letter, self.get_answer_for_letter(letter)))
        print("}")

    def get_answer_for_letter(self, letter):
        return self.answers[letter]

    def letter_ndx_of_word(self, word, letter, chosen_letter_index):
        """
        the earliest letter in the word that the letter exists
        more than word.find this accounts for long words where the letter might not fit at the beginning of the word
        :param word:
        :param letter:
        :param chosen_letter_index:
        :return:
        """
        word_length = len(word)
        earliest_index = self.earliest_possible_index_choice(word_length, chosen_letter_index)
        letter_index = word.find(letter, earliest_index)
        return letter_index

    def earliest_possible_index_choice(self, word_length, chosen_letter_index):
        """
        The word may be too long for the chosen letter to fit every letter index
        This is the earliest index of the word that the chosen letter can be
        :param word_length:
        :param chosen_letter_index:
        :return: 
        """
        if chosen_letter_index > word_length - 1:
            return 0

        return (word_length - 1) - self.chosen_letter_index


class AnswerKeyGenerator:
    def __init__(self, properties, utility):
        self.properties = properties
        self.util = utility

    def generate_answer_key(self, wordbank):
        answerkey = AnswerKey()

        for letter in "abcdefghijklmnopqrstuvwxyz":
            letter_set = wordbank.hash_by_letter[letter]
            word = letter_set.pop()
            answerkey.answers[letter] = word
            wordbank.remove_word(word)

        return answerkey

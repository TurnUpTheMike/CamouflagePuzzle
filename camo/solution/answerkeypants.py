from solution.answerkey import AnswerKeyGenerator, AnswerKey
from solution.puzzleutility import PuzzleUtility
import re
import random


class AnswerKeyPants(AnswerKey):
    def __init__(self):
        super().__init__()
        self.answers_unmodified = {}

    def print_answerkey(self):
        print("------------{}-----------".format(self.__class__.__name__))
        for letter in "abcdefghijklmnopqrstuvwxyz":
            print("{}: {} -> {}".format(letter, self.answers_unmodified[letter], self.answers[letter]))
        print("--------------------------------------")

    def get_answer_for_letter(self, letter):
        return "{}".format(self.answers_unmodified[letter])


class AnswerKeyGeneratorPants(AnswerKeyGenerator):
    def __init__(self, properties, utility):
        super().__init__(properties, utility)
        self.flag_verbose = False
        self.flag_match_counts = True
        self.banned_hash = {i: [i] for i in "abcdefghijklmnopqrstuvwxyz"}
        self.letter_list = []
        for letter in "abcdefghijklmnopqrstuvwxyz":
            self.letter_list.append(letter)

    def log(self, message):
        if self.flag_verbose:
            print(message)

    def log_matches(self, message):
        if self.flag_match_counts:
            print(message)

    def generate_answer_key(self, wordbank):
        self.log("AnswerkeyGeneratorPants")
        answerkey = AnswerKeyPants()

        for letter in "abcdefghijklmnopqrstuvwxyz":
            self.log("Choosing letter {}".format(letter))
            letter_set = wordbank.hash_by_letter[letter]
            word = letter_set.pop()
            answerkey.answers[letter] = self.choose_word(letter, word, wordbank)
            answerkey.answers_unmodified[letter] = word
            wordbank.remove_word(word)

        return answerkey

    def choose_word(self, letter, word, wordbank):
        word_matches = self.get_words_that_almost_match(letter, word, wordbank)
        self.log("Chosen ({}) {} had {} matches".format(letter, word, len(word_matches)))
        self.log_matches("Chosen ({}) {} had {} matches".format(letter, word, len(word_matches)))

        if len(word_matches) == 0:
            return word

        # choose a word
        deterrent = self.choose_deterrent_word(word_matches)

        # combine the deterrent with the chosen word
        mashed_word = self.create_mashed_word(letter, word, deterrent)

        # add the chosen-letter-banned-list to the banned list of deterrent's letter to prevent cycles
        self.add_to_banned_list(deterrent, letter)

        # mashup the word and the deterrent word
        return mashed_word

    def add_to_banned_list(self, deterrent, letter):
        self.log(deterrent.re)
        deterrent_letter = deterrent.groups()[1]
        chosen_letter_banned_list = self.banned_hash[letter]
        for banned_letter in chosen_letter_banned_list:
            self.banned_hash[deterrent_letter].append(banned_letter)
            self.log("adding {} to bucket {}".format(banned_letter, deterrent_letter))

    def create_mashed_word(self, letter, word, deterrent):
        """
        combine the word and the deterrent together
        :param letter: 
        :param word: 
        :param deterrent: 
        :return: string
        """
        letter_index = self.util.letter_ndx_of_word(word, letter)
        word_prefix = word[:letter_index]
        word_suffix = word[letter_index + 1:]
        prefix_group = deterrent.groups()[0]
        suffix_group = deterrent.groups()[2]

        prefix_to_use = word_prefix
        if prefix_group.find(word_prefix) > -1:
            prefix_to_use = prefix_group

        suffix_to_use = word_suffix
        if suffix_group.find(word_suffix) > -1:
            suffix_to_use = suffix_group

        mashed_word = "{}{}{}".format(prefix_to_use, letter, suffix_to_use)
        return mashed_word

    def choose_deterrent_word(self, word_matches):
        """
        
        :param word_matches: dictionary of "word": re.match object
        :return: re.match object
        """
        match_values = list(word_matches.values())
        random_index = random.randint(0, len(match_values) - 1)
        deterrent = match_values[random_index]
        return deterrent

    def get_words_that_almost_match(self, letter, word, wordbank):
        """
        Search for word that almost match our <word> to pad the puzzle with
        
        :param letter: the chosen letter of the word
        :param word: the chosen word
        :param wordbank: the wordbank to search in
        :return: a dictionary of  "word": re.match object
        """
        letter_index = self.util.letter_ndx_of_word(word, letter)
        word_prefix = word[:letter_index]
        word_suffix = word[letter_index + 1:]

        self.log("GetWordsThatAlmostMatch {} for the letter {} ".format(word, letter))
        # self.log(word_prefix)
        # self.log(word_suffix)

        prefix_expression = self.generate_prefix_expression(word_prefix)
        # self.log(prefix_expression)
        suffix_expression = self.generate_suffix_expression(word_suffix)
        # self.log(suffix_expression)

        word_length = len(word)
        num_letters_on_left_side = self.util.chosen_letter_index - letter_index
        num_letters_on_right_side = self.util.chosen_letter_index - (word_length - 1 - letter_index)
        # self.log("letters on side {}".format(num_letters_on_left_side))

        # words that end in the prefix
        chosen_letter_expression = self.generate_not_letter_expression(letter)
        program = re.compile(
            "((?:[a-z]{{0,{}}}{}|^))({})((?:$|{}[a-z]{{0,{}}}))".format(num_letters_on_left_side,
                                                                  prefix_expression,
                                                                  chosen_letter_expression,
                                                                  suffix_expression,
                                                                  num_letters_on_right_side))

        found_words = {}
        for word in wordbank.unique_words:
            match_obj = program.match(word)
            if match_obj:
                # self.log("Found matching word {}".format(word))
                self.log(match_obj.groups())
                found_words[word] = match_obj

        return found_words

    def generate_prefix_expression(self, prefix):
        """
        example generate_prefix_expression('ab') yields ab|^b
        :param prefix: 
        :return: 
        """
        list_prefixes = [prefix]

        for index in range(1, len(prefix)):
            expr = "{}{}".format('|^', prefix[index:])
            list_prefixes.append(expr)

        return ''.join(list_prefixes)

    def generate_suffix_expression(self, suffix):
        """
        example generate_suffix_expression("de" yields d$|de
        :param suffix: 
        :return: 
        """
        list_suffixes = []

        for index in range(1, len(suffix)):
            expr = "{}{}".format(suffix[:index], '$')
            list_suffixes.append(expr)

        list_suffixes.append(suffix)

        return '|'.join(list_suffixes)

    def generate_not_letter_expression(self, letter):
        """
        Generate a regex expression for a single letter that doesn't contain 'letter'
        example letter = e yeilds [a-df-z]
        assumes letter will be in the range of [a-z]
        :param letter: 
        :return: 
        """

        banned_list = self.banned_hash[letter]
        acceptable_letters = [n for n in self.letter_list if n not in banned_list]
        expression = ''.join(acceptable_letters)
        return "[{}]".format(expression)























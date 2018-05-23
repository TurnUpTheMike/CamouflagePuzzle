from solution.answerkey import AnswerKeyGenerator, AnswerKey
from solution.puzzleutility import PuzzleUtility
import re


class AnswerKeyGeneratorPants(AnswerKeyGenerator):
    def generate_answer_key(self, wordbank):
        print("AnswerkeyGeneratorPants")
        answerkey = AnswerKey()

        word_a = wordbank.hash_by_letter['a'].pop()
        self.choose_word('a', word_a, wordbank)
        print("")
        print("")
        print("")

        for letter in "abcdefghijklmnopqrstuvwxyz":
            letter_set = wordbank.hash_by_letter[letter]
            word = letter_set.pop()
            answerkey.answers[letter] = word
            wordbank.remove_word(word)

        return answerkey

    def choose_word(self, letter, word, wordbank):
        word_matches = self.get_words_that_almost_match(letter, word, wordbank)

        if len(word_matches) == 0:
            return word

        # choose a word
        detterent = word_matches.values()[0]

        letter_index = self.util.letter_ndx_of_word(word, letter)
        word_prefix = word[:letter_index]
        word_suffix = word[letter_index + 1:]
        prefix_group = deterrent.groups()[0]
        suffix_group = detterent.groups()[2]

        prefix_to_use = word_prefix
        if prefix_group.find(word_prefix) > -1:
            prefix_to_use = prefix_group

        suffix_to_use = word_suffix
        if suffix_group.find(word_suffix) > -1:
            suffix_to_use = suffix_group

        mashed_word = "{}{}{}".format(prefix_to_use, letter, suffix_to_use)

        # mashup the word and the deterrent word
        return mashed_word

    def get_words_that_almost_match(self, letter, word, wordbank):
        letter_index = self.util.letter_ndx_of_word(word, letter)
        word_prefix = word[:letter_index]
        word_suffix = word[letter_index + 1:]

        wordbank.print_letterbank(letter)

        print("Choose {} for the letter {} ".format(word, letter))
        print(word_prefix)
        print(word_suffix)

        prefix_expression = self.generate_prefix_expression(word_prefix)
        print(prefix_expression)
        suffix_expression = self.generate_suffix_expression(word_suffix)
        print(suffix_expression)

        word_length = len(word)
        num_letters_on_left_side = self.util.chosen_letter_index - letter_index
        num_letters_on_right_side = self.util.chosen_letter_index - (word_length - 1 - letter_index)
        print("letters on side {}".format(num_letters_on_left_side))

        # words that end in the prefix
        print("all the words that match")
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
                print("Found matching word {}".format(word))
                print(match_obj.groups())
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
        prefix_expression = ""
        if letter != 'a':
            letter_before = chr(ord(letter) - 1)
            prefix_expression = "a-{}".format(letter_before)

        suffix_expression = ""
        if letter != 'z':
            letter_after = chr(ord(letter) + 1)
            suffix_expression = "{}-z".format(letter_after)

        return "[{}{}]".format(prefix_expression, suffix_expression)






















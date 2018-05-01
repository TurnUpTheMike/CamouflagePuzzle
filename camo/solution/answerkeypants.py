from solution.answerkey import AnswerKeyGenerator, AnswerKey
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
        letter_index = word.find(letter)
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

        num_letters_on_left_side = self.properties.puzzle_row_length // 2
        num_letters_on_right_side = self.properties.puzzle_row_length // 2
        print("letters on side {}".format(num_letters_on_left_side))

        # words that end in the prefix
        print("all the words that match")
        # program = re.compile(".*pl.")
        # program = re.compile(
        # "(?:[a-z]{{0,{}}}ab|^ab|^b|^)[a-z](?:$|d$|de$|de[a-z]{{0,{}}})".format(
        # num_letters_on_left_side, num_letters_on_right_side))

        program = re.compile(
            "(?:[a-z]{{0,{}}}{}|^)[a-z](?:$|{}[a-z]{{0,{}}})".format(num_letters_on_left_side,
                                                                     prefix_expression,
                                                                     suffix_expression,
                                                                     num_letters_on_right_side))

        found_words = []
        for word in wordbank.unique_words:
            if program.match(word):
                # print("Found matching word {}".format(word))
                found_words.append(word)

        found_words.sort()
        print(found_words)

        # for start_letter in word:
        # prefix_length = 6 - letter_index - 1
        # suffix_length = 6
        # program = re.compile("[a-z]{{0,{}}}{}.{}.*".format(prefix_length, word_prefix, word_suffix))
        # for word in wordbank.unique_words:
        #     if program.match(word):
        #         print("Found matching word {}".format(word))

    # example generate_prefix_expression('ab') yields ab|^b
    def generate_prefix_expression(self, prefix):
        list_prefixes = [prefix]

        for index in range(1, len(prefix)):
            expr = "{}{}".format('|^', prefix[index:])
            list_prefixes.append(expr)

        return ''.join(list_prefixes)

    def generate_suffix_expression(self, suffix):
        list_suffixes = [suffix]

        for index in range(1, len(suffix)):
            expr = "{}{}{}".format('|', suffix[:index], '$')
            list_suffixes.append(expr)

        return ''.join(list_suffixes)























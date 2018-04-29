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

        num_letters_on_side = self.properties.puzzle_row_length // 2
        print("letters on side {}".format(num_letters_on_side))

        # words that end in the prefix
        print("words that end in the prefix")
        program = re.compile("[a-z]{{0,{}}}{}$".format(num_letters_on_side, word_prefix, word_suffix))

        for word in wordbank.unique_words:
            if program.match(word):
                print("Found matching word {}".format(word))

        # for start_letter in word:
        # prefix_length = 6 - letter_index - 1
        # suffix_length = 6
        # program = re.compile("[a-z]{{0,{}}}{}.{}.*".format(prefix_length, word_prefix, word_suffix))
        # for word in wordbank.unique_words:
        #     if program.match(word):
        #         print("Found matching word {}".format(word))
























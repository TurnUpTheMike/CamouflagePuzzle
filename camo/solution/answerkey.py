

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



class AnswerKey:
    def __init__(self):
        self.answers = {}

    def print_answerkey(self):
        print("------------{}-----------".format(self.__class__.__name__))
        for letter in "abcdefghijklmnopqrstuvwxyz":
            print("{}: {}".format(letter, self.answers[letter]))
        print("--------------------------------------")


class AnswerKeyGenerator:
    def __init__(self, properties):
        self.properties = properties

    def generate_answer_key(self, wordbank):
        answerkey = AnswerKey()

        for letter in "abcdefghijklmnopqrstuvwxyz":
            letter_set = wordbank.hash_by_letter[letter]
            word = letter_set.pop()
            answerkey.answers[letter] = word
            wordbank.remove_word(word)

        return answerkey

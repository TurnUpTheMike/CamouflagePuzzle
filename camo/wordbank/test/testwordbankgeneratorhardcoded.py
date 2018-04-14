import unittest
from wordbank.wordbankgenerator import WordBankGeneratorHardCoded, WordBank


class Properties:
    def __init__(self):
        self.puzzle_row_length = 13


class TestWordBankGeneratorHardcoded(unittest.TestCase):

    def setUp(self):
        self.properties = Properties()

    def test_generate_word_bank(self):
        generator = WordBankGeneratorHardCoded(self.properties)
        word_bank = generator.generate_word_bank()
        self.assertIsInstance(word_bank, WordBank)

    def test_generate_words_from_freebsd(self):
        print("started test words")
        import requests
        words = requests.get(
            "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain").content.splitlines()
        x = 0
        for w in words:
            print("{}".format(w.decode('utf-8')))
            x += 1

        with open("freebsd_words.txt", 'w') as file:
            for w in words:
                file.write("{}\n".format(w.decode('utf-8')))
        print("number of words: {}".format(x))
        self.assertEqual(1, 1)

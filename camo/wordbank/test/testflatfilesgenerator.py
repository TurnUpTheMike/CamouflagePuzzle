import unittest
from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles
from parameterized import parameterized


class TestFlatFilesGenerator(unittest.TestCase):

    @parameterized.expand([
        ('Couch', 'couch'),
        ("Don't", "dont"),
        ('bang!', 'bang')
    ])
    def test_format_word(self, input_word, expected_word):
        generator = WordBankGeneratorFlatFiles(app_properties=None)
        formatted_word = generator.format_word(input_word)
        self.assertEqual(expected_word, formatted_word)

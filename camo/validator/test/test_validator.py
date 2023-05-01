import unittest
import os
from validator.validator import PuzzleValidator
from wordbank.flatfilesgenerator import WordBankGeneratorFlatFiles
from solution.puzzle import Puzzle
from solution.puzzleutility import PuzzleUtility
from solution.answerkey import AnswerKey


class Properties:
    def __init__(self):
        self.min_word_length = 5
        self.max_word_length = 10
        self.puzzle_row_length = 13

        cwd = os.path.dirname(os.path.abspath(__file__))
        self.dir_of_answer_keys = cwd + "/../../out/answer_keys"
        self.dir_of_word_bank_src = cwd + "/../../lib/word_bank_src"
        self.dir_negative_bank = "/../../out/negativebank"
        self.answer_key_generator = "pants"


# This is more of an integration test because I'm using the real word bank
class TestPuzzleValidator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.properties = Properties()
        cls.wordbank = cls.create_test_wordbank()

    def setUp(self):
        self.util = PuzzleUtility(self.properties)
        self.validator = PuzzleValidator(properties=self.properties, wordbank=self.wordbank, utility=self.util)

    @classmethod
    def create_test_wordbank(cls):
        wordbank_generator = WordBankGeneratorFlatFiles(cls.properties)
        wordbank_generator.verbose = False
        wordbank = wordbank_generator.generate_word_bank()
        return wordbank

    def test_possible_solutions_for_row_and_letter(self):
        # answer: assault, deterrent: human
        puzzle_row = "CDHUMASSAULTO"
        s_solutions = self.validator.possible_solutions_for_row_and_letter(puzzle_row=puzzle_row, letter='s')
        self.assertEqual(["assault"], s_solutions)  # assault is the only matching s word

        n_solutions = self.validator.possible_solutions_for_row_and_letter(puzzle_row=puzzle_row, letter='n')
        self.assertEqual(["human"], n_solutions)  # human is the only matching n word

    def test_possible_solutions_for_row(self):
        # answer: assault, deterrent: human
        puzzle_row = "CDHUMASSAULTO"
        solutions = self.validator.possible_solutions_for_row(puzzle_row=puzzle_row)
        self.assertEqual({'s': ['assault'], 'n': ['human']}, solutions)

    def test_possible_solutions_for_row_where_whole_word_appears_not_using_the_selector_index(self):
        # assault is the answer, human appears in the row also
        puzzle_row = "HUMANASSAULT"
        solutions = self.validator.possible_solutions_for_row(puzzle_row=puzzle_row)
        self.assertEqual({'s': ['assault']}, solutions)

    def test_solutions_for_all_rows(self):
        puzzle_rows = [
            "KNNCRIMINALLY",
            "MVVIOLENTEGRA",
            "OFFERINGGRESS",
            "JFNORTHWESTPB",
            "EZIZPOVERTYTQ",
            "ASECONTEXTYNC",
            "PLAYOFLOATTMG",
            "NOTHINGABBITX",
            "MIRACLPENCILY",
            "EXPLOIQUESTDP",
            "PBSERVDIRECTP",
            "SUBSIDYIRRORJ",
            "IHLEGACYMBOLI",
            "SPECIABASISDK",
            "DGERMAJORLHYW",
            "VTBELOWEAVILY",
            "TOBVIOUSTATEM",
            "IIFORMATIONRH",
            "HXCCBARMERELY",
            "DAGGRESSIONNE",
            "CJSPEAKARRIAG",
            "DMUTTEXTURENK",
            "BGHELPFULTURA",
            "HQSUFFICIENTI",
            "BNKOPROPERQER",
            "ORGANIZESIDEL"
        ]

        solutions = self.validator.solutions_for_all_rows(puzzle_rows)

        self.assert_solution_dict({'f': ['final'], 'm': ['criminal']}, solutions[puzzle_rows[0]])
        self.assert_solution_dict({'e': ['violent']}, solutions[puzzle_rows[1]])
        self.assert_solution_dict({'n': ['offering']}, solutions[puzzle_rows[2]])
        self.assert_solution_dict({'h': ['north', 'northwest']}, solutions[puzzle_rows[3]])
        self.assert_solution_dict({'v': ['poverty'], 'w': ['power']}, solutions[puzzle_rows[4]])
        self.assert_solution_dict({'t': ['context'], 'd': ['second']}, solutions[puzzle_rows[5]])
        self.assert_solution_dict({'l': ['float']}, solutions[puzzle_rows[6]])
        self.assert_solution_dict({'r': ['rabbit'], 'k': ['think'], 'g': ['nothing', 'thing']}, solutions[puzzle_rows[7]])
        self.assert_solution_dict({'p': ['pencil'], 'e': ['miracle']}, solutions[puzzle_rows[8]])
        self.assert_solution_dict({'t': ['exploit'], 'q': ['quest'], 'g': ['guest']}, solutions[puzzle_rows[9]])
        self.assert_solution_dict({'d': ['direct']}, solutions[puzzle_rows[10]])
        self.assert_solution_dict({'m': ['mirror'], 'y': ['subsidy']}, solutions[puzzle_rows[11]])
        self.assert_solution_dict({'s': ['symbol'], 'c': ['legacy']}, solutions[puzzle_rows[12]])
        self.assert_solution_dict({'b': ['basis'], 'l': ['special']}, solutions[puzzle_rows[13]])
        self.assert_solution_dict({'y': ['mayor'], 'j': ['major']}, solutions[puzzle_rows[14]])
        self.assert_solution_dict({'w': ['below']}, solutions[puzzle_rows[15]])
        self.assert_solution_dict({'u': ['obvious'], 'e': ['estate']}, solutions[puzzle_rows[16]])
        self.assert_solution_dict({'a': ['format', 'formation'], 'o': ['motion']}, solutions[puzzle_rows[17]])
        self.assert_solution_dict({}, solutions[puzzle_rows[18]])
        self.assert_solution_dict({'s': ['aggression']}, solutions[puzzle_rows[19]])
        self.assert_solution_dict({'k': ['speak']}, solutions[puzzle_rows[20]])
        self.assert_solution_dict({'x': ['texture'], 'r': ['mutter']}, solutions[puzzle_rows[21]])
        self.assert_solution_dict({'f': ['helpful']}, solutions[puzzle_rows[22]])
        self.assert_solution_dict({'i': ['sufficient']}, solutions[puzzle_rows[23]])
        self.assert_solution_dict({'o': ['proper']}, solutions[puzzle_rows[24]])
        self.assert_solution_dict({'b': ['beside'], 'z': ['organize'], 'c': ['organic']}, solutions[puzzle_rows[25]])

    def assert_solution_dict(self, expected, actual):
        """
        :param expected: formatted like {'h': ['north', 'northwest']}
        :param actual: formatted like {'h': ['north', 'northwest']}
        :return:
        """
        self.assertEqual(len(expected), len(actual))
        for key in expected:
            self.assertIn(key, actual)
            expected_list = expected[key]
            actual_list = actual[key]
            self.assertEqual(expected_list.sort(), actual_list.sort())

    def test_create_letter_counts(self):
        solutions = {
            'MVVIOLENTEGRA': {'e': ['violent']},
            'KNNCRIMINALLY': {'f': ['final'], 'm': ['criminal']},
            'OFFERINGGRESS': {'n': ['offering']},
            'JFNORTHWESTPB': {'h': ['north', 'northwest']},
            'EZIZPOVERTYTQ': {'v': ['poverty'], 'w': ['power']},
            'ASECONTEXTYNC': {'t': ['context'], 'd': ['second']},
            'PLAYOFLOATTMG': {'l': ['float']},
            'NOTHINGABBITX': {'r': ['rabbit'], 'k': ['think'], 'g': ['nothing', 'thing']},
            'MIRACLPENCILY': {'p': ['pencil'], 'e': ['miracle']},
            'EXPLOIQUESTDP': {'t': ['exploit'], 'q': ['quest'], 'g': ['guest']}
        }

        letter_count = self.validator.create_letter_counts(solutions)

        # as a hash, this looks like
        # [('f', 1, 'KNNCRIMINALLY'), ('d', 1, 'ASECONTEXTYNC'), ('m', 1, 'KNNCRIMINALLY'), ('p', 1, 'MIRACLPENCILY'),
        # ('r', 1, 'NOTHINGABBITX'), ('q', 1, 'EXPLOIQUESTDP'), ('h', 1, 'JFNORTHWESTPB'), ('k', 1, 'NOTHINGABBITX'),
        # ('l', 1, 'PLAYOFLOATTMG'), ('w', 1, 'EZIZPOVERTYTQ'), ('v', 1, 'EZIZPOVERTYTQ'), ('n', 1, 'OFFERINGGRESS'),
        # ('t', 2, 'EXPLOIQUESTDP'), ('e', 2, 'MVVIOLENTEGRA'), ('g', 2, 'EXPLOIQUESTDP')]

        # Assert that the value of the last item is greater frequency than the first item
        self.assertGreater(letter_count[len(letter_count) - 1][1], letter_count[0][1])

    def test_create_solution_from_letter_counts(self):
        solutions = {
            'ABCDEF_ABCDEF': {'a': ['aword']},
            'BCDEFG_BCDEFG': {'b': ['bword'], 'a': ['aworda']},
            'CDEFGH_CDEFGH': {'b': ['bwordb'], 'c': ['cword']},
        }

        letter_counts = self.validator.create_letter_counts(solutions)

        # self.validator.verbose = True
        row_solutions = self.validator.create_solution_from_letter_counts(letter_counts, solutions)

        # verify that each row has a solution
        for row_key in solutions:
            self.assertIn(row_key, row_solutions)

        self.assertEqual(row_solutions['ABCDEF_ABCDEF'], ('a', 'aword'))
        self.assertEqual(row_solutions['BCDEFG_BCDEFG'], ('b', 'bword'))
        self.assertEqual(row_solutions['CDEFGH_CDEFGH'], ('c', 'cword'))

    def test_create_solution_from_letter_counts_multiple_solutions(self):
        solutions = {
            'ABCDEF_ABCDEF': {'a': ['aword'], 'c': ['cwordc']},
            'BCDEFG_BCDEFG': {'b': ['bword'], 'a': ['aworda']},
            'CDEFGH_CDEFGH': {'b': ['bwordb'], 'c': ['cword']},
        }

        letter_counts_all_greater_than_1 = self.validator.create_letter_counts(solutions)

        # self.validator.verbose = True
        row_solutions = self.validator.create_solution_from_letter_counts(letter_counts_all_greater_than_1, solutions)

        self.assertEqual(len(row_solutions), 0)
        self.assertGreater(len(self.validator.error_messages), 0)  # go inspect the error messages
        self.assertIn('Multiple solutions exist', self.validator.error_messages)

    def test_create_solution_from_letter_counts_multiple_solutions_1(self):
        solutions = {
            'ABCDEF_ABCDEF': {'a': ['aword']},
            'BCDEFG_BCDEFG': {'b': ['bword'], 'c': ['cwordc']},
            'CDEFGH_CDEFGH': {'b': ['bwordb'], 'c': ['cword']},
        }

        letter_counts = self.validator.create_letter_counts(solutions)

        # self.validator.verbose = True
        row_solutions = self.validator.create_solution_from_letter_counts(letter_counts, solutions)

        self.assertEqual(row_solutions['ABCDEF_ABCDEF'], ('a', 'aword'))
        self.assertGreater(len(self.validator.error_messages), 0)  # go inspect the error messages
        self.assertIn('Multiple solutions exist', self.validator.error_messages)

    def test_create_solution_from_letter_counts_one_letter_for_two_rows(self):
        solutions = {
            'ABCDEF_ABCDEF': {'a': ['aword']},
            'BCDEFG_BCDEFG': {'b': ['bword']},
            'CDEFGH_CDEFGH': {'b': ['bwordb']},
        }

        letter_counts = self.validator.create_letter_counts(solutions)

        # self.validator.verbose = True
        row_solutions = self.validator.create_solution_from_letter_counts(letter_counts, solutions)

        self.assertEqual(row_solutions['ABCDEF_ABCDEF'], ('a', 'aword'))
        self.assertGreater(len(self.validator.error_messages), 0)  # go inspect the error messages
        self.assertIn('Multiple solutions exist', self.validator.error_messages)

    def test_create_solution_from_letter_counts_two_letter_for_one_rows(self):
        solutions = {
            'ABCDEF_ABCDEF': {'a': ['aword'], 'c': ['cwordc']},
            'BCDEFG_BCDEFG': {'b': ['bword']},
            'CDEFGH_CDEFGH': {'d': ['dword']},
        }

        letter_counts = self.validator.create_letter_counts(solutions)

        # self.validator.verbose = True
        self.validator.create_solution_from_letter_counts(letter_counts, solutions)

        self.assertGreater(len(self.validator.error_messages), 0)
        # The error message is either 'Row ABCDEF_ABCDEF already has a letter. No place to put letter c'
        # or 'Row ABCDEF_ABCDEF already has a letter. No place to put letter a'
        # depending on whether a or c is placed first
        self.assertIn("Two letters only fit on one row", self.validator.error_messages)

    def xtest_specific_puzzle(self):
        """
        This is used for testing the validity of a puzzle end-to-end
        :return:
        """
        puzzle = Puzzle()
        puzzle.puzzle_rows = [
            "DYNAMICANDSOM",
            "XNJDECORATEFU",
            "SVCRIMAFRAIDG",
            "DELIGHTGREEME",
            "FVPRICQUESTXZ",
            "KYKNOWBEAUTYO",
            "ADRIDGSMALLQC",
            "TREALIZEASONM",
            "MMETHODHIGHBP",
            "TSOMEONELIVER",
            "SYNDROMETTERV",
            "DVBRINGREAKBY",
            "MAINSTREAMMAT",
            "ZCGLOBLADENGR",
            "MREMARKABLESP",
            "ZZFENSURECIOU",
            "GBUBBLVOICEGS",
            "CVTNSTEALCULA",
            "OFORMEXICANYS",
            "BOMXESPILLING",
            "READILYUNIORI",
            "YFOLLOWUBSIDY",
            "XMANAGINGRYDF",
            "YBREAKFASTERH",
            "HABITAJURORUR",
            "INTENSHAREDZN"
        ]

        answerkey = AnswerKey()
        answerkey.answers = {
            "a": "afraid",
            "b": "beauty",
            "c": "dynamic",
            "d": "method",
            "e": "steal",
            "f": "breakfast",
            "g": "bring",
            "h": "shared",
            "i": "managing",
            "j": "juror",
            "k": "remarkable",
            "l": "blade",
            "m": "syndrome",
            "n": "someone",
            "o": "decorate",
            "p": "spill",
            "q": "quest",
            "r": "mainstream",
            "s": "small",
            "t": "delight",
            "u": "ensure",
            "v": "voice",
            "w": "follow",
            "x": "mexican",
            "y": "readily",
            "z": "realize"
        }

        self.validator.verbose = True
        is_valid = self.validator.is_valid_puzzle(puzzle, answerkey)

        if not is_valid:
            print(self.validator.validator_error_details())

        self.assertTrue(is_valid)

















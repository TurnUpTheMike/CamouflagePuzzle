from unittest import TestCase
from wordbank.answerkey import sortWords, Solver

class TestSorting(TestCase):

    def testSorting(self):
        hashes = {
            'a' : [1, 2, 3],
            'b' : [2, 3],
            'c' : [1]
        }

        result = sortWords(hashes)
        self.assertEqual(['c', 'b', 'a'], list(result), "Wrong sort order")


class TestSolution(TestCase):

    def testSimple(self):
        ordered = ['a', 'b', 'c']
        hashes = {
            'a' : ['alpha'],
            'b' : ['beta'],
            'c' : ['gamma']
        }

        solver = Solver(ordered, hashes)
        solution = solver.solve()

        self.assertEqual(['alpha', 'beta', 'gamma'], solution)

    def testDuplicate(self):
        ordered = ['a', 'b', 'c']
        hashes = {
            'a' : ['alpha'],
            'b' : ['beta'],
            'c' : ['alpha', 'gamma']
        }

        solver = Solver(ordered, hashes)
        solution = solver.solve()

        self.assertEqual(['alpha', 'beta', 'gamma'], solution)

    def testEarlyDuplicate(self):
        ordered = ['a', 'b', 'c']
        hashes = {
            'a' : ['alpha', 'gamma'],
            'b' : ['beta'],
            'c' : ['alpha']
        }

        solver = Solver(ordered, hashes)
        solution = solver.solve()

        self.assertEqual(['gamma', 'beta', 'alpha'], solution)


from unittest import TestCase

from solution.answerkeyalan import sortWords, Solver


class FakeWordBank():

    def __init__(self, hashes):
        self.hashes_by_letter = hashes


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

        solver = Solver(FakeWordBank(hashes), ordered)
        solution = solver.solve()

        self.assertEqual(['alpha', 'beta', 'gamma'], solution)


    def testNoOrdered(self):
        hashes = {
            'a' : ['alpha'],
            'b' : ['alpha', 'beta'],
            'c' : ['alpha', 'beta', 'gamma']
        }

        solver = Solver(FakeWordBank(hashes))
        solution = solver.solve()

        self.assertEqual(['alpha', 'beta', 'gamma'], solution)

    def testDuplicate(self):
        ordered = ['a', 'b', 'c']
        hashes = {
            'a' : ['alpha'],
            'b' : ['beta'],
            'c' : ['alpha', 'gamma']
        }

        solver = Solver(FakeWordBank(hashes), ordered)
        solution = solver.solve()

        self.assertEqual(['alpha', 'beta', 'gamma'], solution)

    def testEarlyDuplicate(self):
        ordered = ['a', 'b', 'c']
        hashes = {
            'a' : ['alpha', 'gamma'],
            'b' : ['beta'],
            'c' : ['alpha']
        }

        solver = Solver(FakeWordBank(hashes), ordered)
        solution = solver.solve()

        self.assertEqual(['gamma', 'beta', 'alpha'], solution)


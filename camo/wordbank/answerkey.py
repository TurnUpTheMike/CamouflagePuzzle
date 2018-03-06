from collections import defaultdict, OrderedDict

def sortWords(hashes):
    lenmap = defaultdict(list)
    ordered = []
    for alpha, words in hashes.items():
        lenmap[len(words)] += alpha

    for ln in sorted(lenmap.keys()):
        for alpha in lenmap[ln]:
            ordered.append(alpha)

    return ordered
        


class Solver():

    def __init__(self, bank, ordered=None):
        self.hashes = bank.hashes_by_letter
        if ordered is None:
            ordered = sortWords(self.hashes)
        self.ordered = ordered
        self.tried = defaultdict(set)


    def solveLetter(self, letter, solution):
        for word in self.hashes[letter]:
            # feels like a yield in here
            if word not in solution and word not in self.tried[letter]:
                self.tried[letter].add(word)
                solution.append(word)
                return True
        return False

    def solve(self):
        solution = []
        
        i = 0
        while (i >= 0) and (i < len(self.ordered)):
            letter = self.ordered[i]
            if self.solveLetter(letter, solution):
                i += 1
            else:
                self.tried[letter].clear()
                solution.pop()
                i -= 1
        
        return solution if len(solution) == len(self.ordered) else None


def create_solution(bank):
    # populate the solver with the appropriate hashes.
    solver = Solver(bank)

    # now from bottom of list, go up and try to find words
    solution = solver.solve()

    # return the list
    return solution

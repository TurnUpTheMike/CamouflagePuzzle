

class PuzzlePackager:
    def __init__(self, properties):
        self.properties = properties

    def write_puzzle(self, puzzle):
        print("Creating puzzle")


class PuzzleToPDF(PuzzlePackager):
    def write_puzzle(self, puzzle):
        print("Creating PDF")

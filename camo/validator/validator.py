
class PuzzleValidator:
    def __init__(self, properties, wordbank, utility):
        self.properties = properties
        self.wordbank = wordbank
        self.util = utility
        self.error_messages = []
        self.verbose = False
        self.row_solutions = None
        self.override_validation = False
        if self.properties.answer_key_generator == 'theme':
            self.override_validation = True

    def is_valid_puzzle(self, puzzle, answerkey):
        if self.override_validation:
            return True

        solutions_by_row = self.solutions_for_all_rows(puzzle.puzzle_rows)
        if not self.does_each_row_have_at_least_one_solution(solutions_by_row):
            return False

        letter_counts = self.create_letter_counts(solutions_by_row)
        self.row_solutions = self.create_solution_from_letter_counts(letter_counts, solutions_by_row)

        # more checking on the validated row solutions
        self.do_solutions_match_answerkey(self.row_solutions, answerkey)

        return len(self.error_messages) == 0

    def do_solutions_match_answerkey(self, row_solutions, answerkey):
        found_letters = set()

        for row_key in row_solutions:
            row_solution = row_solutions[row_key]
            letter = row_solution[0]
            if letter not in answerkey.answers:
                self.error_messages.append("letter {} not found in answerkey".format(letter))
                continue

            word = row_solution[1]
            answer_word = answerkey.answers[letter]
            if answer_word.find(word) < 0:  # the word may be a substring of answer
                self.error_messages.append(
                    "Invalid AnswerKey: For letter {} answerkey word = {} found word = {}".format(
                        letter, answer_word, word
                    )
                )
                continue

            # This is the correct row solution
            found_letters.add(letter)

        if len(found_letters) != len(answerkey.answers):
            self.error_messages.append("The number of validated answers {} do not match the answerkey {}".format(
                len(found_letters), len(answerkey.answers)
            ))

        return

    def create_solution_from_letter_counts(self, original_letter_counts, original_solutions_by_row):
        validated_row_solutions = {}  # puzzle_row => (letter, answer_word)
        max_attempts = len(original_solutions_by_row)

        letter_counts = original_letter_counts
        remaining_solutions = original_solutions_by_row

        self.vprint("The original letter counts are")
        self.pretty_letter_counts(original_letter_counts)

        for solving_attempt in range(max_attempts):
            for letter_frequency in letter_counts:
                potential_num_answers_for_letter = letter_frequency[1]
                if potential_num_answers_for_letter == 1:
                    self.vprint("remaining_solutions")
                    self.pretty_solutions(remaining_solutions)

                    # choose this letter because it only works for one row
                    letter_to_place = letter_frequency[0]
                    self.vprint("placing letter {}".format(letter_to_place))

                    # add the row => letter, word to the working solution
                    row_for_letter = letter_frequency[2]
                    if row_for_letter not in remaining_solutions:
                        self.error_messages.append("Two letters only fit on one row")
                        self.error_messages.append(
                            "Row {} already has a letter. No place to put letter {}".format(
                                row_for_letter, letter_to_place
                            )
                        )
                        return validated_row_solutions

                    word_for_row = remaining_solutions[row_for_letter][letter_to_place][0]
                    validated_row_solutions[row_for_letter] = (letter_to_place, word_for_row)
                    self.vprint("placed letter {} as word {} for row {}".format(
                        letter_to_place, word_for_row, row_for_letter
                    ))

                    # remove the row from the list of solutions
                    del remaining_solutions[row_for_letter]

                    # remove the letter from any other solutions
                    for row_key in remaining_solutions:
                        row_solution = remaining_solutions[row_key]
                        if letter_to_place in row_solution:
                            self.vprint("removing letter {} from {} of row {}".format(
                                letter_to_place, row_key, remaining_solutions[row_key]))
                            del remaining_solutions[row_key][letter_to_place]
                else:
                    self.vprint("time to reevaluate the letter counts")
                    break
            self.vprint("preparing next solving attempt {} of {}".format(solving_attempt, max_attempts))
            if len(remaining_solutions) == 0:
                break  # we've found all of the easy solutions

            letter_counts = self.create_letter_counts(remaining_solutions)
            self.vprint("new letter counts are:")
            self.pretty_letter_counts(letter_counts)

        if len(remaining_solutions) > 0:
            self.error_messages.append("Multiple solutions exist")
            self.error_messages.append("Remaining solutions:")
            self.error_messages.append("{}".format(remaining_solutions))
            self.error_messages.append("Remaining letter counts")
            self.error_messages.append("{}".format(letter_counts))

        return validated_row_solutions

    def vprint(self, msg):
        if self.verbose:
            print(msg)

    def pretty_letter_counts(self, letter_counts):
        if self.verbose:
            to_list = ["{}".format(k) for k in letter_counts]
            to_string = "\n".join(to_list)
            print(to_string)

    def pretty_solutions(self, solutions):
        if self.verbose:
            to_list = ["{}: {}".format(key, solutions[key]) for key in solutions]
            to_string = "\n".join(to_list)
            print(to_string)

    def does_each_row_have_at_least_one_solution(self, solutions_for_each_row):
        for row_puzzle in solutions_for_each_row:
            row_solutions = solutions_for_each_row[row_puzzle]
            if len(row_solutions) == 0:
                self.error_messages.append("row {} has 0 solutions".format(row_puzzle))
                return False

        return True

    def create_letter_counts(self, solutions):
        letter_count_hash = {}
        first_word_hash = {}

        for row_key in solutions:
            row_solution = solutions[row_key]
            for letter_solution in row_solution:
                if letter_solution in letter_count_hash:
                    letter_count_hash[letter_solution] = letter_count_hash[letter_solution] + 1
                else:
                    letter_count_hash[letter_solution] = 1
                    first_word_hash[letter_solution] = row_key

        # sort the letters by frequency
        letter_count_list = [(k, letter_count_hash[k], first_word_hash[k]) for k in
                             sorted(letter_count_hash, key=letter_count_hash.get, reverse=False)]
        return letter_count_list

    def solutions_for_all_rows(self, puzzle_rows):
        solutions = {}
        for puzzle_row in puzzle_rows:
            solutions_for_row = self.possible_solutions_for_row(puzzle_row=puzzle_row)
            if not solutions_for_row:
                self.error_messages.append("No solutions for puzzle row {}".format(puzzle_row))
            solutions[puzzle_row] = solutions_for_row

        return solutions

    def possible_solutions_for_row(self, puzzle_row):
        solutions_by_letter = {}
        for letter in "abcdefghijklmnopqrstuvwxyz":
            potential_solutions = self.possible_solutions_for_row_and_letter(puzzle_row=puzzle_row, letter=letter)
            if potential_solutions:
                solutions_by_letter[letter] = potential_solutions

        return solutions_by_letter

    def possible_solutions_for_row_and_letter(self, puzzle_row, letter):
        solutions = []
        row = "{}{}{}".format(
            puzzle_row[:self.util.chosen_letter_index],
            letter,
            puzzle_row[self.util.chosen_letter_index + 1:]
        ).lower()

        for word in self.wordbank.hash_by_letter[letter]:
            found = row.find(word)
            letter_ndx = self.util.letter_ndx_of_word(word, letter)
            if found + letter_ndx == self.util.chosen_letter_index:
                solutions.append(word)

        return solutions

    def validator_error_details(self):
        print_messages = [
            "The Puzzle is not valid",
            "-----------------------------"
        ]
        if len(self.error_messages) > 0:
            print_messages += self.error_messages

        return "\n".join(print_messages)

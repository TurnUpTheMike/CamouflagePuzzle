from jinja2 import Environment, FileSystemLoader
import os
import pdfkit


class PuzzlePackager:
    def __init__(self, properties):
        self.properties = properties
        self.html_template_file = self.properties.puzzle_template

    def write_puzzle(self, puzzle):
        puzzle_html = self.puzzle_to_html(puzzle)
        pdfkit.from_string(puzzle_html, "testing_puzzle.pdf")

    def puzzle_to_html(self, puzzle):
        template_filename = os.path.basename(self.html_template_file)
        template_dir = os.path.dirname(os.path.abspath(self.html_template_file))
        chosen_letter_index = self.properties.puzzle_row_length // 2

        environment = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
        puzzle_html = environment.get_template(template_filename).render(
            title="Hello Pants",
            puzzle_rows=puzzle.puzzle_rows,
            puzzle_row_length = self.properties.puzzle_row_length,
            chosen_letter_index=chosen_letter_index
        )

        return puzzle_html


class PuzzleToPDF(PuzzlePackager):
    def write_puzzle(self, puzzle):
        print("Creating PDF")

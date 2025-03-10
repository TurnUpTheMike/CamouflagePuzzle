from jinja2 import Environment, FileSystemLoader
import os
import pdfkit
import datetime
import time


class PuzzlePackager:
    def __init__(self, properties):
        self.properties = properties
        self.html_template_file = self.properties.puzzle_template
        self.output_file_name = self.get_output_filename(
            self.properties.puzzle_output_dir,
            self.properties.puzzle_pdf_name
        )

    def get_output_filename(self, filename_directory, filename_pattern):
        if self.properties.answer_key_generator == 'theme':
            pdf_name = filename_pattern.format(self.properties.theme.replace('.csv', ''))
            return os.path.join(filename_directory, pdf_name)

        if '{}' in filename_pattern:
            timestamp = time.time()
            formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')
            filename_pattern = filename_pattern.format(formatted_timestamp)

        return os.path.join(filename_directory, filename_pattern)

    def write_puzzle(self, puzzle):
        puzzle_html = self.puzzle_to_html(puzzle)
        print("writing puzzle {}".format(self.output_file_name))
        print(f'environment_home? {self.properties.environment_home}')

        if self.properties.environment_home:
            path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            pdfkit.from_string(puzzle_html, self.output_file_name, configuration=config)
        else: 
            pdfkit.from_string(puzzle_html, self.output_file_name)

    def puzzle_to_html(self, puzzle):
        template_filename = os.path.basename(self.html_template_file)
        template_dir = os.path.dirname(os.path.abspath(self.html_template_file))
        chosen_letter_index = self.properties.puzzle_row_length // 2

        environment = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
        puzzle_html = environment.get_template(template_filename).render(
            title="Camouglage Puzzle",
            puzzle_rows=puzzle.puzzle_rows,
            puzzle_row_length=self.properties.puzzle_row_length,
            chosen_letter_index=chosen_letter_index
        )

        return puzzle_html


class SolutionPackager:
    def __init__(self, properties, utility):
        self.properties = properties
        self.util = utility

    def puzzle_to_string(self, puzzle, answerkey):
        output_array = []
        for row in puzzle.puzzle_rows:
            letter = row[self.util.chosen_letter_index]
            word = answerkey.get_answer_for_letter(letter.lower())
            output_array.append(word.upper())
            output_array.append('\n')

        return ''.join(output_array)

    def get_answerkey_filename(self):
        if self.properties.answer_key_generator == 'theme':
            answerkey_name = self.properties.answerkey_txt_name.format(self.properties.theme.replace('.csv', ''))
            return os.path.join(self.properties.dir_of_answer_keys, answerkey_name)

        filename = self.properties.answerkey_txt_name
        if '{}' in filename:
            timestamp = time.time()
            formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d%H%M%S')
            filename = filename.format(formatted_timestamp)

        return os.path.join(self.properties.dir_of_answer_keys, filename)

    def write_solution(self, puzzle, answerkey):
        output_name = self.get_answerkey_filename()

        file = open(output_name, "w")
        file.write(self.puzzle_to_string(puzzle, answerkey))
        file.close()




















































class SinglePuzzleData:

    def __init__(self, description, quote, answer_array, solution_text, puzzle_hint="  ", solved=False):
        self.description = description
        self.quote = quote
        self.answer_array = answer_array
        self.puzzle_hint = puzzle_hint
        self.solution_text = solution_text
        self.solved = solved

    def set_solved(self, is_solved):
        self.solved = is_solved

    def get_description(self):
        return self.description

    def get_quote(self):
        return self.quote

    def get_answer_array(self):
        return self.answer_array

    def get_solution_text(self):
        return self.solution_text

    def get_puzzle_hint(self):
        return self.puzzle_hint

    def get_solution_line(self):
        if self.solved:
            result = "{0}|{1}".format(self.get_solution_text(), self.get_puzzle_hint())
        else:
            result = "|{0}".format(self.get_puzzle_hint())
        return result
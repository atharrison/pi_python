class SinglePuzzleData:

    def __init__(self, description, quote, answer_array, solution_text, solved=False):
        self.description = description
        self.quote = quote
        self.answer_array = answer_array
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
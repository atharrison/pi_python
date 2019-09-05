
class PuzzleTracker:

    def __init__(self):
        self.diagnostics_ran = False
        self.progress = 0 # integer, 0->100
        self.load_state()
        self.puzzle_index = 1
        self.init_answers()
        self.init_quotes()
        self.init_puzzle_descriptions()

    def increment_puzzle_index(self):
        self.puzzle_index += 1
        print("Puzzle Index now at {0}".format(self.puzzle_index))

    def is_diagnostics_ran(self):
        return self.diagnostics_ran

    def set_diagnostics_ran(self, b):
        self.diagnostics_ran = b
        self.save_state()

    def get_next_puzzle_description(self):
        # if self.diagnostics_ran:
        #
        # else:
        #     return
        return self.puzzle_descriptions(self.puzzle_index)

    def get_progress_text(self):
        # self.progress +=1
        return "{0}%".format(self.progress)

    def save_state(self):
        # TODO: Save state to file
        pass

    def load_state(self):
        # TODO: Load state from file
        pass

    def check_answer_against_switch__state(self, switch_state):
        # Return true if state given matches current answer
        result = self.current_answer() == switch_state
        print("Checking equality: {0} =? {1} : {2}".format(self.current_answer(), switch_state, result))
        return result

    def current_answer(self):
        return self.answers[self.puzzle_index]

    def current_quote(self):
        return self.quotes[self.puzzle_index]

    def current_puzzle_description(self):
        return self.puzzle_descriptions[self.puzzle_index]

    def init_answers(self):
        # Could read from a file, or just hard-code them here.
        self.answers = {
            1: [0, 0, 0, 0, 0, 0, 0, 1],
            2: [0, 0, 0, 0, 0, 0, 1, 0],
            3: [0, 0, 0, 0, 0, 0, 1, 1],
            4: [0, 0, 0, 0, 0, 1, 0, 0],
            5: [0, 0, 0, 0, 0, 1, 0, 1],
            6: [0, 0, 0, 0, 0, 1, 1, 0],
            7: [0, 0, 0, 0, 0, 1, 1, 1],
            8: [0, 0, 0, 0, 1, 0, 0, 0],
            9: [0, 0, 0, 0, 1, 0, 0, 1],
            10: [0, 0, 0, 0, 1, 0, 1, 0],
        }

    def init_quotes(self):
        self.quotes = {
            1: "Quote 1",
            2: "Quote 2",
            3: "Quote 3",
            4: "Quote 4",
            5: "Quote 5",
            6: "Quote 6",
            7: "Quote 7",
            8: "Quote 8",
            9: "Quote 9",
            10: "Quote 10",
        }

    def init_puzzle_descriptions(self):
        self.puzzle_descriptions = {
            1: " System Enabled\n Run Diagnostics...",
            2: "Puzzle 2",
            3: "Puzzle 3",
            4: "Puzzle 4",
            5: "Puzzle 5",
            6: "Puzzle 6",
            7: "Puzzle 7",
            8: "Puzzle 8",
            9: "Puzzle 9",
            10: "Puzzle 10",
        }
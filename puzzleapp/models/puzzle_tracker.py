from .single_puzzle_data import SinglePuzzleData

TOTAL_PUZZLES = 10

class PuzzleTracker:

    def __init__(self):
        self.diagnostics_ran = False
        self.progress = 0 # integer, 0->100
        self.puzzle_index = 0
        self.puzzles = []
        self.load_state()

    def increment_puzzle_index(self):
        self.puzzle_index += 1
        print("Puzzle Index now at {0}".format(self.puzzle_index))

    def is_diagnostics_ran(self):
        return self.diagnostics_ran

    def set_diagnostics_ran(self, b):
        self.diagnostics_ran = b
        self.save_state()

    def get_progress_text(self):
        # self.progress +=1
        return "{0}%".format(self.progress)

    def save_state(self):
        # TODO: Save state to file
        pass

    def load_state(self):
        # TODO: Load state from file.
        # Maybe we can just save a single number: the puzzle_index we're currently on.
        self.load_puzzles(self.puzzle_index)

    def check_answer_against_switch_state(self, switch_state):
        # Return true if state given matches current answer
        result = self.current_answer() == switch_state
        print("Checking equality: {0} =? {1} : {2}".format(self.current_answer(), switch_state, result))
        return result

    def current_answer(self):
        return self.puzzles[self.puzzle_index].get_answer_array()

    def current_quote(self):
        return self.puzzles[self.puzzle_index].get_quote()

    def current_puzzle_description(self):
        return self.puzzles[self.puzzle_index].get_description()

    def current_solution_text(self):
        # TODO: Create string of all solved puzzles.
        result = ""
        for idx in range(self.puzzle_index+1):
            result = result + "\n{0}".format(self.puzzles[idx].get_solution_text())
        # return self.puzzles[self.puzzle_index].get_solution_text()
        return result

    def get_progress_percent(self):
        return float(self.puzzle_index) / float(TOTAL_PUZZLES) * 100

    def load_puzzles(self, puzzle_index):
        self.puzzles.append(SinglePuzzleData(" System Enabled\n Run Diagnostics...", "Quote 0", [0, 0, 0, 0, 0, 0, 0, 0], "----------"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 1\nhas second line", "Quote 1", [0, 0, 0, 0, 0, 0, 0, 1], "1"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 2", "Quote 2", [0, 0, 0, 0, 0, 0, 1, 0], "2"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 3", "Quote 3", [0, 0, 0, 0, 0, 0, 1, 1], "3"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 4", "Quote 4", [0, 0, 0, 0, 0, 1, 0, 0], "4"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 5", "Quote 5", [0, 0, 0, 0, 0, 1, 0, 1], "5"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 6", "Quote 6", [0, 0, 0, 0, 0, 1, 1, 0], "6"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 7", "Quote 7", [0, 0, 0, 0, 0, 1, 1, 1], "7"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 8", "Quote 8", [0, 0, 0, 0, 1, 0, 0, 0], "8"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 9", "Quote 9", [0, 0, 0, 0, 1, 0, 0, 1], "9"))
        self.puzzles.append(SinglePuzzleData(" Puzzle 10", "Quote 10", [0, 0, 0, 0, 1, 0, 1, 0], "10"))

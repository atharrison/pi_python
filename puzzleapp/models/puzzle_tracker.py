from .single_puzzle_data import SinglePuzzleData

import os

PUZZLE_STATE_FILE_LINUX="~/tmp/puzzle_app_state.txt"
PUZZLE_STATE_FILE_WINDOWS="C:/tmp/puzzle_app_state.txt"

class PuzzleTracker:

    def __init__(self):
        if os.name == 'nt':
            self.puzzle_state_filename = PUZZLE_STATE_FILE_WINDOWS
        else:
            self.puzzle_state_filename = PUZZLE_STATE_FILE_LINUX

        self.progress = 0 # integer, 0->100
        self.puzzle_index = 0
        self.puzzles = []
        self.load_state()

    def get_total_puzzles(self):
        return len(self.puzzles)

    def increment_puzzle_index(self):
        self.puzzles[self.puzzle_index].set_solved(True)
        self.puzzle_index += 1
        print("Puzzle Index now at {0}".format(self.puzzle_index))
        self.save_state()

    def is_diagnostics_ran(self):
        return self.puzzle_index > 0

    def get_progress_text(self):
        # self.progress +=1
        return "{0}%".format(self.progress)

    def save_state(self):
        # TODO: Save state to file
        state_file = open(self.puzzle_state_filename, "w+")
        state_file.write(str(self.puzzle_index))

    def load_state(self):
        # TODO: Load state from file.
        # Maybe we can just save a single number: the puzzle_index we're currently on.
        index = 0
        try:
            state_file = open(self.puzzle_state_filename, "r+")
            data = state_file.read()
            index = int(data)
            print("Successfully loaded puzzle state to index {0}".format(str(index)))
        except FileNotFoundError as ex:
            print("FileNotFoundError for {0}, using index=0".format(self.puzzle_state_filename))
            index = 0
        except ValueError as ex:
            print("Error reading {0}, using index=0".format(self.puzzle_state_filename))
            index = 0
        except Exception as ex:
            print("Unknown error occurred while loading state: {0}".format(ex))
            index = 0

        self.puzzle_index = index
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
        # Create string of all solved puzzles, and hints for upcoming puzzles.
        result = ""
        if self.puzzle_index < 1:  # Until Diagnostic run, don't show
            return result

        # for idx in range(self.puzzle_index+1):
        for idx in range(len(self.puzzles)):
            result = result + "\n{0}".format(self.puzzles[idx].get_solution_line())
        # return self.puzzles[self.puzzle_index].get_solution_text()
        return result

    def get_progress_percent(self):
        return float(self.puzzle_index) / float(self.get_total_puzzles()) * 100

    def load_puzzles(self, puzzle_index):
        self.puzzles.append(SinglePuzzleData(" System Enabled\n Run Diagnostics...\n\n Switch everything to 1,\n then press the button.",
                                             "",
                                             [1, 1, 1, 1, 1, 1, 1, 1],
                                             "----------------",
                                             "--",
                                             puzzle_index > 0))
        self.puzzles.append(SinglePuzzleData(" Puzzle 1\n Binary Numbers",
                                             "Every journey begins\n  with the first step.\n    ― Lao Tzu",
                                             [0, 0, 0, 0, 0, 0, 0, 1],
                                             "Solved 1",
                                             "  ",
                                             puzzle_index > 1))
        self.puzzles.append(SinglePuzzleData(" To solve this puzzle\n you will need\n Wits and skills\n for you to succeed.\n\n\n\n\nand a line here.",
                                             "Quote 2",
                                             [0, 0, 0, 0, 0, 0, 1, 0],
                                             "Solved 2",
                                             "TX",
                                             puzzle_index > 2))
        self.puzzles.append(SinglePuzzleData(" Puzzle 3",
                                             "Quote 3",
                                             [0, 0, 0, 0, 0, 0, 1, 1],
                                             "Solved 3",
                                             "AZ",
                                             puzzle_index > 3))
        self.puzzles.append(SinglePuzzleData(" Puzzle 4",
                                             "Quote 4",
                                             [0, 0, 0, 0, 0, 1, 0, 0],
                                             "Solved 4",
                                             "CA",
                                             puzzle_index > 4))
        self.puzzles.append(SinglePuzzleData(" Puzzle 5",
                                             "Quote 5",
                                             [0, 0, 0, 0, 0, 1, 0, 1],
                                             "Solved 5",
                                             "NV",
                                             puzzle_index > 5))
        self.puzzles.append(SinglePuzzleData(" Puzzle 6",
                                             "Quote 6",
                                             [0, 0, 0, 0, 0, 1, 1, 0],
                                             "Solved 6",
                                             "NM",
                                             puzzle_index > 6))
        self.puzzles.append(SinglePuzzleData(" Puzzle 7",
                                             "Quote 7",
                                             [0, 0, 0, 0, 0, 1, 1, 1],
                                             "Solved 7",
                                             "??",
                                             puzzle_index > 7))
        self.puzzles.append(SinglePuzzleData(" Puzzle 8",
                                             "Quote 8",
                                             [0, 0, 0, 0, 1, 0, 0, 0],
                                             "Solved 8",
                                             "??",
                                             puzzle_index > 8))
        self.puzzles.append(SinglePuzzleData(" Puzzle 9",
                                             "Quote 9",
                                             [0, 0, 0, 0, 1, 0, 0, 1],
                                             "Solved 9",
                                             "??",
                                             puzzle_index > 9))
        self.puzzles.append(SinglePuzzleData(" Puzzle 10",
                                             "Quote 10",
                                             [0, 0, 0, 0, 1, 0, 1, 0],
                                             "Solved X",
                                             "??",
                                             puzzle_index > 10))

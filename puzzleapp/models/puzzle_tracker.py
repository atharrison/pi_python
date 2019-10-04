from .single_puzzle_data import SinglePuzzleData

import os

PUZZLE_STATE_FILE_LINUX="/puzzleapp/puzzle_app_state.txt"
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

        # If you want to reset, set index here to 0
        if os.name == 'nt':
            # Always reset, for now, on Windows
            self.puzzle_index = 0

        self.load_puzzles(self.puzzle_index)

    def check_answer_against_switch_state(self, switch_state):
        # Return true if state given matches current answer
        result = self.current_answer() == switch_state
        print("Checking equality: {0} =? {1} : {2}".format(self.current_answer(), switch_state, result))
        return result

    def current_answer(self):
        if self.puzzle_index >= len(self.puzzles):
            return []

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
        return float(self.puzzle_index) / float(self.get_total_puzzles()-1) * 100

    def load_puzzles(self, puzzle_index):
        idx = 0
        self.puzzles.append(SinglePuzzleData(" System Enabled\n Diagnostics Part 1 ...\n\n Switch everything to 1,\n then press the button.",
                                             "",
                                             [1, 1, 1, 1, 1, 1, 1, 1],
                                             "   Progress     ",
                                             "  ",
                                             puzzle_index > idx))
        idx+=1
        self.puzzles.append(SinglePuzzleData(" System Enabled\n Diagnostics Part 2 ...\n\n Now, switch everything to 0,\n then press the button.",
                                             "                    ",
                                             [0, 0, 0, 0, 0, 0, 0, 0],
                                             "---------------",
                                             "--",
                                             puzzle_index > idx))
        idx+=1
        self.puzzles.append(SinglePuzzleData(" Diagnostics Complete!\n You have unlocked the PuzzleBox 1000!\n\n Your goal is to solve my puzzles, in a certain order.\n There is a special surprise at the end!\n  To begin, find the puzzle named\n  'Binary Numbers'.",
                                             "Every journey begins\n  with the first step.\n    ― Lao Tzu",
                                             [0, 0, 0, 1, 1, 0, 1, 1],
                                             ".~~~~~~~~~~~~~.",
                                             "  ",
                                             puzzle_index > idx))
        idx+=1
        self.puzzles.append(SinglePuzzleData(" Most puzzles will be solved in groups of 4, \n related in some way.\n The column on the right\n will guide you on your way. \n(Hint: Find the puzzles related to Texas!)",
                                             "Never give up and\n   good luck will find you.\n    - Falcor,\n     The Neverending Story",
                                             [0, 0, 0, 0, 1, 1, 1, 0],
                                             "~ X X X X X X ~",
                                             "TX",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" More info can be found\n in that States and Capitals book.\n If you know where we're travelling,\n you'll know where to look!",
                                             "It does not matter\nhow slowly you go\nas long as you do not stop.\n   - Confucius",
                                             [0, 1, 1, 1, 0, 1, 0, 1],
                                             "~ X O X X X X ~",
                                             "NM",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" Keep it up, you are well on your way!\n Solve some more puzzles\n and don't throw them away!",
                                             "Study nature, love nature,\nstay close to nature.\nIt will never fail you.\n    - Frank Lloyd Wright",
                                             [1, 1, 1, 0, 0, 1, 1, 0],
                                             "~ X X X X O X ~",
                                             "AZ",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" The halfway point,\n once you've solved this group.\n Take a break if you need!\n You don't have to solve \n in one fell swoop!",
                                             "In wisdom gathered over time\nI have found that every\nexperience is a\nform of exploration.\n   - Ansel Adams",
                                             [0, 1, 0, 0, 1, 0, 1, 1],
                                             "~ X X O X X X ~",
                                             "CA",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" Mathematics is fun, and logic is too.\n But travelling, you'll see,\n is just as fun too!",
                                             "The world is a book,\nand those who do not travel\nread only one page.\n  - Saint Augustine",
                                             [1, 1, 0, 0, 1, 0, 0, 1],
                                             "~ X X X X X X ~",
                                             "NV",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" By now you've pieced together\n nearly all you've been handed.\n But more awaits still\n I won't leave you stranded.",
                                             "Traveling - it leaves\nyou speechless,\nthen turns you\ninto a storyteller.\n   - Ibn Battuta",
                                             [1, 0, 0, 1, 1, 0, 1, 0],
                                             "~ X X X X X O ~",
                                             "UT",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" Now see here, you'll find\n some puzzles repeat.\n Look closer, you'll see,\n how some states meet!",
                                             "Our greatest weakness lies in giving up.\nThe most certain way to succeed\nis always to try just one more time.\n   - Thomas Edison",
                                             [1, 1, 1, 0, 0, 0, 0, 1],
                                             "~ O X X X X X ~",
                                             "4C",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" Solve the Maze.\n The CLUE it gives you\n will point you to\n 4 other puzzles.",
                                             "Some people talk to animals.\nNot many listen though.\nThat's the problem.\n   - A.A. Milne",
                                             [0, 1, 1, 0, 0, 1, 1, 0],
                                             "~ X X X X X X ~",
                                             "??",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" So many puzzles.\n You're nearly finished!\n Solving the\n  Puzzle of Puzzles\n will point you\n to the last 4 puzzles.",
                                             "Start by doing what's necessary;\nthen do what's possible;\nand suddenly you are doing the impossible.\n   - Francis of Assisi",
                                             [1, 1, 0, 1, 0, 0, 0, 1],
                                             "*~~~~~~~~~~~~~*",
                                             "??",
                                             puzzle_index > idx))
        idx += 1
        self.puzzles.append(SinglePuzzleData(" You've solved all the puzzles!\n Now there's just two things left.\n (Have you found the other objects?)\n 1. Check your Progress, it holds a key.\n 2. How low is the lowest point\n     in Death Valley?",
                                             "The biggest reward\nfor a thing well done\nis to have done it.\n   – Voltaire",
                                             [],
                                             "",
                                             "  ",
                                             puzzle_index > idx))

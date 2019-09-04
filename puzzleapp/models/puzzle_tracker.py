
class PuzzleTracker:

    def __init__(self):
        self.diagnostics_ran = False
        self.progress = 0 # integer, 0->100
        self.load_state()

    def is_diagnostics_ran(self):
        return self.diagnostics_ran

    def set_diagnostics_ran(self, b):
        self.diagnostics_ran = b
        self.save_state()

    def get_next_puzzle_description(self):
        if self.diagnostics_ran:
            return "Diagnostics\nComplete"
            # TODO: Find and return current puzzle description
        else:
            return " System Enabled\n Run Diagnostics..."

    def get_next_puzzle_quote(self):
        return "And all that jazz"

    def get_progress_text(self):
        self.progress +=1
        return "{0}%".format(self.progress)

    def save_state(self):
        # TODO: Save state to file
        pass

    def load_state(self):
        # TODO: Load state from file
        pass

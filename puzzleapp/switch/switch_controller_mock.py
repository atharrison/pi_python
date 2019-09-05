
class SwitchControllerMock():

    def __init__(self):
        self.switches = [0, 0, 0, 0, 0, 0, 0, 0]
        self.index = 0
        self.puzzle_solutions = [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 0],
        ]

    def switch_data(self):
        # Return the solution for index, each time this is called
        result = self.puzzle_solutions[self.index]
        # self.index = (self.index+1) % len(self.puzzle_solutions)
        return result

    def input_as_string(self):
        return "".join(map(str, self.switch_data()))

    def input_as_array(self):
        return self.switch_data()

    def simulate_button_push(self):
        # Simulate a user entering the next puzzle
        self.index = (self.index+1) % len(self.puzzle_solutions)
        print("Index updated to {0}".format(self.index))
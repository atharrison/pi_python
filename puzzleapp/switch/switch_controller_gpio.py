import random

class SwitchControllerGPIO():

    def __init__(self):
        self.switches = [0, 0, 0, 0, 0, 0, 0, 0]

    def switch_data(self):
        # For now, randomize each time it is called
        for i in range (0, len(self.switches)):
            self.switches[i] = random.randint(0, 1)

        return self.switches

    def input_as_string(self):
        return "".join(map(str, self.switch_data()))

    def input_as_array(self):
        return self.switch_data()

import gui
import switch
import models
import os
from tkinter import Tk


def main():
    root = Tk()

    # Use the Mock if we're debugging on Windows:
    if os.name == 'nt':
        switch_controller = switch.SwitchControllerMock()
    else:
        switch_controller = switch.SwitchControllerGPIO()

    puzzle_tracker = models.PuzzleTracker()
    app = gui.PuzzleGui(root, switch_controller, puzzle_tracker)
    app.start()

main()

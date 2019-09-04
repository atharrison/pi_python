import gui
import switch
import models
from tkinter import Tk


def main():
    root = Tk()
    switch_controller = switch.SwitchController()
    puzzle_tracker = models.PuzzleTracker()
    app = gui.PuzzleGui(root, switch_controller, puzzle_tracker)
    app.start()

main()
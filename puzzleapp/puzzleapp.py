import gui
import switch
from tkinter import Tk


def main():
    root = Tk()
    switch_controller = switch.SwitchController()
    app = gui.PuzzleGui(root, switch_controller)
    app.start()

main()
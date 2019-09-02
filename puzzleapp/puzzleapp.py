import gui
from tkinter import Tk


def main():
    root = Tk()
    app = gui.PuzzleGui(root)
    app.start()

main()
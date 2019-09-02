import sys
import time
from tkinter import *

root = Tk()
label_text = StringVar()


def task():
    print("Task running")
    label_text.set("Changed")


def kill_task():
    print("Killing")

    global root
    # root.quit()
    root.destroy()
    sys.exit()


class PuzzleGui:

    def __init__(self):

        global root
        self.root = root
        self.root.overrideredirect(True)

        self.root_bg = "#405659"
        self.frame_bg = self.root_bg

        self.initialize_app()

        self.start()

    def initialize_app(self):
        # for debug, update frame color
        # frame_bg = "green"
        frame = Frame(root, bg="green")
        # frame = Frame(root, bg=self.frame_bg)
        frame.pack(side=LEFT, fill='both', expand='no')

        w = Label(frame,
                  # font=("courier new", 20, "bold"),
                  justify="left", textvariable=label_text, bg="#405659",
                  fg="#b1e7f0")

        machine_text = " System Enabled\n Run Diagnostics..."
        label_text.set(machine_text)

        # Window uses:
        # "width x height + x_offset + y_offset" (no spaces)

        root_geo = "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())
        # root_geo = "{0}x{1}+0+0".format(1024, 600)
        print(root_geo)
        root.geometry(root_geo)
        root.configure(bg=self.root_bg)
        root.focus_set()  # <-- move focus to this widget

    def register_task(self, delay, task, reccuring=False):
        root.after(delay, task)
        if reccuring:
            # TODO How to re-register
            pass


    def start(self):
        self.register_task(1000, task)
        self.register_task(3000, kill_task)

        self.root.mainloop()

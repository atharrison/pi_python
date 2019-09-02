import time
from tkinter import *
from .tasks import test_task, kill_task

class PuzzleGui:

    def __init__(self, root):
        self.master = root
        self.label_text = StringVar()
        self.root_bg = "#405659"
        self.frame_bg = self.root_bg

        self.initialize_app()

        self.start()

    def initialize_app(self):
        # for debug, update frame color
        # frame_bg = "green"
        # frame = Frame(self.master, bg="green")
        frame = Frame(self.master, bg=self.frame_bg)
        frame.pack(side=LEFT, fill='both', expand='no')

        w = Label(frame,
                  font=("courier new", 20, "bold"),
                  justify="left",
                  textvariable=self.label_text,
                  # text="Testing",
                  bg="#405659",
                  fg="#b1e7f0")

        machine_text = " System Enabled\n Run Diagnostics..."
        self.label_text.set(machine_text)

        self.master.overrideredirect(True)

        # Pressing Escape kills the window
        self.master.bind("<Escape>", lambda e: kill_task(self.master))

        # Window uses:
        # "width x height + x_offset + y_offset" (no spaces)

        #root_geo = "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())
        root_geo = "{0}x{1}+0+0".format(1024, 600)
        print(root_geo)
        self.master.geometry(root_geo)
        self.master.configure(bg=self.root_bg)
        self.master.focus_set()  # <-- move focus to this widget
        w.pack()

    def register_task(self, delay, task, reccuring, *args):
        self.master.after(delay, task, args)
        if reccuring:
            # TODO How to re-register
            pass


    def start(self):
        self.master.after(1000, test_task, self.label_text)
        self.master.after(3000, kill_task, self.master)

        # self.register_task(1000, task, False, self.label_text)
        # self.register_task(3000, kill_task, False)

        self.master.mainloop()

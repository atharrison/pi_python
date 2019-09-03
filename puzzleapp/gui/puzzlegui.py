import time
from tkinter import *
from .tasks import test_task, kill_task, set_switch_input_text


class PuzzleGui:

    def __init__(self, root, switch_controller):
        self.master = root
        self.switch_controller = switch_controller
        self.left_msg_text = StringVar()
        self.right_msg_text = StringVar()
        self.switch_inputs = StringVar()
        self.root_bg = "#405659"
        self.frame_bg = self.root_bg


        self.initialize_app()

        self.start()

    def initialize_app(self):
        # for debug, update frame color
        # frame_bg = "green"
        # frame = Frame(self.master, bg="green")

        switch_frame = Frame(self.master, bg=self.frame_bg)
        switch_frame.pack(side=BOTTOM, fill='x', expand='no')

        left_msg_frame = Frame(self.master, bg=self.frame_bg)
        left_msg_frame.pack(side=LEFT, fill='both', expand='no')

        right_msg_frame = Frame(self.master, bg=self.frame_bg)
        right_msg_frame.pack(side=RIGHT, fill='x', expand='no')

        left_msg_box = Label(left_msg_frame,
                  font=("courier new", 36, "bold italic"),
                  justify="left",
                  textvariable=self.left_msg_text,
                  bg="#405659",
                  fg="#b1e7f0")

        right_msg_box = Label(right_msg_frame,
                  font=("times new roman", 20, "italic"),
                  justify="center",
                  textvariable=self.right_msg_text,
                  bg="#405659",
                  fg="#b1e7f0")

        switch_box = Label(switch_frame,
                  font=("arial", 72, "bold"),
                  justify="center",
                  textvariable=self.switch_inputs,
                  bg="#405659",
                  fg="#b1e7f0")

        machine_text = " System Enabled\n Run Diagnostics..."
        self.left_msg_text.set(machine_text)

        info_text = " Lorem Ipsum\n and all that jazz."
        self.right_msg_text.set(info_text)

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
        left_msg_box.pack()
        right_msg_box.pack()
        switch_box.pack()

    def register_task(self, delay, task, reccuring, *args):
        self.master.after(delay, task, args)
        if reccuring:
            # TODO How to re-register
            pass


    def start(self):
        self.master.after(0, set_switch_input_text, self.master,
                          self.switch_inputs, self.switch_controller)
        self.master.after(1000, test_task, self.left_msg_text)
        self.master.after(6000, kill_task, self.master)

        # self.register_task(1000, task, False, self.left_msg_text)
        # self.register_task(3000, kill_task, False)

        self.master.mainloop()

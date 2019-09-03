import time
from tkinter import *
from .tasks import test_task, kill_task, set_switch_input_text


class PuzzleGui:

    def __init__(self, root, switch_controller):
        self.master = root
        self.switch_controller = switch_controller
        self.progress_text = StringVar()
        self.left_msg_text = StringVar()
        self.right_msg_text = StringVar()
        self.switch_inputs = StringVar()
        self.root_bg = "#405659"
        self.frame_bg = self.root_bg
        self.text_color = "#b1e7f0"

        self.initialize_app()

        self.start()

    def initialize_app(self):
        # for debug, update frame color
        # frame_bg = "green"
        # frame = Frame(self.master, bg="green")
        master_frame = Frame(self.master, bg=self.root_bg)

        progress_frame = master_frame
        switch_frame = master_frame
        left_msg_frame = master_frame
        right_msg_frame = master_frame

        progress_box = Label(master_frame,
                             font=("arial", 12, "bold"),
                             justify="left",
                             textvariable=self.progress_text,
                             bg=self.root_bg,
                             fg=self.text_color)

        left_msg_box = Label(master_frame,
                  font=("courier new", 24, "bold"),
                  justify="left",
                  textvariable=self.left_msg_text,
                  # bg="green",
                  bg=self.root_bg,
                  fg=self.text_color)

        right_msg_box = Label(master_frame,
                  font=("times new roman", 20, "italic"),
                  justify="center",
                  textvariable=self.right_msg_text,
                  # bg="blue",
                  bg=self.root_bg,
                  fg=self.text_color)

        image_box = Label(master_frame,
                          font=("courier new", 120, "bold"),
                          justify="center",
                          text="X",
                          # bg="yellow",
                          bg=self.root_bg,
                          fg=self.text_color)

        switch_box = Label(master_frame,
                  font=("arial", 72, "bold"),
                  justify="center",
                  textvariable=self.switch_inputs,
                  bg=self.root_bg,
                  fg=self.text_color)

        # Grid:
        master_frame.grid(row=0, column=0, sticky="NSEW")
        master_frame.grid_rowconfigure(0, weight=1)
        master_frame.grid_columnconfigure(0, weight=1)
        progress_box.grid(row=0, column=0, columnspan=3, sticky="NW")
        left_msg_box.grid(row=1, column=0, columnspan=1, sticky="NW")
        image_box.grid(row=2, column=1, columnspan=2, sticky="NSEW", padx=200, pady=20)
        right_msg_box.grid(row=3, column=2, columnspan=1, sticky="SE", padx=5)
        switch_box.grid(row=4, column=0, columnspan=3, sticky="S")

        progress = "10%"
        self.progress_text.set(progress)

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

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.master.focus_set()  # <-- move focus to this widget


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

        self.master.mainloop()

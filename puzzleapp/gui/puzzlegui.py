from tkinter import *
from tkinter.ttk import Progressbar, Style
from .tasks import *
from .ip_address import IPAddress

ROOT_BG = "#405659"
TEXT_COLOR = "#b1e7f0"
HIDDEN_TEXT_COLOR = "#516770"
TROUGH_COLOR = ROOT_BG
BAR_COLOR = TEXT_COLOR


class PuzzleGui:

    def __init__(self, root, switch_controller, puzzle_tracker):
        self.master = root
        self.ip_address = IPAddress()
        self.switch_controller = switch_controller
        self.puzzle_tracker = puzzle_tracker
        self.progress_text = StringVar()
        self.left_msg_text = StringVar()
        self.right_msg_text = StringVar()
        self.switch_inputs = StringVar()
        self.solution_text = StringVar()
        self.ip_text = StringVar()
        self.root_bg = ROOT_BG
        self.frame_bg = self.root_bg
        self.text_color = TEXT_COLOR
        self.hidden_text_color = HIDDEN_TEXT_COLOR

        # images must be attached to an object. Local ones will be garbage collected
        # self.image = PhotoImage(file="images/Compass_F.gif")

        self.initialize_app()

        self.register_tasks()
        self.start()

    def initialize_app(self):
        # for debug, update frame color
        # frame_bg = "green"
        # frame = Frame(self.master, bg="green")
        master_frame = Frame(self.master,
                             # bg="red"
                             bg=self.root_bg
                             )

        # Create a canvas to hide the progress bar edges in, so we can make it smaller
        progress_canvas = Canvas(master_frame,
                                width=1024, height=5)

        # Define a style for the progress bar, and name it:
        self.progress_bar_style = Style()
        self.progress_bar_style.theme_use('clam')
        self.progress_bar_style.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR, bordercolor=TROUGH_COLOR,
                        background=BAR_COLOR, lightcolor=BAR_COLOR, darkcolor=BAR_COLOR)

        # Use the name of the style above, for this progress bar
        self.progress_box = Progressbar(progress_canvas,
                                        orient=HORIZONTAL,
                                        length=1030, mode='determinate',
                                        style="bar.Horizontal.TProgressbar")
        # The first 2 create window argvs control where the progress bar is placed
        # I place it outside the window to obsure the frame that I can't remove.
        progress_canvas.create_window(-3, -3, anchor=NW, window=self.progress_box)
        progress_canvas.grid()

        left_msg_box = Label(master_frame,
                  font=("courier new", 14, "bold"),
                  justify="left",
                  textvariable=self.left_msg_text,
                  # bg="green",
                  bg=self.root_bg,
                  fg=self.text_color)

        right_msg_box = Label(master_frame,
                  font=("times new roman", 12, "italic"),
                  justify="center",
                  textvariable=self.right_msg_text,
                  # bg="blue",
                  bg=self.root_bg,
                  fg=self.text_color)

        ip_box = Label(master_frame,
                font=("courier new", 8, ""),
                       justify="right",
                       text=self.ip_address.ip(),
                       # textvariable=self.ip_text,
                       bg=self.root_bg,
                       # bg="green",
                       fg=self.hidden_text_color
                       )

        solution_box = Label(master_frame,
                          font=("courier new", 12, ""),
                          justify="right",
                          # image=self.image,
                         textvariable=self.solution_text,
                          # text="X",
                          # bg="yellow",
                          bg=self.root_bg,
                          fg=self.text_color
                          )

        switch_box = Label(master_frame,
                  font=("arial", 72, "bold"),
                  justify="center",
                  textvariable=self.switch_inputs,
                  bg=self.root_bg,
                  fg=self.text_color)

        exit_button = Button(master_frame,
                             text="EXIT",
                             bg=self.root_bg,
                             fg=self.root_bg, # really hidden
                             highlightthickness=0,
                             bd=0,
                             command=self.exit_method)

        # Grid:
        master_frame.grid(row=0, column=0, sticky="NSEW")
        master_frame.grid_rowconfigure(0, weight=10)
        master_frame.grid_columnconfigure(0, weight=10)

        # self.progress_box.grid(row=0, column=0, columnspan=3, sticky="NW")
        progress_canvas.grid(row=0, column=0, columnspan=3, sticky="NW")
        left_msg_box.grid(row=1, column=0, rowspan=2, columnspan=1, sticky="NW",pady=100)

        exit_button.grid(row=2, column=0, columnspan=1, sticky="SW")

        solution_box.grid(row=2, column=1, columnspan=1, sticky="N", padx=30, pady=0)
        solution_box.grid_rowconfigure(0, weight=1)
        solution_box.grid_columnconfigure(0, weight=1)

        right_msg_box.grid(row=3, column=2, columnspan=1, sticky="SE", padx=5)
        switch_box.grid(row=4, column=0, columnspan=3, sticky="S")
        ip_box.grid(row=4, column=2, columnspan=1, rowspan=1, sticky="SE")

        self.master.overrideredirect(True)

        # Pressing Escape kills the window
        self.master.bind("<Escape>", lambda e: kill_task(self.master))
        #self.master.bind("<Control-c>", lambda e: kill_task(self.master))

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

        # Write the SolutionText using the current puzzle state:
        self.solution_text.set(self.puzzle_tracker.current_solution_text())

    def register_tasks(self):
        self.master.after(1000, set_switch_input_text, self.master,
                          self.switch_inputs, self.switch_controller)
        self.master.after(0, puzzle_desc_task, self.left_msg_text, self.puzzle_tracker, self.master)
        self.master.after(0, quote_task, self.right_msg_text, self.puzzle_tracker, self.master)
        self.master.after(0, progress_task, self.progress_box, self.puzzle_tracker, self.master)
        self.master.after(500, check_for_next_answer, self.master, self.puzzle_tracker, self.switch_controller, self.solution_text)

        self.master.after(1000, update_ip, self.master, self.ip_address, self.ip_text)
        # If self-destructing, do this:
        # self.master.after(34000, kill_task, self.master)

        # If mocking, do this:
        self.master.after(2500, push_button, self.master, self.switch_controller)

    def exit_method(self):
        self.master.after(0, kill_task, self.master)

    def start(self):
        self.master.mainloop()

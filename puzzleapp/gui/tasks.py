import sys

def test_task(label_text):
    print("Task running")
    label_text.set("Changed")


def puzzle_desc_task(label, puzzle_tracker, master):
    print("Setting Puzzle Desc")
    label.set(puzzle_tracker.get_next_puzzle_description())
    master.after(500, puzzle_desc_task, label, puzzle_tracker, master)

def quote_task(label, puzzle_tracker, master):
    print("Setting Quote")
    label.set(puzzle_tracker.get_next_puzzle_quote())
    master.after(500, quote_task, label, puzzle_tracker, master)

def progress_task(label, puzzle_tracker, master):
    print("Setting Progress")
    label.set(puzzle_tracker.get_progress_text())
    # TODO: Make a cool progress bar representation
    master.after(500, progress_task, label, puzzle_tracker, master)

def kill_task(master):
    print("Killing")
    master.destroy()
    sys.exit()

def auto_set_diag(puzzle_tracker):
    puzzle_tracker.set_diagnostics_ran(True)

def set_switch_input_text(master, switch_inputs, switch_controller):
    # print("Reading switches...")
    switch_inputs.set(switch_controller.input_as_string())

    # Register to execute again
    master.after(100, set_switch_input_text, master, switch_inputs, switch_controller)
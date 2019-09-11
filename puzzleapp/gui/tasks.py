import sys

def test_task(label_text):
    print("Task running")
    label_text.set("Changed")


def puzzle_desc_task(label, puzzle_tracker, master):
    # print("Setting Puzzle Desc")
    label.set(puzzle_tracker.current_puzzle_description())
    master.after(500, puzzle_desc_task, label, puzzle_tracker, master)

def quote_task(label, puzzle_tracker, master):
    # print("Setting Quote")
    label.set(puzzle_tracker.current_quote())
    master.after(500, quote_task, label, puzzle_tracker, master)

def progress_task(bar, puzzle_tracker, master):
    # print("Setting Progress")
    # label.set(puzzle_tracker.get_progress_text())
    bar['value'] = puzzle_tracker.get_progress_percent()
    # TODO: Make a cool progress bar representation
    master.after(500, progress_task, bar, puzzle_tracker, master)

def kill_task(master):
    print("Killing")
    master.destroy()
    sys.exit()

def push_button(master, switch_controller):
    # Simulate the user updating the switch values, and pushing the button
    print("Button Pushed.")
    switch_controller.simulate_button_push()
    master.after(3000, push_button, master, switch_controller)

def auto_set_diag(puzzle_tracker):
    puzzle_tracker.set_diagnostics_ran(True)

def set_switch_input_text(master, switch_inputs, switch_controller):
    # print("Reading switches...")
    switch_inputs.set(switch_controller.input_as_string())

    # Register to execute again
    master.after(50, set_switch_input_text, master, switch_inputs, switch_controller)

def check_for_next_answer(master, puzzle_tracker, switch_controller, solution_text):

    #print("Checking for button pushed and answer...")
    if(switch_controller.is_button_pushed()):
        print("Detected button pushed...")
        current_switch_state = switch_controller.input_as_array()
        if(puzzle_tracker.check_answer_against_switch_state(current_switch_state)):
            # Puzzle answered, move to next puzzle
            print("Puzzle Solved! Incrementing index.")
            puzzle_tracker.increment_puzzle_index()
            solution_text.set(puzzle_tracker.current_solution_text())

    master.after(50, check_for_next_answer, master, puzzle_tracker, switch_controller, solution_text)

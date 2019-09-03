import sys

def test_task(label_text):
    print("Task running")
    label_text.set("Changed")


def kill_task(master):
    print("Killing")
    master.destroy()
    sys.exit()

def set_switch_input_text(master, switch_inputs, switch_controller):
    # print("Reading switches...")
    switch_inputs.set(switch_controller.input_as_string())

    # Register to execute again
    master.after(100, set_switch_input_text, master, switch_inputs, switch_controller)
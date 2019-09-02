import sys

def test_task(label_text):
    print("Task running")
    label_text.set("Changed")


def kill_task(master):
    print("Killing")
    master.destroy()
    sys.exit()

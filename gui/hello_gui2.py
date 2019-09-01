import time
from tkinter import *
 
root = Tk()

label_text = StringVar()

root_bg = "#405659"
frame_bg = root_bg

# for debug, update frame color
#frame_bg = "green"

frame = Frame(root, bg=frame_bg)
frame.pack(side=LEFT, fill='both', expand='no')

w = Label(frame, font=("courier new", 20, "bold"), justify="left", textvariable=label_text, bg="#405659", fg="#b1e7f0")


def task():
    print("Task running")
    label_text.set("Changed")
    
 

# Full-screen mode
# w = Label(root, text="Hello, world!")


machine_text=" System Enabled\n Run Diagnostics..."
label_text.set(machine_text)



# w.place(x=50, y=50)

root.overrideredirect(True)

# Window uses:
# "width x height + x_offset + y_offset" (no spaces)

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg=root_bg)
root.focus_set()  # <-- move focus to this widget



# Pressing Escape kills the window
root.bind("<Escape>", lambda e: root.destroy())
w.pack()


root.after(1000, task)
root.mainloop()


print("Exit")

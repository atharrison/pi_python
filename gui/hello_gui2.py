from tkinter import *
 
root = Tk()
 

# Full-screen mode
w = Label(root, text="Hello, world!")
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget

# Pressing Escape kills the window
root.bind("<Escape>", lambda e: root.destroy())
w.pack()


root.mainloop()

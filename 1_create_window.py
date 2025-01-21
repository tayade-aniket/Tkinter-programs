# importing Tkinter
from tkinter import *

# This will help to create a window
root = Tk()

# let's create something to show on window
myLabel = Label(root, text="Namaste, Duniya !")
# For adding label on screen
myLabel.pack()

# this will hold window until we close it
root.mainloop()
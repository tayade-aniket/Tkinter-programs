from tkinter import *

root = Tk()

# creating labels
username = Label(root, text="Username")
password = Label(root, text="Password")

# creating input field
input1 = Entry(root)
input2 = Entry(root)

# packing components in grid
username.grid(row=0)
input1.grid(row=0, column=1)
password.grid(row=1, column=0)
input2.grid(row=1, column=1)

# Creating checkbox with correct columnspan
tick = Checkbutton(root, text="Keep me logged in")
tick.grid(columnspan=2)  

root.mainloop()

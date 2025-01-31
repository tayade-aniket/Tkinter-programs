from tkinter import *

root = Tk()

label1 = Label(root, text="This is Label 1")
label2 = Label(root, text="This is Label 2")

label1.place(x=10, y=10)
label2.place(x=10, y=30)


root.mainloop()
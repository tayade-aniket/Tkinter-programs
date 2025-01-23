from tkinter import *

root = Tk()
root.geometry("300x300")

# creating three functions for Left, Right, Scroll click respectively.
# Left Click
def leftClick(event):
    print("You just clicked Left Button !")

# Right Click
def rightClick(event):
    print("You just clicked Right Button !")

# Scroll
def scroll(event):
    print("You just scrolled the Window !")

# creating frame
frame = Frame(root, width=350, height=350)
frame.bind("<Button-1>", leftClick)             # <Button-1> is Left Click
frame.bind("<Button-2>", scroll)                # <Button-2> is Scroll
frame.bind("<Button-3>", rightClick)            # <Button-3> is Right Click
frame.pack()


root.mainloop()
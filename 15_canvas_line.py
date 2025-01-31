from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=250, bg="#ffffff")
canvas.pack()

# Creating Line
line = canvas.create_line(0,0,200,100)
# we use 0,0,200,100 that means First two values are the co-ordinets of X Axis and The last one are co-ordinents of Y axis

blue_line = canvas.create_line(200,100, 0, 200, fill="blue")

root.geometry("300x350")
root.mainloop()
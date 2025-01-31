from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=350, bg="#ffffff")
canvas.pack()

canvas.create_rectangle(100, 100, 300, 200, fill='green', outline='green')


root.mainloop()
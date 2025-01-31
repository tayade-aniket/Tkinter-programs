from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=350, bg="#ffffff")
canvas.pack()

canvas.create_rectangle(100, 100, 300, 300, fill='green', outline='green')
canvas.create_oval(100, 100, 300, 300, fill='orange', outline='orange')

root.mainloop()
from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=350, bg="#ffffff")
canvas.pack()

canvas.create_arc(50, 50, 300, 300)

# We alos can pass the degree as extent value 
# canvas.create_arc(100, 100, 250, 250, extent=120)

root.mainloop()
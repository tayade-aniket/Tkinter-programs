from tkinter import *

root = Tk()

canvas = Canvas(width=600, height=400, bg="#FFFFFF")
canvas.pack()


points = [250, 110, 480, 200, 280, 280, 250, 110]
canvas.create_polygon(points, fill="green", outline="green")

root.mainloop()
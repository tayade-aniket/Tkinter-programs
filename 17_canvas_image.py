# Here we need to understand that we can add image on our Canvas but that Image should be
# in PNG of GIF format Other than this Extensions format is not accessible by Tkinter

from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=350, bg="#FFFFFF")
canvas.pack()

# Here we need to pass the complete path to the file
photo = PhotoImage(file='D://Data Science & AI//Tkinter//assets//logo.PNG')
canvas.create_image(20,20, image=photo, anchor=NW)
# anchor is the position from where we want to display our Image

root.geometry("450x400")
root.mainloop()


from tkinter import *
from tkinter import messagebox

# Define function
def my_fun():
    answer = messagebox.askyesnocancel("Exit", "Do You Really Want to Exit ?")
    if answer:
        root.quit()

# We also can use askokcancel, askretrycancel, askyesno & askyesnocancel

root = Tk()

btn = Button(root, text="Exit", command=my_fun)
btn.pack()

root.geometry("250x300")
root.mainloop()
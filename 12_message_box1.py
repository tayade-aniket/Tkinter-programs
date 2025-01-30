from tkinter import *
from tkinter import messagebox

# Define function
def my_fun():
    messagebox.showinfo("Magic Message", "You are Cute !!!!")

#  We also can use 'showerror & showwarning

root = Tk()

btn = Button(root, text="Magic Button", command=my_fun)
btn.pack()

root.geometry("400x400+120+120")
root.mainloop()
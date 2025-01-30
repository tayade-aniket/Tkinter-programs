from tkinter import *
from tkinter import messagebox

# Define function
def my_fun():
    answer = messagebox.askquestion("Exit", "Do You Really Want to Exit ?")
    if answer == 'yes':
        root.quit()


root = Tk()

btn = Button(root, text="Magic Button", command=my_fun)
btn.pack()

root.geometry("400x400+120+120")
root.mainloop()
from tkinter import *

def result():
    print(i.get())

root = Tk()

# to getting response in Int type like 0,1
i = IntVar()

# creating a checkbox
option1 = Checkbutton(root, text="Option", variable=i)
option1.pack()


# We also can use StringVar to get customized responses like follow -
# i = StringVar()

# creating a checkbox
# option2 = Checkbutton(root, text="Option", variable=i, offvalue="Unchecked", onvalue="Checked")
# option2.pack()


btn = Button(root, text="Result", command=result)
btn.pack()


root.geometry("300x400")
root.mainloop()
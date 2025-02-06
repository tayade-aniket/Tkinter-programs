from tkinter import *

def result():
    print(i.get())

root = Tk()

i = IntVar()

r1 = Radiobutton(root, text="Male", value=1, variable=i)
r2 = Radiobutton(root, text="Female", value=2, variable=i)

r1.pack()
r2.pack()

btn = Button(root, text="Check", command=result)
btn.pack()

root.geometry("300x350")
root.mainloop()

# We can create multiple radio groups on one window but they should on different Frame. Different Frames can 
# have different Radio Groups.
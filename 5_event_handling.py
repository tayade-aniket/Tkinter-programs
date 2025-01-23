from tkinter import *

root = Tk()
root.geometry("400x450")

##### WAY 1
# Creating a function
def calling():
    print("I'm Called by Button!")

# creating button
button = Button(root, text="Click Me", command=calling)
button.pack()


##### WAY 2
def recieving(event):
    print("Hi there !")

button1 = Button(root, text="Magic Button")
button1.bind("<Button-1>", recieving)
button1.pack()

root.mainloop()

# When click on the Button you'll get output on console.
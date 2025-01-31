from tkinter import *

def data_fetch():
    data = str.get()
    
    if(data):
        print(data)
    else:
        print("Data didn't Fetch !")

root = Tk()

str = StringVar()
entry = Entry(root, textvariable=str)
str.set("Welcome")
entry.pack()

button = Button(root, text="Get Data", command=data_fetch)
button.pack()

root.geometry("300x350")
root.mainloop()
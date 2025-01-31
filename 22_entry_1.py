from tkinter import *

def data_fetch():
    data = entry.get()
    
    if(data):
        print("Data Fetch Successfully !")
    else:
        print("Data didn't Fetch !")

root = Tk()

entry = Entry(root)
entry.pack()

button = Button(root, text="Get Data", command=data_fetch)
button.pack()

root.geometry("300x350")
root.mainloop()
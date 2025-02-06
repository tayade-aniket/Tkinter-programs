from tkinter import *

root = Tk()

# creating List box
lang = Listbox(root, width=30, height=15, selectmode=EXTENDED)
# we can change the select mode by simply passing the following values to the selectmode.
# BROWSE, SINGLE, MULTIPLE and EXTENDED

# adding list items to the list
lang.insert(1, "Python")        
lang.insert(2, "JavaScript")    
lang.insert(3, "C")             
lang.insert(4, "C++")
lang.insert(5, "C#")
lang.insert(6, "Java")
lang.insert(7, "Go")


lang.pack()

root.geometry("300x350")
root.mainloop()
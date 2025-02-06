from tkinter import *

root = Tk()

# creating List box
lang = Listbox(root, width=30, height=15)    
# By default each value can contains 20 character in the list box row and 
# Height is 10 by default means it can show upto 10 items in the listbox. for more than 10 items it will
# add a scrollbar, we also can change the height too. 


# adding list items to the list
lang.insert(1, "Python")        # Here we pass two arguments fist is index and second is Value
lang.insert(2, "JavaScript")    
lang.insert(3, "C")             
lang.insert(4, "C++")
lang.insert(5, "C#")
lang.insert(6, "Java")
lang.insert(7, "Go")


lang.pack()

root.geometry("300x350")
root.mainloop()
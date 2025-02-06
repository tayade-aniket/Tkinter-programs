from tkinter import *

def result():
    selected_item = lang.curselection()
    # print(selected_item)                    #It will return a tuple because user can select multiple values 
    for item in selected_item:
        print(lang.get(item))


def delete_item():
    selected_item = lang.curselection()
    for item in selected_item:
        print(lang.delete(item))

root = Tk()
# creating List box
lang = Listbox(root, width=30, height=15, selectmode=MULTIPLE)

# adding list items to the list
lang.insert(1, "Python")        
lang.insert(2, "JavaScript")    
lang.insert(3, "C")             
lang.insert(4, "C++")
lang.insert(5, "C#")
lang.insert(6, "Java")
lang.insert(7, "Go")
lang.pack()

btn = Button(root, text="Show Result", command=result).pack()
del_btn = Button(root, text="Delete", command=delete_item).pack()


root.geometry("300x350")
root.mainloop()
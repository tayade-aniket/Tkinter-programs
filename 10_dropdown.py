from tkinter import *

def test():
    print("Hello There !")

root = Tk()

# create a Menu
main_menu = Menu(root)

# attaching Menu to Window
root.config(menu=main_menu)

#  Creating File Menu
fileMenu = Menu(main_menu)
main_menu.add_cascade(label = "File", menu=fileMenu)

# Creating Edit Menu
editMenu = Menu(main_menu)
main_menu.add_cascade(label = "Edit", menu=editMenu)

# Adding Options to the File Menu
fileMenu.add_command(label = "New", command=test)
fileMenu.add_command(label = "New Window", command=test)
fileMenu.add_command(label = "Open", command=test)
# To add Seperator line 
fileMenu.add_separator()

fileMenu.add_command(label = "Save", command=test)
fileMenu.add_command(label = "Save As", command=test)
# To add Seperator line 
fileMenu.add_separator()

fileMenu.add_command(label = "Page Setup", command=test)
fileMenu.add_command(label = "Print", command=test)
fileMenu.add_command(label = "Exit", command=test)


root.mainloop()
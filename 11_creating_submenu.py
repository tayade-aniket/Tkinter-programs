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

# Creating View Menu
viewMenu = Menu(main_menu)
main_menu.add_cascade(label = "View", menu=viewMenu)

zoomMenu = Menu(viewMenu)
zoomMenu.add_command(label = "Zoom In", command=test)
zoomMenu.add_command(label = "Zoom Out", command=test)

viewMenu.add_cascade(label = "Zoom", menu=zoomMenu)

root.mainloop()
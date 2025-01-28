from tkinter import *

#  create a class
class myButtons :
    def __init__(self, master):
        # First button to print MSG
        self.printButton = Button(master, text="Click Me", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        # Second Button to Quit Window
        self.quitButton = Button(master, text="Close", command=master.quit)
        self.quitButton.pack(side=LEFT)

    # Function 
    def printMessage(self):
        print("Welcome")
    
root = Tk()
# Object for class
button = myButtons(root)

root.mainloop()
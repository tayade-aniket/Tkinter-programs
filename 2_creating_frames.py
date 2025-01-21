# In Tkinter, a Frame is a container widget that is used to organize other widgets in a rectangular area on the 
# screen. It is a useful way to group and arrange related widgets within a window (or parent widget). 
# A Frame itself does not display anything, but it helps in organizing the layout by providing a structure 
# that can hold other widgets, such as labels, buttons, and text fields.


from tkinter import *

root = Tk()

# Creating Frame using Frame Class
# We can create multiple frames in one program.
frame = Frame(root)

# Creating button component
button1 = Button(frame, text="Click Me")
button2 = Button(frame, text="Close Me")

button1.pack()      # Here we can pass side value inside pack like button1.pack(side=LEFT)
button2.pack()      # Also there are 4 values which we can use as side - TOP, BOTTOM, LEFT, RIGHT
frame.pack()

root.mainloop()
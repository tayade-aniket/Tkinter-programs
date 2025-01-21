from tkinter import *

root = Tk()
root.geometry("400x450")  # Set the window size properly

# Create frames for organization
logo_frame = Frame(root, height=100, bg="crimson")
navbar_frame = Frame(root, height=50, bg="grey")
sidebar_frame = Frame(root, width=100, bg="green")

# Pack the frames into the root window
logo_frame.pack(fill=X)  # Horizontally fill the top part of the window
navbar_frame.pack(fill=X)  # Horizontally fill the next part for navbar

# Sidebar should be packed in the left side, filling vertically
sidebar_frame.pack(side=LEFT, fill=Y)

# Add text labels to each frame
logo = Label(logo_frame, text="Logo", bg="crimson")
navbar = Label(navbar_frame, text="Navbar", bg="grey")
sidebar = Label(sidebar_frame, text="Sidebar", bg="green")

logo.pack()
navbar.pack()
sidebar.pack()

root.mainloop()

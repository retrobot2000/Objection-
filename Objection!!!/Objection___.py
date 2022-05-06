# Import the appropriate libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage

# How this works is when you see the prosecutor pop up, click him and an objection will appear next to him
# If you see an objection next to Phoenix, click on the objection and one will pop up on the prosecutors side
# Game over if you touch any empty space, an objection on the prosecutors side, if you don't hit the keys on time, or Phoenix
# Game win after 10 successful counters

###########
# Tkinter #
###########

# Create welcome window
welcome = tk.Tk()
# Set title
welcome.title("Ace Attorney: Menu")
# Set window size
welcome.geometry("300x300")

# Create main game window
win = tk.Tk()
# Set title
win.title("Ace Attorney")
# Set window size
win.geometry("1600x300")

##########
# Images #
##########
PW = PhotoImage(file="phoenix-wright.png")
ME = PhotoImage(file="miles-edgeworth.png")
OBJ = PhotoImage(file="objection.png")
E = PhotoImage(file="Empty.png")

# Columns for Phoenix
buttonname = tk.Button(image= PW)
buttonname.grid(row=0,column=1)

# Objection Columns
buttonname = tk.Button(image= E)
buttonname.grid(row=0,column=2)
# Swap for column 2
buttonname = tk.Button(image= E)
buttonname.grid(row=0,column=3)
# Swap for column 3


# Edgeworth Columns
buttonname = tk.Button(image= E)
buttonname.grid(row=0,column=4)

##############
# Win Screen #
##############

###############
# Lose Screen #
###############

tk.mainloop()
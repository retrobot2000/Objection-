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
# Windows #
###########
def wel_win():
	""" Create welcome window """
	global win
	window.destroy()
	welcome = tk.Tk()
	# Set title
	welcome.title("Ace Attorney: Menu")
	# Set window size
	welcome.geometry("300x300")

def set_win():
	""" Create settings window """
	global win
	window.destroy()
	settings = tk.Tk()
	# Set title
	settings.title("Ace Attorney: Settings")
	# Set window size
	settings.geometry("300x300")

def gme_win():
	""" Create Game window """
	global win
	window.destroy()
	game = tk.Tk()
	# Set title
	game.title("Ace Attorney: Menu")
	# Set window size
	game.geometry("900x300")


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

##########
# Images #
##########
def load_images():
	""" Loads all images because it can """
	PW = PhotoImage(file="phoenix-wright.png")
	ME = PhotoImage(file="miles-edgeworth.png")
	OBJ = PhotoImage(file="objection.png")
	E = PhotoImage(file="Empty.png")

##############
# Win Screen #
##############

###############
# Lose Screen #
###############

tk.mainloop()
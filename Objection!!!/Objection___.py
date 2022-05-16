# Import the appropriate libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage

# How this works is when you see the prosecutor pop up, click him and an objection will appear next to him
# If you see an objection next to Phoenix, click on the objection and one will pop up on the prosecutors side
# Game over if you touch any empty space, an objection on the prosecutors side, if you don't hit the keys on time, or Phoenix
# Game win after 20 seconds pass

##########
# Images #
##########

def load_images():
	""" Loads all images because it can """
	global PW
	global ME
	global OBJ
	global E
	global L
	PW = PhotoImage(file="phoenix-wright.png")
	ME = PhotoImage(file="miles-edgeworth.png")
	OBJ = PhotoImage(file="objection.png")
	E = PhotoImage(file="Empty.png")
	L = PhotoImage(file="Logo.png")

###########
# Buttons #
###########

def gme_click(argument):
	argument
	gme_win()
def set_click(argument):
	argument
	set_win()
def ext_click(argument):
	argument
	window.destroy()

###########
# Windows #
###########

def wel_win():
	""" Create welcome window """
	global window
	window = tk.Tk()
	# Set title
	window.title("Ace Attorney: Menu")
	# Set window size
	window.geometry("1600x700")

	# Load images for intro graphic
	load_images()

	# Create a label and put an image on
	lbl = tk.Label(window,image=L)
	lbl.grid(row=0,column=0,columnspan=3)

	#  Buttons for start, settings, and exit
	gmebtn = tk.Button(window,text='Begin',width=30,height=5,command= lambda b="gme_click" :gme_click(b))
	gmebtn.grid(row=1,column=0)

	stgbtn = tk.Button(window,text='Settings',width=30,height=5,command= lambda b="set_click" :set_click(b))
	stgbtn.grid(row=1,column=1)	

	extbtn = tk.Button(window,text='Exit',width=30,height=5,command= lambda b="ext_click" :ext_click(b))
	extbtn.grid(row=1,column=2)


def set_win():
	""" Create settings window """
	global window
	window.destroy()
	window = tk.Tk()
	# Set title
	window.title("Ace Attorney: Settings")
	# Set window size
	window.geometry("1600x600")
	
	# Load images for intro graphic
	load_images()

def gme_win():
	""" Create Game window """
	global window
	window.destroy()
	window = tk.Tk()
	# Set title
	window.title("Ace Attorney: OBJECTION!!!")
	# Set window size
	window.geometry("1600x600")

	# Load images for intro graphic
	load_images()

	# Empty 1st row
	lbl = tk.Label(window,image=E)
	lbl.grid(row=0,column=0)
	lbl = tk.Label(window,image=E)
	lbl.grid(row=0,column=1)
	lbl = tk.Label(window,image=E)
	lbl.grid(row=0,column=2)
	lbl = tk.Label(window,image=E)
	lbl.grid(row=0,column=3)

	# Columns for Phoenix
	buttonname = tk.Button(image= PW)
	buttonname.grid(row=1,column=0)

	# Objection Columns
	buttonname = tk.Button(image= E)
	buttonname.grid(row=1,column=1)
	# Swap for column 1


	buttonname = tk.Button(image= E)
	buttonname.grid(row=1,column=2)
	# Swap for column 2


	# Edgeworth Columns
	buttonname = tk.Button(image= E)
	buttonname.grid(row=1,column=3)



wel_win()

tk.mainloop()
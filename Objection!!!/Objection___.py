#import the appropriate libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage

#create our window
win = tk.Tk()
#set its title
win.title("OBJECTION")
#set the window size
win.geometry("300x300")

#create the 3 variables to hold the images
PW = PhotoImage(file="phoenix-wright.png")
ME = PhotoImage(file="miles-edgeworth.png")
OBJ = PhotoImage(file="objection.png")

buttonname = tk.Button(image= PW)
buttonname.grid(row=0,column=1)

tk.mainloop()
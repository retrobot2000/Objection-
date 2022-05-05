#import the appropriate libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import PhotoImage
#test me
#create our window
win = tk.Tk()
#set its title
win.title("Ace Attorney")
#set the window size
win.geometry("1600x300")

#create the 3 variables to hold the images
PW = PhotoImage(file="phoenix-wright.png")
ME = PhotoImage(file="miles-edgeworth.png")
OBJ = PhotoImage(file="objection.png")
E = PhotoImage(file="Empty.png")

buttonname = tk.Button(image= PW)
buttonname.grid(row=0,column=1)

buttonname = tk.Button(image= E)
buttonname.grid(row=0,column=2)
buttonname = tk.Button(image= E)
buttonname.grid(row=0,column=3)

buttonname = tk.Button(image= ME)
buttonname.grid(row=0,column=4)
tk.mainloop()
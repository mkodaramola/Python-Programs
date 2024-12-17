import tkinter as tk
from tkinter import ttk
from tkinter import *
import os


# tkinter => {* | ttk => {Button, Frame, Label, Style} | font => {Font} } 
root = tk.Tk()


#--- Properties of Window

#title
root.title("Jarvis")
#width, height, x, y
root.geometry('1200x650+100+50')
#resize
root.resizable(True,False)
#transparency
root.attributes('-alpha',1)
root.attributes('-topmost',0)



text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

label = ttk.Label(root)
label.configure(text=text, font=('Times','10','bold'),background="green",foreground="white",width="30")
label.pack(fill='x',padx=0,pady=10)

frame = ttk.Frame(root)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(0,weight=3)
frame.configure(borderwidth = "15")
frame.pack()





entryInput = ttk.Entry(frame)
entryInput.insert('end',"Entry Widget")
entryInput.configure(show='',state='disabled',background="green",foreground="#4AC", font=('Time','15','italic'))
entryInput.grid(column=1,row=0,sticky= tk.W)


textInput = Text(frame)
textInput.insert('end',"Text Widget")
textInput.configure(state="disabled",background="red",foreground="#FFF", font=('Time','15','italic'),height="1")
textInput.grid(column=2,row=0,sticky= tk.E,padx=40)


frame2 = ttk.Frame(root)
frame2.configure(borderwidth="15")
frame2.pack(fill="x")
st = tk.EW
for i in range(3):
	for j in range(3):
		lbl = ttk.Label(frame2)
		t = f"This is row {i} column {j}"
		lbl.configure(text = t,background="#000", foreground="#FFF",font=("Times","20","bold"))
		if j == 1:
			st = tk.W
		elif j == 2:
			st = tk.EW
		elif j == 3:
			st = tk.E

		lbl.grid(row=i, column=j,padx=55,pady=15,sticky=st)
		

print(__name__)

root.mainloop()
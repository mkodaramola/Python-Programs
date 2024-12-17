from pynput import keyboard
import pyautogui as pg
import os
from tkinter import *
from tkinter.ttk import Label

opengame = False

root = Tk()

root.wm_title("DaraTronics")

root.configure(background="green")


def cont():
	root.destroy()
	opengame = True



#resize
root.resizable(False,False)

#transparency
root.attributes('-alpha',1)
root.attributes('-topmost',0)

label = Label(root, font=("Times","20"),text="Click the 'Go to Game' button to continue\nPress Escape key to quit when you're done playing game.")
label.pack(padx=(50,20),pady=(20,20))

label2 = Label(root, font=("Times","10"),text="Credit: Keyboard-control programmed to this game by Daramola Oluwafemi Michael (14th Sept, 2022) [DaraTronics]")
label2.pack(padx=(50,20),pady=(20,20))

button = Button(root,text="Go to Game", command=cont)
button.pack()


root.mainloop()



def onPress(key):
	try:
		print(f'{key.char}')
	except AttributeError:
		print(f'{key}')
		if (key == keyboard.Key.up):
			pg.mouseDown(x=706,y=500,button='left')
		elif (key == keyboard.Key.left):
			pg.mouseDown(x=913,y=375,button='left')
		elif (key == keyboard.Key.right):
			pg.mouseDown(x=713,y=375,button='left')
		elif (key == keyboard.Key.down):
			pg.mouseDown(x=706,y=200,button='left')
		


			


def onRelease(key):
	print(f"{key} Released")
	if (key == keyboard.Key.up):
		pg.dragTo(706,200,duration=0)
	elif (key == keyboard.Key.left):
		pg.dragTo(713,375,duration=0)
	elif (key == keyboard.Key.down):
		pg.dragTo(706,500,duration=0)
	elif (key == keyboard.Key.right):
		pg.dragTo(913,375,duration=0)
			
	if (key == keyboard.Key.esc):
		if opengame == True:
			pg.hotkey("alt","tab")
			pg.hotkey("alt","tab")
			pg.hotkey("alt","f4")
			return False
		






os.startfile("C:\\Program Files (x86)\\Subway Surfers\\Subway_Surfers.exe")

opengame = True

with keyboard.Listener(on_press = onPress,on_release = onRelease) as listener:
	listener.join()

import tkinter as tk
from tkinter import *
from tkinter.ttk import Button,Frame,Label,Style, Combobox, LabelFrame
from threading import Thread


def inter():
		# tkinter => {* | ttk => {Button, Frame, Label, Style} | font => {Font} } 
	root = tk.Tk()


	#--- Properties of Window

	scrW = root.winfo_screenwidth()
	scrH = root.winfo_screenheight()

	#title
	root.title("Jarvis")
	#width, height, x, y
	root.geometry('1200x650+100+50')
	#resize
	root.resizable(True,False)
	#transparency
	root.attributes('-alpha',1)
	root.attributes('-topmost',0)

	lf1 = LabelFrame(root, width=scrW, text=f"Lower Bound")
	lf1.pack(expand=True,fill=BOTH, padx=10, pady=10)

	LH = Label(lf1,text="H :")
	LH.place(x=10,y=20)


	LHslider = Scale(lf1,from_=0,to=180,orient=HORIZONTAL)
	LHslider.place(x=50,y=0)


		

	LHslider.configure(command=opencv)


	LS = Label(lf1,text="S :")
	LS.place(x=10,y=70)

	LSslider = Scale(lf1,from_=0,to=255,orient=HORIZONTAL)
	LSslider.place(x=50,y=50)


	LV = Label(lf1,text="V :")
	LV.place(x=10,y=120)

	LVslider = Scale(lf1,from_=0,to=255,orient=HORIZONTAL)
	LVslider.place(x=50,y=100)




	lf2 = LabelFrame(root, width=scrW, text=f"Upper Bound")
	lf2.pack(expand=True,fill=BOTH, padx=10, pady=10)

	UH = Label(lf2,text="H :")
	UH.place(x=10,y=20)

	UHslider = Scale(lf2,from_=0,to=255,orient=HORIZONTAL)
	UHslider.place(x=50,y=0)

	US = Label(lf2,text="S :")
	US.place(x=10,y=70)

	USslider = Scale(lf2,from_=0,to=255,orient=HORIZONTAL)
	USslider.place(x=50,y=50)



	UV = Label(lf2,text="V :")
	UV.place(x=10,y=120)

	UVslider = Scale(lf2,from_=0,to=255,orient=HORIZONTAL)
	UVslider.place(x=50,y=100)


	# def opencv(e):
	# 	cap = cv2.imread('cp.jpg',1)
	# 	while True:
	# 		cap = cv2.resize(cap,(600,400))
	# 		hsv = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)

	# 		lower_blue = np.array([LHslider.get(),LSslider.get(),LVslider.get()])
	# 		upper_blue = np.array([UHslider.get(),USslider.get(),UVslider.get()])

	# 		mask = cv2.inRange(hsv,lower_blue, upper_blue)
	# 		result = cv2.bitwise_and(cap,cap, mask=mask)
	# 		cv2.imshow('Remove Blue',result)
	# 		# cv2.imshow('mask',mask)
	# 		# cv2.imshow('HSV',hsv)
	# 		if cv2.waitKey(1) == ord('q'):
	# 			break
	# 	cv2.destroyAllWindows()

	root.mainloop()



def opencv(e):
	import numpy as np
	import cv2


	# cap = cv2.VideoCapture(0)

	cap = cv2.imread('cp.jpg',1)
	#cap = cv2.resize(cap,(600,400))
	while True:
		# ret, frame = cap.read()
		# cap = cv2.resize(cap,(600,400))
		# width = int(cap.get(3))
		# height = int(cap.get(4))

		cap = cv2.resize(cap,(600,400))


		hsv = cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)	#white-> blue, blue -> white

		# lower_blue = np.array([90,50,50])
		# upper_blue = np.array([130,255,255])

		lower_blue = np.array([0,120,120])
		upper_blue = np.array([100,255,255])

		mask = cv2.inRange(hsv,lower_blue, upper_blue)
		result = cv2.bitwise_and(cap,cap, mask=mask)


	 
		cv2.imshow('Remove Blue',result)
		# cv2.imshow('mask',mask)
		# cv2.imshow('HSV',hsv)
		if cv2.waitKey(1) == ord('q'):
			break
	# cap.release()
	cv2.destroyAllWindows()

t1 = Thread(target=inter)
t2 = Thread(target=opencv)

t1.start()
t2.start()
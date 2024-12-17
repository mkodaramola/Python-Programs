from vosk import Model, KaldiRecognizer
import pyaudio
from conv import CONV
from JVR import tool
import tkinter as tk
from tkinter.font import Font
from tkinter.ttk import Button,Frame,Label,Style
from PIL import ImageTk, Image




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
root.attributes('-alpha',0.9)
root.attributes('-topmost',0)


#--- Setting Background Image

img = Image.open("bg.jpg")
img = img.resize((1200,650))
bg = ImageTk.PhotoImage(img)
bg_label = Label(root, image=bg)
bg_label.place(x=0,y=0)



 

model = Model(r"C:\Users\user\Documents\Programming\Python\Packages\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")

r = KaldiRecognizer(model,16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
stream.start_stream()

active = False



while True:

	 data = stream.read(4096,exception_on_overflow=False)
	 if r.AcceptWaveform(data):	
	 	text = r.Result() 
	 	text = text[14:-3]
	 	print(text)

	 	if (text[0:6] == "jarvis" or text[0:6] == "johnny" or text[0:3]=="gov" or text[0:6] == "travis" or text[0:7]=="daddy's"  or text[0:6] == "chavis"  or text[0:6] == "davies" or text[0:7] == "jerry's" or text[0:6] == "jervis" or text[0:14]=="justice league" or text[0:4]=="joey" or "douglas" in text  or text[0:8]=="japanese" or text[0:4] == "john" or text[0:4] == "jack" or text[0:6]=="judges"  or text[0:3] == "job" or text[0:3] == "jav" or text[0:5]=="jones" or text[0:9]== "germany's"):																					 				
	 		active = True
	 	if active:
	 		CONV.conv(text)
	 		if (text[0:6] == "jarvis" or text[0:7] == "jerry's" or text[0:6] == "jervis" or text[0:4]=="joey" or "douglas" in text  or text[0:8]=="japanese" or text[0:8] == "johnny's" or text[0:8] == "jackie's" or text[0:6]=="judges" or text[0:3] == "job" or text[0:5]=="jones" or text[0:9]== "germany's") and ("in" in text or ("go" in text and "inactive" in text) or "hibernate" in text or (("i " in text or "buy" in text) and ("neat" in text or "need" in text or "meat" in text))):
	 			CONV.hibernate()

	 			active = False
	 	

		


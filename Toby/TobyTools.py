import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio
import psutil as ps
import random
from datetime import date 
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui as pg
from time import sleep
import urllib.request as req
from pyfirmata import Arduino, util



class tool:
	#date
	d = date.today()
	day = d.day
	month = d.strftime('%B')
	year = d.year
	wkd = d.strftime('%A')
	t = datetime.now()
	hr = t.hour
	min = t.minute
	speechControl = False
	sec = t.second
	ost = False
	save_ST = False
	name_ST = False	
	ext_ST = False
	shutdown = False
	restart = False
	workMode = False
	googleQ = False
	googleW = ""
	bat3Time = False

	try:
		board = Arduino('COM18')
		print('Communication Successful!')

		it = util.Iterator(board)
		it.start()
	except:
		print("No Arduino found")



	def internetAccess():	
		try:
			req.urlopen('http://google.com')
			return True
		except:
			return False


	def playMusic():
		pg.hotkey('winleft','e')

		sleep(3)

		music = pg.locateCenterOnScreen("music.png")
		pg.doubleClick(music)

		sleep(2)

		songs = pg.locateCenterOnScreen("mysong.png")
		pg.doubleClick(songs)

		sleep(1)

		praise = pg.locateCenterOnScreen("praise.png")
		pg.click(praise,button='right')


		sleep(1)

		play = pg.locateCenterOnScreen("play.png")
		pg.click(play)

	def textToNum(t):

		def ttd(t):
			teens = {'thir':13,'four':14,'fif':15,'six':16,'seven':17,'eight':18,'nine':19}
			tys = {'twen':20,'thir':30,'four':40,'fif':50,'six':60,'seven':70,'eight':80,'nine':90}
			units = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'hundred':0}

			if "teen" in t:
				t = t.replace('teen', '')
				t= t.strip()
				t = t.lower()
				dkeys = list(teens.keys())
				dvalues = list(teens.values())
				for i in range(len(teens)):
					if t == dkeys[i]:
						return dvalues[i]
			elif t[-2:] == 'ty':
				t = t.replace('ty', '')
				t= t.strip()
				t = t.lower()
				dkeys = list(tys.keys())
				dvalues = list(tys.values())
				for i in range(len(tys)):
					if t == dkeys[i]:
						return dvalues[i]
			else:
				dkeys = list(units.keys())
				dvalues = list(units.values())
				for i in range(len(units)):
					if t == dkeys[i]:
						return dvalues[i]
		

		t = t.replace(',','')
		t = t.replace(' and','')
		num = 0

		def Analyse(t):
			b = ""
			m = ""
			th = ""
			h = ""

			if "billion" in t:
				b = t[0:t.find('billion')-1]
				t = t[t.find('billion')+8:len(t)]
			if "million" in t:
				m = t[0:t.find('million')-1]
				t = t[t.find('million')+8:len(t)]
			if "thousand" in t:
				th = t[0:t.find('thousand')-1]
				t = t[t.find('thousand')+9:len(t)]
			h = t


			return [b,m,th,h]


		def toNum(t):
			a = t.split(' ')
			s = 0
			temp=1
			for i in range(len(a)):
				num = ttd(a[i])
				if num == 0:
					s *= 100
				else:
					s+=num	
				
			return s


		arr = Analyse(t)
		print (arr)
		f_sum = [0]*4
		ff_sum = 0
		for i in range(4):
			if arr[i] == '':
				continue
			else:
				f_sum[i] = toNum(arr[i])
				if i == 0:
					f_sum[i]*=1000000000
					
				if i == 1:
					f_sum[i]*=1000000
				
				if i == 2:
					f_sum[i]*=1000

		for i in range(4):
			ff_sum+=f_sum[i]



		return ff_sum






	def speechCtrl(text):

		if ("page"in text or "pledge" in text) and ("up" in text or "op" in text or "or" in text):
			pg.press('pageup')
		elif ("sw"in text and "ch"in text):
			pg.hotkey('winleft','tab')
		elif ("page"in text or "pledge" in text) and ("down" in text or "don't" in text or "though" in text):
			pg.press('pagedown')
		elif "explorer"in text:
			pg.hotkey('winleft','e')
		elif "explorer"in text:
			pg.press('winleft')
		elif "stop" in text and ("spe" in text or "control" in text):
			tool.speechControl = False
		elif "close"in text or "clues" in text or "news" in text:
			pg.hotkey('alt','f4')
		elif ("dex"in text or "jax" in text) and ("op" in text or "er" in text):
			pg.hotkey('winleft','d')
		elif "space" in text:
			pg.press('space')
		elif "start"in text or "stat" in text or "staff" in text or "stuff" in text:
			pg.press('winleft')

		elif "up" in text or "op" in text or "hope" in text:
			pg.press('up')

		elif "down"in text or "don't" in text or "though" in text or text == "damn":
			pg.press('down')
		elif "left"in text or "lift" in text:
			pg.press('left')

		elif "right"in text:
			pg.press('right')
		elif "rename"in text:
			pg.press('f2')
		elif ("space"in text or "peace" in text) and "b" in text:
			pg.press('backspace')
		
		elif "tab"in text or "top" in text:
			pg.press('tab')
		elif "enter"in text or "return" in text:
			pg.press('enter')
		elif "copy"in text or "opie" in text:
			pg.hotkey('ctrl','c')
		elif "min"in text or "ni" in text:
			pg.hotkey('winleft','down')
		elif "max"in text or "mug" in text or "my my" in text:
			pg.hotkey('winleft','up')
		elif "paste"in text or "best" in text or "beast" in text:
			pg.hotkey('ctrl','v')
		elif "lock"in text:
			pg.hotkey('winleft','l')
		elif "screen"in text or "shot" in text:
			im = pg.screenshot()
		elif ("save"in text or "safe" in text) and ("file" in text or "five" in text):
			pg.hotkey('ctrl','s')
		elif ("select"in text or "let's" in text) and ("all" in text or "oh" in text or "lo" in text):
			pg.hotkey('ctrl','a')
		elif text[0:5]== "on do" or text[0:6]=="and do" or text[0:4]=="undo":
			pg.hotkey('ctrl','z')
		elif "re"in text and " do" in text:
			pg.hotkey('ctrl','y')

		
		






	def timeleft(s):

		h = s//3600
		ns = s - (h *3600)
		m = ns//60
		nns = ns - (m*60)
		if h == 0 and m == 0:
			return f'{nns} seconds'
		elif h== 0:
			return f'{m} minutes, {nns} seconds'
		else:
			return f'{h} hours, {m} minutes, {nns} seconds'


	def batteryDetails():
		battery = ps.sensors_battery()
		t = battery.secsleft
		p = battery.percent
		pp = battery.power_plugged

		print ("Percentage:", battery.percent)

		print ("Seconds left:", battery.secsleft)

		print ("Seconds left:", battery.power_plugged)
		t_msg = ""
		pp_msg = ""

		if type(t) != int:
			t_msg = "cannot be determined"
		else:
			t_msg = tool.timeleft(t)

		if pp == True:
			pp_msg = 'yes'
		else:
			pp_msg = 'no'

		return str(p),pp_msg,t_msg











# Find meaning of words
	def dFind(word):
		fob = open("dictionary.txt")
		t = fob.readlines()

		for i in range(len(t)):
			t[i] = t[i].lower()
			if(t[i][0:len(word)] == word):
				
				t[i]=t[i].replace(word,"",1)
				t[i]=t[i].replace("adj.","")
				t[i]=t[i].replace("—n","")
				t[i]=t[i].replace("—adv","")
				t[i]=t[i].replace("adv.","")
				t[i]=t[i].replace("—attrib.","")
				t[i]=t[i].replace("n.","")
				t[i]=t[i].replace(" v. "," ")
				t[i]=t[i].replace("—v.","in verb form,")
				t[i]=t[i].replace("—","")
				t[i]=t[i].replace("—s","in subject form")
				t[i]=t[i].replace("—int.","in interjection form")
				t[i]=t[i].replace("e.g","for example")
				t[i]=t[i].replace("pl.","in plural form")
				t[i]=t[i].replace("etc.","et cetera")
				t[i]=t[i].replace("colloq.","colloquial")
				return t[i]
		return "NIL"

	def googleSearchKw(t):
		t = t[(t.find("search")+7):len(t)]
		t = t.replace("google","",1)
		t = t.replace("for","",1)
		return t.strip()
	def googleSearch(toSearch):
			driver = webdriver.Chrome()
			driver.get("https://www.google.com/")
			sleep(2)
			searchBox = driver.find_element_by_xpath("//input[@title='Search'][@name='q']")
			searchBox.click()
			action = ActionChains(driver)
			searchBox.send_keys(toSearch)
			sleep(2)
			action.key_down(Keys.RETURN).perform()

	def whats(t):
		if ("'s" in t):
			t = t[(t.find("'s")+3):len(t)]
		elif (' is ' in t):
			t = t[(t.find("is")+3):len(t)]
		elif 'does it' in t:
			t = t[(t.find("does it")+8):len(t)]
		elif 'does' in t:
			t = t[(t.find("does")+5):len(t)]
		t = t.replace("meaning of","",1)
		t = t.replace("means","",-1)
		t = t.replace("mean","",-1)
		t = t.replace("an ","",1)
		t = t.replace("a ","",1)
		t = t.replace("your ","",1)
		t = t.replace("to be","",1)
		t = t.replace("to","",1)
		t = t.replace("the ","",1)
		t = t.replace("your ","",1)

		if 'plus' in t:
			sp = t.split('')



		return t.strip().lower()


#Mathematics
	def Mathswhats(t):

		if ("'s" in t):
			t = t[(t.find("'s")+3):len(t)]
		elif (' is ' in t):
			t = t[(t.find("is")+3):len(t)]
		elif 'does it' in t:
			t = t[(t.find("does it")+8):len(t)]
		elif 'does' in t:
			t = t[(t.find("does")+5):len(t)]
		t = t.replace("meaning of","",1)
		t = t.replace("means","",-1)
		t = t.replace("mean","",-1)
		t = t.replace("an ","",1)
		t = t.replace("a ","",1)
		t = t.replace("your ","",1)
		t = t.replace("to be","",1)
		t = t.replace("to","",1)
		t = t.replace("the ","",1)
		t = t.replace("your ","",1)

		t = t.replace('multiplied by','times')
		t = t.replace('divided by','divided')
		sp = t.split(' ')
		temp = ""
		nsp = [None]*20
		ni = 0
		for i in range(len(sp)):
			if sp[i] == 'times':
				nsp[ni] = temp.strip() + '*'
				ni+=1
				temp = ""
			elif sp[i] == 'divided':
				nsp[ni] = temp.strip()+'/'
				ni+=1
				temp = ""
			elif sp[i] == 'plus':
				nsp[ni] = temp.strip() + '+'
				ni+=1
				temp = ""
			elif sp[i] == 'minus':
				nsp[ni] = temp.strip() + '-'
				ni+=1
				temp = ""
			else:
				temp += sp[i]
				temp += " "
		nsp[ni] = temp.strip()
				
		while None in nsp:
			nsp.remove(None)
		ftext = ""
		for v in nsp:
			if '*' in v:
				v = v.replace('*','')
				ftext += str(tool.textToNum(v))
				ftext += '*'
			elif '/' in v:
				v = v.replace('/','')
				ftext += str(tool.textToNum(v))
				ftext += '/'
			elif '+' in v:
				v = v.replace('+','')
				ftext += str(tool.tool.textToNum(v))
				ftext += '+'
			elif '-' in v:
				v = v.replace('-','')
				ftext += str(tool.textToNum(v))
				ftext += '-'
		ftext += str(tool.textToNum(nsp[-1]))

		print(ftext)

		return eval(ftext)


	def dmath(t):
		s = None
		if 'divide ' in t and ' by ' in t:
			t = t[t.find('divide')+7:len(t)]
			sp = t.split(' by ')
			s = tool.textToNum(sp[0])
			for i in range(1,len(sp)):
				s/=tool.textToNum(sp[i])

		elif 'multiply ' in t and ' by ' in t:
			t = t[t.find('multiply')+9:len(t)]
			sp = t.split(' by ')
			s = 1
			for i in range(len(sp)):
				s*=tool.textToNum(sp[i])

		elif 'add ' in t and ' to ' in t:
			t = t[t.find('add')+4:len(t)]
			sp = t.split(' to ')
			s = 0
			for i in range(len(sp)):
				s+=tool.textToNum(sp[i])

		elif 'subtract ' in t and ' from ' in t:
			t = t[t.find('subtract')+9:len(t)]
			sp = t.split(' from ')
			s = tool.textToNum(sp[0])
			for i in range(1,len(sp)):
				s-=tool.textToNum(sp[-i])
			s *=-1



		return s
	def WhatSumm(t):
		t= t[t.find('sum'):len(t)]
		t = t[t.find('of')+3:len(t)]
		t = t.replace(',','')
		arr = t.split(' ')
		s = 0
		for i in arr:
			if i == 'and':
				continue
			s += tool.textToNum(i)

		return s



	def extension(text):
		if("py" in text):
			return "py"
		elif ("html" in text):
			return "html"
		elif ("css" in text):
			return "css"
		elif ("java " in text):
			return "java"
		elif ("visual" in text or "basic" in text):
			return "vbs"
		elif ("java" in text or "script"):
			return "js"
		elif ("php" in text):
			return "php"
		elif ("pla" in text or "text" in text):
			return "txt"
		else:
			return text
	def PKW_dcYou(t):
		if (t[0:6] == "do you"):
			cod ="do"		
			t = t[t.find("do you")+7:len(t)]
		elif(t[0:7] == "can you"):
			cod = "can"
			t = t[t.find("can you")+8:len(t)]
		t = t.replace(" me"," you")
		t = t.replace("a ","",1)
		t = t.replace("to ","",1)
		t = t.replace("use","",1)
		
			
		t = t.replace("usually","",1)
		r = [t.strip(),cod]
		return r

	def PR_dcYou(kw,cod):
			df1 = f"No, I {cod} not {kw}"
			df8 = f"I {cod} not {kw}"
			df2 = f"Let me remind you that I'm simply a machine, I {cod} not {kw} like humans do"
			df3 = f"I'm a machine, I don't know anything nothing about {kw}"
			df4 = f"I'm sorry, robots {cod}n't {kw}"
			df5 = f"I would have loved to, but I haven't been programmed to {kw} yet"
			df6 = f"I'm sorry, I have not been programmed to do that yet"
			df7 = f"I'm simply still a software, I dont have the body to {kw} yet"

			pr = [df1,df2,df3,df4]
			dpr = [df8,df8,df1,df1]

			replies = {

				"sleep" : pr,
				"dance" : ["Humans use their legs to dance, I don't have one", df1,"I cannot do that for now, maybe when I have legs",df7],
				"die": ["Maybe when my battery runs down", "I am neither mortal nor immortal, I'm simply a robot",df2,df2],
				"eat": pr,
				"dream":["I neither sleep, nor dream",df1,df2,df3],
				"pray": [f"No, I do not {kw}, but I believe that there is God", df2,df1,"Prayers are majorly for those who have souls, I dont have one"],
				"know":[df1,df1,df8,df8],
				"sing":[df5,df1,df8,df6],
				"swim":[df7,df1,"I dont have body to swim, besides, I am not sure I'm waterproof",df8],
				"see": ["I am yet to have an eye","Not literally, but I can hear you","My vision aren't yet activated, Maybe in my upcoming ugrades I will be able to see you","For now I can only hear you, I hope to be upgraded soon so that I will be able to hear you."],
				"hear":["Yes! When you speak louder and clearer", "I can now hear you sir", "You can speak up sir","I'm programmed to, please speak audibly and clearly"]

			}
			rl = list(replies.keys())
			for i in range(len(rl)):
				if(rl[i] == kw[0:len(rl[i])]):
					return replies[rl[i]]
			return dpr



	def setFalse():
		ost = False
		save_ST = False
		name_ST = False
		ext_ST = False	
	def lastWord(text):
		if (" " in text):
			text = text[text.rfind(" ")+1:len(text)]
			return text
		else:
			return text


	def writeFile(file, text):
		f =open("{0}.vbs".format(file),'w')
		f.write('Set wss = wscript.CreateObject("WScript.Shell")\nwss.SendKeys "{0}"'.format(text))
		f.close()

	def writeFile_forSave(file, text):
		f =open("{0}.vbs".format(file),'w')
		code = 'Set wss = wscript.CreateObject("WScript.Shell")\nwss.SendKeys "{0}"'.format(text)
		code =code + '\nwss.SendKeys "{ENTER}"'
		f.write(code)
		f.close()


	#Replies
	def reply(t1,t2=None,t3=None,t4=None):	
		engine = pyttsx3.init()
		r = random.randint(1,4)
		if(t2==None):	
			engine.say(t1)
		elif(t3==None):
			r = random.randint(1,2)	
			if r == 1:	
				engine.say(t1)
			elif r == 2:
				engine.say(t2)
		elif(t4==None):
			r = random.randint(1,3)	
			if r == 1:	
				engine.say(t1)
			elif r == 2:
				engine.say(t2)
			elif r == 3:
				engine.say(t3)
		else:
			r = random.randint(1,3)	
			if r == 1:	
				engine.say(t1)
			elif r == 2:
				engine.say(t2)
			elif r == 3:
				engine.say(t3)
			elif r==4:
				engine.say(t4)
		engine.runAndWait()



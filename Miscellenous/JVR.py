import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio
from pyfirmata import Arduino, util
import random
from datetime import date 
from datetime import datetime
import os


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

	#Arduino Connection
	board = Arduino('COM6')
	print('Communication Successful!')

	it = util.Iterator(board)
	it.start()


	servo = board.get_pin('d:9:s')
	angle = 30
	servo.write(30)

	l =0
	r =0

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

	def Up():
		tool.angle
		tool.angle = tool.angle + 10
		if tool.angle <= 0:
			tool.angle = 0
		tool.servo.write(tool.angle)
		print(tool.angle)
	def Down():
		tool.angle = tool.angle - 10
		if tool.angle <= 0:
			tool.angle = 0
		tool.servo.write(tool.angle)
		print(tool.angle)
	def Left():
		l=1
		r=0
		tool.board.digital[8].write(r)
		tool.board.digital[7].write(l)
		print("Left")
	def Right():
		r=1
		l=0
		tool.board.digital[8].write(r)
		tool.board.digital[7].write(l)
		print("Right")
	def Centre():
		tool.board.digital[8].write(0)
		tool.board.digital[7].write(0)



	def googleSearchKw(t):
		t = t[(t.find("search")+7):len(t)]
		t = t.replace("google","",1)
		t = t.replace("for","",1)
		return t.strip()
	def googleSearch(t):
			driver = webdriver.Chrome()
			driver.get("https://www.google.com/")
			time.sleep(2)
			searchBox = driver.find_element_by_xpath("//input[@title='Search'][@name='q']")
			searchBox.click()
			action = ActionChains(driver)
			searchBox.send_keys(toSearch)
			time.sleep(2)
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
		return t.strip().lower()




	val = 0


	# def doorSensor():
	# 	board = tool.board
	# 	it = util.Iterator(board)
	# 	it.start()
	# 	board.analog[0].enable_reporting()
	# 	tool.val = board.analog[0].read()
	# 	if (tool.val is not None):
	# 		tool.val = tool.val * 100
	# 		return tool.val
	# 	else:
	# 		return 0

	

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



			 
			 		
			 			
			 
	
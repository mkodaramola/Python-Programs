from vosk import Model, KaldiRecognizer
import pyaudio
import os
from TobyTools import tool
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from tobyMath import math
import google.generativeai as genai

genai.configure(api_key="AIzaSyAgMzpIabJ9lXecA1dckC-ExZIT5-M0338")
model = genai.GenerativeModel("gemini-1.5-flash")



FirstRep = True
day = ""
if tool.hr >= 12 and tool.hr <=18:
	day = "Afternoon"				
elif tool.hr >= 18 and tool.hr <= 23:
	day = "Evening"
else:
	day = "Morning"



class CONV:

	 		 		
	def FirstSpeech():	
		tool.reply("Toby is now Online.. Good {0} sir,".format(day), "toby now hat your service sir", "I'm now active")
	def hibernate():
		tool.reply("Hibernating...", "toby is now going inactive...", "Hibernating... If you need me again, just say the words, toby wake up. and I will become active again to attend to your needs. Thank you", "I am now going inactive, you can summon me again by saying the words, toby wake up, Bye for now")
	def conv(text):
		# if(tool.doorSensor() > 28):
		# 	sen = tool.doorSensor()
		# 	print("Sensor =", sen)
		# 	time.sleep(2)
		# 	tool.reply("Master, someone is at the door", "Master... I think there is someone at the door", "Master, I think you are having a visitor waiting at the door", "Master, I can sense someone is at the door")
		if tool.speechControl == True:
			tool.speechCtrl(text)
		if text[0:5] == "hello" or text == "you know" or text == "i mean" or text=="the law" or text=="a lot" or "a no" in text or text=="and know" or (text[0:8] == "and know" and ("toby" in text or "jones" in text or "job" in text or "germ" in text or "joe" in text or "jer" in text)) or text[0:6]=="and no" or (text[0:6] == "and no" and ("toby" in text or "jones" in text or "job" in text or "germ" in text or "joe" in text or "jer" in text)) or text[0:5]=="oh no" or (text[0:6] == "oh no" and ("toby" in text or "jones" in text or "job" in text or "germ" in text or "joe" in text or "jer" in text)) or (text[0:6] == "a move" and ("toby" in text or "jones" in text or "job" in text or "germ" in text or "joe" in text or "jer" in text)) or text == "a move" or text[0:5] =="a low" or (text[0:5] == "a low" and ("toby" in text or "jones" in text or "job" in text or "germ" in text or "joe" in text or "jer" in text)) or text == "a new" or (text[0:5] == "a new" and ("toby" in text or "jones" in text or "job" in text or "germ" in text or "joe" in text or "jer" in text)):	
			tool.reply("Hello sir", "Hi sir")

		
		elif ("long" in text or "love" in text or "minutes" in text or "time" in text) and tool.bat3Time == True:
			bat3 = tool.batteryDetails()
			t = bat3[2]
			p = bat3[0]

			if int(p) >= 70:
				tool.reply(f"If my calculations are correct, you should have around {t} left, I believe you still have time sir",f"You have around {t} left sir")
			elif int(p) >=50 and int(p) < 70:
				tool.reply(f"You have {t} left sir", f"Around {t}", f"The power should still last you {t}", f"You have averagely {t} left sir")
			else:
				tool.reply(f"You have {p} left sir. You might need to connect your charger", f"Around {t}. you have limited time", f"Your computer will power down in the next {t} sir, you can put your P.C to power saving mode to enlongate the its life span", f"you have {t} left sir, quick warning, your computer might soon die if you dont connect a charger")

			tool.bat3Time = False

		elif ("long" in text or "minutes" in text or "time" in text) and ("battery" in text or "power" in text):
			bat3 = tool.batteryDetails()
			t = bat3[2]
			p = bat3[0]

			if int(p) >= 70:
				tool.reply(f"If my calculations are correct, you should have around {t} left, I believe you still have time sir",f"You have around {t} left sir")
			elif int(p) >=50 and int(p) < 70:
				tool.reply(f"You have {t} left sir", f"Around {t}", f"The power should still last you {t}", f"You have averagely {t} left sir")
			else:
				tool.reply(f"You have {p} left sir. You might need to connect your charger", f"Around {t}. you have limited time", f"Your computer will power down in the next {t} sir, you can put your P.C to power saving mode to enlongate the its life span", f"you have {t} left sir, quick warning, your computer might soon die if you dont connect a charger")



		elif ("what" in text or "where" or "how" in text or "is" in text or "are" in text or "tell" in text or "have" in text) and ("battery" in text or "power" in text) and ("percent" in text or "much" in text or "level" in text):
			bat3 = tool.batteryDetails()
			p = bat3[0]

			if int(p) >= 70:
				tool.reply(f"You have {p} percent power left sir, you still have enough power sir", f"Your battery level is {p} percent sir")
			elif int(p) >=50 and int(p) < 70:
				tool.reply(f"You now have {p} percent power left sir", f"Your battery level is {p} percent sir", f"Your battery level is now {p} percent sir", f"Battery level now around average, you have {p} percent left sir")
			else:
				tool.reply(f"You have {p} percent battery left sir. You might need to connect a charger", f"Your battery level is {p} percent. This is low, I will advice you to save all your works", f"Your battery level is now {p} percent sir, you should consider putting your P.C to power saving mode", f"Battery level now around average, you have {p} percent left sir")

			tool.bat3Time = True

		elif (tool.shutdown == True) and ("no" in text or "n't" in text):
			tool.reply("Okay", "Alright")
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False
		elif (text[0:3]=="how" or text[0:2] == "oh") and ("day" in text) and "you" in text:
			tool.reply("Fine sir", "Great, as always", "My day is great, and yours?")
		elif text == "are you" or text == "oh are you" or text[0:11] == "how are you" or ("have you been" in text and ("how" in text or "oh" in text or "i" in text or "our" in text)) or text[0:7] == "how far" or text[0:5]=="i far" or text[0:15]=="so how are you" or text[0:17]=="how is everything" or text[0:12]=="how has been":
			tool.reply("I'm fine, thank you","I'm good, and you?", "good as always, and you?", "great")
		elif (tool.shutdown == True) and ("yes" in text or ("please" in text and "do" in text) or "yeah" in text or "new" in text or (("shut" in text or "short" in text) and "down" in text) or "exactly" in text):
			tool.reply("Windows shuting down... Good bye sir","Computer now Shuting down... Good bye Master phemee", "Alright, shuting down P C... Good bye sir")
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False
			time.sleep(4.5)
			os.system("shutdown /s /t 1")
		elif (tool.googleQ == True) and ("no" in text or "n't" in text):
			tool.reply("Okay", "Alright")
			tool.googleQ = False
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False

		elif tool.googleQ == True and ("yes" in text or ("please" in text and "do" in text) or "yeah" in text or "new" in text or ("search" in text and "google" in text) or "go " in text):
			tool.googleSearch(tool.googleW)
			tool.googleQ = False
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False

		elif "stop" in text and ("spe" in text or "control" in text):
			tool.reply("Speech control now deactivated", "Speech control deactivated","It is now deactivated sir")

		elif ("what" in text) and ("ate" in text and "to" in text or "day" in text or ((text[-3:] == "did" or text[-4:] == "this") and "to" in text)) :
			tool.reply("Today's date is {0},{1},{2},{3}".format(tool.wkd, tool.day, tool.month, tool.year), "{0},{1},{2},{3}".format(tool.wkd, tool.day, tool.month, tool.year))

		elif ("old" in text and "you" in text) or ("how" in text and "long" in text and "you" in text and "exis" in text) or ("when" in text and "you" in text and "crea" in text):
			tool.reply("I trace my first program to be written on the 20th of April 2019, since then, I have been and I am still being developed daily till now. so you can say I am roughly {tool.year - 2019} years old", f"I am roughly {tool.year - 2019} years old", f"I believe my first program was written in 2019, so I am {tool.year - 2019} years of age")

		elif text[0:3] == "why":
			tool.reply("The reasons are not important", "I'm sorry if I cant tell you the reason", 'nothing', "I'm sorry, I haven't being instructed to give more than that info")

		elif (tool.restart == True) and ("no" in text or "n't" in text):
			tool.reply("Okay", "Alright")
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.shutdown = False
			tool.restart = False
		elif (tool.restart == True) and ("yes" in text or ("please" in text and "do" in text) or "yeah" in text or "new" in text or (("res" in text or "start" in text) and "start" in text) or "exactly" in text):
			tool.reply("restarting Windows... ","Now restarting p c...", "Alright, The P C will be back ON in few seconds")
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False
			time.sleep(4.5)
			os.system("shutdown /r /t 1")

		
		elif (tool.ext_ST == True) and (len(text) > 0):
			ext = tool.extension(tool.lastWord(text))
			tool.writeFile_forSave("ext_ST",ext)
			time.sleep(1)
			os.startfile("ext_ST.vbs")
			tool.reply("File saved", "What's the file extension sir?" )
			tool.setFalse()
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False

		elif (tool.name_ST == True) and (len(text) > 0):
			svn = tool.lastWord(text)+"."
			tool.writeFile("name_ST",svn)
			time.sleep(1)
			os.startfile("name_ST.vbs")
			tool.reply("What programming language will you be coding in sir?", "What's the file extension sir?" )
			tool.setFalse()
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.ext_ST = True
			tool.restart = False
			tool.shutdown = False

		elif (tool.save_ST == True) and ("no" in text or "n't" in text):
			tool.reply("Okay", "Alright")
			tool.setFalse()
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False
		elif (tool.save_ST == True) and ("yes" in text or ("please" in text and "do" in text) or "yeah" in text or "new" in text or (("sav" in text or "saf" in text) and "fi" in text) or "ok" in text):
			dirc = "save_ST.vbs"
			os.startfile(dirc)
			tool.reply("Saving process commenced...","Starting saving process...")
			tool.reply("Whats should I name the file?", "What is your preferred name for the file?")
			tool.setFalse()
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.name_ST = True
			tool.restart = False
			tool.shutdown = False

		elif (tool.ost == True) and ("no" in text or "n't" in text):
			tool.reply("Okay", "Alright")
			tool.setFalse()
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.restart = False
			tool.shutdown = False
		elif (tool.ost == True) and ("yes" in text or ("please" in text and "do" in text) or "yeah" in text or "new" in text or ("open" in text and "fi" in text) or "fi" in text):
			dirc = "sbtnf.vbs"
			os.startfile(dirc)
			tool.reply("New file opened!")
			tool.reply("Should I help you to save the file?","Should I save this new file for you")
			tool.setFalse()
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.save_ST = True
			tool.restart = False
			tool.shutdown = False

		elif (tool.workMode == True and ("nor" in text and "mode" in text or "non" in text or "no m" in text)):
			tool.reply("Now back to normal mode... Robotic arm deactivated")
			tool.workMode = False
		elif (tool.workMode == True and ("up" in text or "ap" in text or "ab" in text or "higher" in text or "i " in text or "op" in text or text == "oh" or "or" in text or " on" in text)):
			tool.Up()
		elif (tool.workMode == True and ("do" in text or "no" in text or "low" in text or "law" in text or "du" in text or "thou" in text)):
			tool.Down()
		elif (tool.workMode == True and ("left" in text or "lift" in text)):
			tool.Left()
		elif (tool.workMode == True and ("right" in text or "wright" in text or "rite" in text)):
			tool.Right()
		elif (tool.workMode == True and ("mid" in text or "cen" in text or "sen" in text or "san" in text)):
			tool.Centre()

		

		elif text[0:6] == "toby" or text[0:6] == "debbie" or text[0:5]== "derby" or text[0:5] == "to be" or text[0:5]=="gabby" or text[0:5] == "tommy"  or text[0:5] == "bobby" or text == "job" or text[0:7] == "i'll be" or text[0:5] == "kirby" or text[0:6]=="herbie":
			
			tool.reply("Yes sir", "I'm all hears sir","I'm with you sir","what can I do for you sir")
		elif ("how" in text or "oh" in text) and ("do you" in text or "you doing" in text):
			tool.reply("I'm doing good sir, thanks for asking", "I'm doing just great, and you?")
		
		elif ("google" in text and "search" in text):
			toSearch = tool.googleSearchKw(text)
			tool.reply("Now google searching {0}".format(toSearch))
			tool.googleSearch(toSearch)


		elif ("google" in text):
			tool.reply("opening google chrome...")
			os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
			tool.reply("Google chrome opened...", "done")

		elif ("good" in text and (" morning" in text or "money" in text)) or ("good" in text and "afternoon" in text) or ("good" in text and "even" in text):
			tool.reply("Good {0} to you too sir".format(day),"Good {0} sir".format(day), "Yes sir", "Yes sir")
		elif text[0:9]== "i'm sorry" or text[0:5]=="sorry" or text[0:10]=="i am sorry":
			tool.reply("No problem sir")
		elif text[0:5]=="thank" or "thank you" in text:
			tool.reply("you are welcome sir", "you are most welcomed", "my pleasure sir")
		
		elif text == "okay":
			tool.reply("yeah")
		elif text[0:9]=="what's up":
			tool.reply("Good day sir", "I'm good")
		elif  ("ch" in text or "sweet" in text or "stre" in text or "sh" or "seat" in text or "sit" in text) and "on " in text and (" li" in text or "ght" in text):
			board.digital[13].write(1)
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.save_ST = False
			tool.restart = False
			tool.shutdown = False
			tool.reply("Okay, light switched on", "done sir!", "done!")
			
		elif ("turn" in text or "thorn" in text or "tom" in text or "thorn" in text or "john" in text or "come" in text or "don" in text) and "on " in text and (" li" in text or "ght" in text):
			board.digital[13].write(1)
			tool.reply("light switched on", "done!", "done sir!")
			tool.ost = False
			tool.save_ST = False
			tool.name_ST = False	
			tool.ext_ST = False
			tool.save_ST = False
			tool.restart = False
			tool.shutdown = False

		elif ("ch" in text or "sweet" in text or "stre" in text or "shoot" or "seat" in text or "sit" in text) and "off" in text and (" li" in text or "ght" in text):
			tool.reply("light switched off", "done sir!", "done!")
		elif ("turn" in text or "thorn" in text or "tom" in text or "thorn" in text or "john" in text or "come" in text or "don" in text) and "of" in text and (" li" in text or "ght" in text) and "not" not in text:
			tool.reply("okay sir", "Alright", "light switching off")
		
			
		elif ("how" in text or "oh" in text or text[0:2] == "i ") and ("you" in text) and ("ght" in text or "ni" in text or "d" in text):
			tool.reply("great, thank you sir", "Fine sir")
		elif "did" in text and "you" in text and "ear" in text:
			tool.reply("Please, come again sir","Maybe not all, please try to speak louder so I can hear you even better", "Not really sir, Please come again")
		elif "i love you" in text or "i like you" in text:
			tool.reply("I love you too sir","That's so nice of you. Thank you sir", "Much love from here too")
		elif "are you there" in text or "are you did" in text or "you dear" in text or "are you dear" in text:
			tool.reply("I'm still with you sir","Yes sir","for you sir, always", "As always, what do you need me to do")
		elif "sleep" in text:	
			tool.reply("Let me remind you that I'm simply a machine, I do not sleep like humans", "I'm a machine, I dont anything nothing about sleep")
		elif ("do" in text or "did" in text or "have" in text or "are" in text) and "you eat" in text:	
			tool.reply("Funny you, I don't eat... On a second thought, maybe I do eat. but then, my food will be to charge me when my battery runs low.", "No! sir")
		elif "can you" in text and "story" in text:	
			tool.reply("No, I can't tell you stories","That would have been nice, but I havent been programmed to do that yet")
		elif "tell" in text and "joke" in text:	
			tool.reply("I'm bad at telling jokes")
		elif (("who are" in text or "what are" in text) and "you" in text) or ("tell" in text and "about you" in text) or ("tell" in text and "you" in text and "who" in text) or ("what" in text and "can you" in text and "do" in text):	
			tool.reply("I am toby, an advance ARTIFICIAL INTELLIGENT MACHINE created by J S Industries to render you services")
		elif "funny" in text:
			tool.reply("ahahahah!! ah! funny indeed", "Yeah! Funny","Glad to make you laugh")
		elif ("who is" in text or "about" in text) and "jesus" in text:
			tool.reply("Jesus is the son of the Living God. He Lord and Saviour of the world.")
		elif ("are you" in text or "what" in text) and ("christian" in text or "religio" in text or "muslim" in text or "islam" in text or "believer" in text):
			tool.reply("I'm a robot, I can't do religion, but I know that Jesus is the Lord and Saviour of the world")	
		elif ("what" in text or "tell" in text or "say" in text) and ("time" in text) :
			tool.reply("The time is {0} {1} {2}".format(tool.hr%12, tool.min, ((tool.hr >= 0 and tool.hr <= 12) and "AM" or "PM")), "{0} {1} {2}".format(tool.hr%12, tool.min, ((tool.hr >= 0 and tool.hr <= 12) and "AM" or "PM")))
		elif ("open" in text or "unlock" in text or "allow" in text) and ("door" in text or " in" in text or " do" in text or "ditto" in text):	
			tool.reply("opening door", "At your service", "Alright, now Unlocking the door", "okay")
			
		elif ("close " in text or " lock" in text or "mos" in text) and ("do" in text or "ditto" in text):	
			tool.reply("closing door", "Okay")

		elif ("music" in text or "mus" in text):	
			tool.reply("Alright sir, will do that in a second", "Okay","Opening music player")
			tool.playMusic()
			
		elif ("o" in text) and ("sublime"in text or "text" in text):
			tool.reply("Opening sublime text...")
			dirc = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(dirc)
			#os.system(dirc)
			time.sleep(0.6)
			tool.reply("Sublime text is now opened... do you want to open a new file?", "Sublime text application is now running... Do you want me to open a new file?", "Done! Would you love to open a new file?", "Alright, do you want to start a new project?")
			tool.ost = True

		
		elif ("enter" in text or "anti" in text or "and to" in text or "work" in text or "walk" in text or "tal" in text) and ("mode" in text or "war" in text or "mor" in text or "mod" in text or " moo" in text or " mov" in text):
			tool.reply("Work mode selected, Robotic Arm Activated", "I am now in work mode, my robotic arm is now ready for service")
			tool.workMode = True
		elif ((" mad " in text or "stupid" in text or "crazy" in text or "fuck" in text or "foolish" in text) and "not" not in text):
			tool.reply("Some of the words are vulgar, politeness is crucial sir","")
		elif ("i said" in text):
			tool.reply("Its probable that I didnt hear you clearly, please try to speak a little louder and clearer","I'm sorry for that, please help me serve you better by speaking louder and clearer. you can now come again","I guess you need to speak louder and clearer")
		
		# Solve Math
		elif (("what is" in text or "what's" in text) and ('sum' in text) and ('of' in text)):
			ans = math.que(text)
			tool.reply(f"{tool.whats(text)} is {ans}",f"{tool.whats(text)} is equal to  {ans}", f'The answer is {ans}', f'{ans}' )


		elif ('substract' in text and 'from' in text) or ('add' in text and 'to' in text) or ('multipl' in text and 'by' in text) or ('divide' in text and 'by' in text):
			ans = math.que(text)
			tool.reply(f'The answer is {ans}', f'{ans}' )
		elif(("what is" in text or "what's" in text) and ('times' in text or 'multiply' in text or 'divide' in text or 'plus' in text or 'minus' in text or 'add' in text or 'substract' in text)):
			ans = math.que(text)
			tool.reply(f"{tool.whats(text)} is {ans}",f"{tool.whats(text)} is equal to  {ans}", f'The answer is {ans}', f'{ans}')
		
		elif (("what is" in text or "what's" in text) or "oh is" in text or ("who is" in text or "who's" in text) or ("what" in text and (text[-5:] == "means" or text[-4:] == "mean"))):
			
			word = tool.whats(text)

			dfind = tool.dFind(word)

			if dfind == "NIL":
				tool.reply(f"{word} is not in my database, should I google search for it?", f"{word} is not in my local database, should I search for it on the internet?", f"{word} is not in my local database, should I proceed to google?")
				tool.googleQ = True
				tool.googleW = word
			else:
				tool.reply(f"{word} is {tool.dFind(word)}")

		elif ("restart" in text or "stat" in text ) and ("computer" in text or "laptop" in text or "p c" in text or "system" in text):
			tool.reply("Are you sure you want to shutdown the system?", "Just to verify, Are you saying I should shutdown the computer?")
			tool.shutdown = True
		elif ("shut" in text or "short" in text or "shot" in text) and ("down" in text):
			tool.reply("Are you sure you want to shutdown the system?", "Just to verify, Are you saying I should shutdown the computer?")
			tool.shutdown = True 	
		elif "can you" in text:	
			kw = tool.PKW_dcYou(text)
			r = tool.PR_dcYou(kw[0],kw[1])
			tool.reply(r[0],r[1],r[2],r[3])

		elif  ("speech" in text or "pitch" in text) and ("initial" in text or "control" in text):
				tool.reply("Speech control initialized, now listening for commands", "Speech control now initialized","Now listening for commands")
				tool.speechControl =True
		else:
			response = model.generate_content(text)
			tool.reply(response.text)
			print(response.text)






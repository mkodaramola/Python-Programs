import speech_recognition as sr
				
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
	r.adjust_for_ambient_noise(source)	
	while True:	
		audio = r.listen(source)
		try:			
			text = r.recognize_google(audio)	
			print(text)
		except:
			print("No Audio")
			continue	
		

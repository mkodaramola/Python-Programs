import speech_recognition as sr

# create a recognizer object
r = sr.Recognizer()

# create a microphone object
mic = sr.Microphone()

# create a variable to control when to stop listening
stop_listening = False

# start the loop
while not stop_listening:
    # listen for speech
    print("Listening for speech...")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # try to transcribe the speech to text
    print("Transcribing speech to text...")
    try:
        text = r.recognize_google(audio)
        print(f"Text: {text}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Error transcribing speech to text:")
        print(e)

    # check if the user said "stop" to stop the loop
    if "stop" in text.lower():
        stop_listening = True

print("Exiting loop...")

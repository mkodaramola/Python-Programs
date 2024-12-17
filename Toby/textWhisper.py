import whisper
import speech_recognition as sr




# recognizer_instance.recognize_whisper(audio_data: AudioData, model: str="base", show_dict: bool=False, load_options: Dict[Any, Any]=None, language:Optional[str]=None, translate:bool=False, **transcribe_options):


# model = whisper.load_model("tiny.en")
# result = model.transcribe("aud.mp3",language='english')
# print(result["text"])



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
        text = r.recognize_whisper(audio,"tiny.en",False,None,"english",False)

        text = text.lower()
        print(f"Text: {text}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Error transcribing speech to text:")
        print(e)
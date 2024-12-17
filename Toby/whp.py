import whisper
import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Create a microphone object
mic = sr.Microphone()

# Start the loop for speech recognition
while True:
    print("Listening for speech...")
    with mic as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # Listen for audio
        audio = r.listen(source)
    
    # Load the whisper model
    model = whisper.load_model("tiny.en")

    # Load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # Decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # Print the recognized text
    print(result.text)

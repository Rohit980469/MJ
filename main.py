import speech_recognition as sr
from gpt4all import GPT4All
import pyttsx3 as pt   # pyhton text to speech

# model = GPT4All("A:\\gpt4all\\Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf", device='nvidia')   # to load a model
model = GPT4All(r"A:\gpt4all\mistral-7b-instruct-v0.1.Q4_0.gguf", device='nvidia')   # to load a model

def speak_text(n):    #    for voice
    engine = pt.init()   # initialize TTS engine
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(n)  
    engine.runAndWait()  # actually speaks the text
    engine.stop()

r = sr.Recognizer()

with model.chat_session():
    while True:
        try:
            with sr.Microphone() as source:
                print("Speak something...")
                audio = r.listen(source)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if "exit" in text:
                 break
            print("thinking...")
            response = model.generate(prompt=text, max_tokens=50)
            print(f"Response : {response}")
            speak_text(response)

        except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
        except sr.RequestError:
                print("Could not request results; check your internet connection.") 

        

import pyttsx3
import 


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate",150) 
    engine.say(text)
    engine.runAndwait()

    speak("I love India")
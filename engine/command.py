import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text): 

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #changing index changes voices but only 0 and 1 are working here
    engine.setProperty("rate",120)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening........')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing........')
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands():
    
    try:   
        query = takecommand()
        print(query)
        
        if "open"in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
            

        else:
            print("not run")
    except:
        print("error")  


    eel.ShowHood()


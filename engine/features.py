from playsound import playsound
import eel



#play music assistant
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\tejasaudio.mp3"
    playsound(music_dir)
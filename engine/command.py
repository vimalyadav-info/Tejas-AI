import datetime
from turtle import listen
import webbrowser
from plyer import notification
import pyautogui
import pyttsx3
import speech_recognition as sr
import eel
import time
import wikipidea


def speak(text): 

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #changing index changes voices but only 0 and 1 are working here
    engine.setProperty("rate",120)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
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
def allCommands(message=1):
    
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)


    try:   
   
        if "open"in query:
            from engine.features import openCommand
            openCommand(query)

        elif "hello anugat" in query:
            speak("hello sir, Welcome , How can I help you.")

        elif "anugat say time" in query:
            now_time = datetime.datetime.now().strftime("%H:%M")
            print("Current time is " + str(now_time))
            speak("Current time is " + str(now_time))

        elif "anugat say date" in query:
            now_time = datetime.datetime.now().strftime("%d:%m")
            print("Current time is " + str(now_time))
            speak("Current date is " + str(now_time))    
        
        
        elif "on youtube" in query:
                    from engine.features import PlayYoutube
                    PlayYoutube(query)

                    

        elif "windows" in query:
                    query = query.replace("windows", "").strip().lower()
                    print(f"Query: {query}")
                    speak(f"You asked to open: {query}")

                    app_name = (query)
                    if app_name:
                        try:
                            pyautogui.press("super")
                            pyautogui.typewrite(app_name)
                            time.sleep(2)
                            pyautogui.press("enter")
                            
                            result = f"Opening {app_name}"
                            print(result)
                            speak(result)
                        except pyautogui.FailSafeException as fse:
                            error_message = (
                                f"PyAutoGUI fail-safe triggered while opening {app_name}. "
                                f"Ensure the mouse wasn't moved to a corner: {str(fse)}"
                            )
                            print(error_message)
                            speak(error_message)
                        except Exception as e:
                            error_message = f"An unexpected error occurred while opening {app_name}: {str(e)}"
                            print(error_message)
                            speak(error_message)
                    else:
                        error_message = "The requested application is not allowed or recognized."
                        print(error_message)
                        speak(error_message)
            


        elif "wikipedia" in query:
            query = query.replace("search wikipedia", "").strip()
            speak(f"Searching Wikipedia for {query}")
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)

                # Ask if the user wants to open the Wikipedia page
                speak("Would you like to open the Wikipedia page for more details? Please say yes or no.")
                user_response = listen().lower()  # Replace listen() with your input handling function

                if "yes" in user_response:
                    url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
                    speak(f"Opening Wikipedia page for {query}")
                    webbrowser.open(url)
                else:
                    speak("Okay, not opening the Wikipedia page.")

            except wikipedia.exceptions.DisambiguationError:
                speak("The term is ambiguous. Please provide more specific information.")
            except wikipedia.exceptions.PageError:
                speak("No page found for the given query.")
            except Exception as e:
                speak(f"An error occurred: {str(e)}")

                    

        elif "search google" in query:
                query = query.replace("search google", "").strip()
                speak(f"Searching Google for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")


#===>>>>
#===>>>>
        elif "new task" in query:
            task = query.replace("new task", "").strip()
            if task:
                result = f"Adding task: {task}"
                print(result)  # Print the task being added
                speak(result)  # Speak the task being added
                try:
                    with open("todo.txt", "a") as file:
                        file.write(task + "\n")
                    print("Task added successfully.")  # Confirm task addition
                    speak("Task added successfully.")
                except Exception as e:
                    error_message = f"An error occurred while adding the task: {str(e)}"
                    print(error_message)
                    speak(error_message)
            else:
                error_message = "No task provided. Please specify the task to add."
                print(error_message)
                speak(error_message)

        elif "speak task" in query:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()
                if tasks:
                    result = f"Tasks we have to do today are: {tasks}"
                    print(result)  # Print all tasks
                    speak(result)  # Speak all tasks
                else:
                    result = "Your to-do list is empty."
                    print(result)  # Print empty to-do list message
                    speak(result)  # Speak empty to-do list message
            except FileNotFoundError:
                error_message = "No to-do list found. Please add tasks first."
                print(error_message)
                speak(error_message)
            except Exception as e:
                error_message = f"An error occurred while reading the tasks: {str(e)}"
                print(error_message)
                speak(error_message)

        elif "show work" in query:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read().strip()
                if tasks:
                    print("Tasks to display in notification:")  # Log the tasks
                    print(tasks)
                    notification.notify(
                        title="Today's Work",
                        message=tasks,
                        timeout=10  # Notification will stay for 10 seconds
                    )
                    speak("Displayed your tasks as a notification.")
                else:
                    result = "Your to-do list is empty. Nothing to display."
                    print(result)  # Log empty message
                    speak(result)  # Speak empty message
            except FileNotFoundError:
                error_message = "No to-do list found. Please add tasks first."
                print(error_message)
                speak(error_message)
            except Exception as e:
                error_message = f"An error occurred while showing the tasks: {str(e)}"
                print(error_message)
                speak(error_message)




            #whatsapp command

        elif "send message" in query or "phone call" in query or "video call" in query:
                    from engine.features import findContact, whatsApp
                    flag = ""
                    contact_no, name = findContact(query)
                    if(contact_no != 0):

                        if "send message" in query:
                            flag  = 'message'
                            speak("what message to send")
                            query = takecommand()
                            
                        elif "phone call" in query:
                            flag = 'call'
                        else:
                            flag  = 'video call'
                            
                        whatsApp(contact_no, query, flag, name)
        else:
            print("not run")
    except:
        print("error")  


    eel.ShowHood()


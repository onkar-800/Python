import speech_recognition as sr 
import pyttsx3
import webbrowser
import pyautogui
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def say(text):
    engine.say(text)
    engine.runAndWait()

def recognizing():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listning....")
        say("Listning...")
        try:
            audio = recognizer.listen(source, timeout=2)  
            text = recognizer.recognize_google(audio)
            return text.lower()     

        except Exception as e:
            print(e)
            say("Please say something....")
            return None


def rony():
    say("Welcome...")
    print   ("Welcome...")
    while True:
        try:
            user_input = recognizing()
            if(user_input==None):                
                continue    

            user_input = user_input.split()
            check = user_input[0].lower()
            if(check in ['exit','stop']):
                print("Exiting")
                say("Exiting")
                return

            enter = "".join(user_input[1:])           
            search = f"https://www.google.com/search?q={enter}"                        
            if(check.lower() == 'search'):
                print(f"Searching {enter}")
                say(f"Searching {enter}")
                webbrowser.open(search)
            elif(check.lower() == 'open'):
                print(f"Opening {enter}")
                say(f"Opening {enter}")
                webbrowser.open(search)
                time.sleep(4)
                pyautogui.click(280,300)
            else:
                say("I didn't catch that. Can you please repeat?")
        #    user_input.lower() for word in ['exit','stop']):
            
        except Exception as e:
            print(e)

if __name__=='__main__':
    rony()

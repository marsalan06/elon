import pyttsx3 
import datetime
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1]) #print voice id
engine.setProperty('voices',voices[1].id)

def which_func(name):
    print(".....")
    print("Executing "+ str(name)+" function")
    print(".....")

def speak(audio):
    which_func(str("speak"))
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    which_func(str("wishme"))
    if hour>=0 and hour <12:
        speak("Good Morning Arsalan, how may i asist you this morning")
    elif hour>=12 and hour <17:
        speak("Good afternoon Arsalan, how may i asist you this afternoon")
    elif hour>=17 and hour<19 :
        speak("Good evening Arsalan, how may i asist you this evening")
    else :
        speak("Hello Arsalan, How may i help you tonight")
    
    speak("My name is Elon") 


def takeCommand():
    """it takes microphone input from user and returns output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1.5
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("say that again please....")
        speak("say that again please....")
        return "None" 
    return query

if __name__=="__main__":
    speak("Hi Arsalan")
    wishme()
    while True:
        takeCommand()

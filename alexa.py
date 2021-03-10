# importing modules 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time as t
from win32com.client import Dispatch
import pyautogui as p
import psutil


engine = pyttsx3.init('sapi5')  # creating a voice obj
voices = engine.getProperty('voices')   # getting voice 
engine.setProperty('voice', voices[0].id)   # selecting voice 


def speak(audio):   
    '''this function is used to 
    speak the given string'''
    engine.say(audio)
    engine.runAndWait()


def wishMe():   # it will wish acording to time ever time when it will run
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 18:
        speak('good afternoon!')
    else:
        speak('good evening!')


def takeCommand():  
    ''' this function will take the command from the user and analyse it according to the 
    sentence spoken by the user and return it in the form of string.'''
    # the return type is only ""STRING""
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")

        # r.energy_threshold = 200
        r.phrase_threshold = 1

        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"you said {query}\n")

        except Exception as e:
            print(e)
            speak("i did not get that, can you please repeat it?")
            return 'None'
        return query


wishMe()


# nested if-else begins here
if __name__ == '__main__':
    speak("hello sir, i am your personal assistant jarvis, how may i help you?")
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('www.stackoverflow.com')

        elif 'open instagram' in query:
            webbrowser.open('www.instagram.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir the time is{strTime}")
            print(strTime)

        elif 'open vs code' in query:
            vscodepath = "C:\\Users\\Ashish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)

        elif 'open pycharm' in query:
            pycharmpath = "C:\\Program Files\\JetBrains\\PyCharm Community Editdsion 2020.2.2\\bin\\pycharm64.exe"
            os.startfile(pycharmpath)

        elif 'open discord' in query:
            webbrowser.open("www.discord.com")

        elif 'hello jarvis' in query:
            speak("hello Krishil!")


        elif 'how are you' in query:
            speak("i'm great! thanks for asking!")

        elif "join maths" in query.lower():
            if datetime.datetime.now().strftime("%H:%M"):
                webbrowser.open('https://us04web.zoom.us/j/7485853691?pwd=YzhveUtOUmhUd21uOUsvczVReGhaUT09')

            else:
                speak("no class found!")

        elif 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = str(battery.percent)

            speak('your device is running on  ' + percentage + "% battery")

        elif 'what is my name' in query:
            speak("as you have told me sir, you are KRISHIL, GHELANI!")

        elif 'i am getting bored' or 'bored' or 'i am bored' in query:
            speak("How is this possible if i'm here!, okay, so let me tell you a joke!")
            speak('which is the best rhythm for computers?')
            t.sleep(2)
            speak("it's an algo-rhythm")
        elif 'nice one' in query:
            speak("thank you!")

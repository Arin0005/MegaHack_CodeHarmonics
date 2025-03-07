import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice",voice[0].id) # 0 - david, 1 - Zira,
# print(voices[0])
engine.setProperty("rate",160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("How may I help you..?? ")


def bye():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 6:
        speak("Good Working Sir, Have a Good Night")
    elif hour >= 6 and hour < 16:
        speak("Have a Great day ahead Sir")
    elif hour >= 16 and hour <= 20:
        speak("I Wish for you to have a great Evening ahead Sir")
    else:
        speak("Good Working Sir, Have a Good Night")

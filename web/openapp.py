import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep


engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
# engine.setProperty("voice", voice[0].id)  # 0 - David, 1 - Zira
engine.setProperty("rate", 160)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


openapps = {"command prompt":"cmd",
            "word":"winword",
            "excel":"excel",
            "vscode":"code",
            "pycharm":"pycharm",
            "powerpoint":"powerpnt",
            "brave":"brave",
            "edge":"msedge"}   # Dictionary for apps

def openweb(query):  # Function to open web or apps
    speak("Processing Sir....")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("launch", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(openapps.keys())
        for app in keys:
            if app in query:
                os.system(f"start {openapps[app]}")


def closeapp(query):
    speak("Closing sir....")
    if "one tab" in query or "1 tab" in query:
        close_tabs(1)
    elif "2 tab" in query:
        close_tabs(2)
    elif "3 tab" in query:
        close_tabs(3)
    elif "4 tab" in query:
        close_tabs(4)
    elif "5 tab" in query:
        close_tabs(5)
    elif "6 tab" in query:
        close_tabs(6)
    else:
        keys = list(openapps.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {openapps[app]}.exe")  # Corrected taskkill command


def close_tabs(number_of_tabs):  # Function to close tabs
    for _ in range(number_of_tabs):
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
    speak(f"{number_of_tabs} Tab(s) removed")
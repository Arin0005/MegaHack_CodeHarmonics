import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("rate", 160)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

openapps = {
    "command prompt": "cmd",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "edge": "msedge",
    "chrome": "chrome",
    "brave": "brave",
    "vscode": "code",
    "pycharm": "pycharm",
    "intellij": "idea",
    "notepad++": "notepad++",
    "adobe reader": "Acrobat",
    "photoshop": "photoshop",
    "vlc": "vlc",
    "media player": "wmplayer",
    "spotify": "spotify",
    "zoom": "zoom",
    "teams": "teams",
    "discord": "discord",
    "whatsapp": "whatsapp",
    "telegram": "telegram",
    "outlook": "outlook",
    "file explorer": "explorer",
    "calculator": "calc",
    "paint": "mspaint",
    "onenote": "onenote",
    "onedrive": "onedrive",
    "dropbox": "dropbox",
    "google drive": "googledrivesync",
    "winrar": "winrar",
    "git bash": "git-bash",
    "vmware": "vmware",
    "virtualbox": "virtualbox",
    "blender": "blender",
    "autocad": "acad",
    "obs": "obs",
    "steam": "steam:",
    "epic games": "epicgameslauncher",
    "microsoft store": "ms-windows-store",
    "task manager": "taskmgr",
    "control panel": "control",
    "settings": "ms-settings",
    "prime": "PrimeVideo",
    "camera": "microsoft.windows.camera:",
    "photos": "microsoft.windows.photos:",
    "mail": "microsoft.windowscommunicationsapps:",
    "calendar": "microsoft.windowscommunicationsapps:",
    "alarm": "microsoft.windowsalarms:",
    "maps": "microsoft.windowsmaps:",
    "weather": "microsoft.bingweather:",
    "news": "microsoft.bingnews:",
    "groove music": "microsoft.zunemusic:",
    "movies": "microsoft.windowsphotos",
    "sticky notes": "microsoft.stickynotes",
    "voice recorder": "microsoft.windowsvoice Recorder",
}

def openweb(query):
    speak("Processing Sir....")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
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
                os.system(f"taskkill /f /im {openapps[app]}.exe")

def close_tabs(number_of_tabs):
    try:
        pyautogui.hotkey("alt", "tab")
        sleep(1)
    except Exception as e:
        speak("Unable to bring the browser into focus. Please ensure a browser window is open.")
        return

    for _ in range(number_of_tabs):
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
    speak(f"{number_of_tabs} Tab(s) removed")


def ott(query):
    if True:
        speak("Opening your entertainment platform...")
        query = query.split()
        if len(query) > 2:
            ott = ""
            for x in range(1, len(query)):
                ott = ott + query[x]
        else:
            ott = query[-1]
        webbrowser.open(f"https://www.{ott}.com/in/")
    else:
        speak("I couldn't identify which streaming platform you wanted. Please specify Netflix, Prime Video, Disney+, or another service.")
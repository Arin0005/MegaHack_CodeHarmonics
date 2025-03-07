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
    "steam": "steam",
    "epic games": "epicgameslauncher",
    "microsoft store": "ms-windows-store",
    "task manager": "taskmgr",
    "control panel": "control",
    "settings": "ms-settings",
    "prime":"PrimeVideo"
}  # Dictionary for apps

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

    # ott_platforms = {
    #     "netflix": "https://www.netflix.com",
    #     "prime video": "https://www.primevideo.com",
    #     "prime": "https://www.primevideo.com",
    #     "amazon prime": "https://www.primevideo.com",
    #     "disney plus": "https://www.disneyplus.com",
    #     "disney+": "https://www.disneyplus.com",
    #     "hotstar": "https://www.hotstar.com",
    #     "disney hotstar": "https://www.hotstar.com",
    #     "hulu": "https://www.hulu.com",
    #     "hbo max": "https://www.max.com",
    #     "max": "https://www.max.com",
    #     "apple tv": "https://tv.apple.com",
    #     "apple tv plus": "https://tv.apple.com",
    #     "apple tv+": "https://tv.apple.com",
    #     "youtube": "https://www.youtube.com",
    #     "youtube premium": "https://www.youtube.com/premium",
    #     "paramount plus": "https://www.paramountplus.com",
    #     "paramount+": "https://www.paramountplus.com",
    #     "peacock": "https://www.peacocktv.com",
    #     "discovery plus": "https://www.discoveryplus.com",
    #     "discovery+": "https://www.discoveryplus.com",
    #     "crunchyroll": "https://www.crunchyroll.com",
    #     "funimation": "https://www.funimation.com",
    #     "sony liv": "https://www.sonyliv.com",
    #     "zee5": "https://www.zee5.com",
    #     "voot": "https://www.voot.com",
    #     "jiocinema": "https://www.jiocinema.com",
    #     "mubi": "https://mubi.com",
    #     "tubi": "https://tubitv.com",
    #     "pluto tv": "https://pluto.tv"
    # }  # Dictionary of OTT platforms and their URLs

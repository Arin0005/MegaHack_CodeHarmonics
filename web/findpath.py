import webbrowser
import pyttsx3

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def mapPath(query):

    words = query.split()
    from_index = words.index("from")
    to_index = words.index("to")
    origin = words[from_index + 1]
    destination = words[to_index + 1]
    url = f"https://www.google.com/maps/dir/{origin}/{destination}/"
    speak("Opening Google Maps...")
    webbrowser.open(url)


import webbrowser

import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia



# Initialize the pyttsx3 engine
engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)  # 0 - David, 1 - Zira
engine.setProperty("rate", 160)  # Set speech rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak....")
        r.pause_threshold = 1
        r.energy_threshold = 275  # Sensitivity to ambient noise
        audio = r.listen(source, 0, 5)
        try:
            print("Hearing...")
            query = r.recognize_google(audio, language='en-in')  # Google speech recognition
            print(f"You Said: {query}\n")
            return query
        except:
            print("Speak Again !!")
            return "None"
        # return query


query = takecommand().lower()


def Google(query):
    if "google" in query:
        import wikipedia as gs
        query = query.replace("google","")
        query = query.replace("google search", "")
        speak("This is what i found on google:")
        try:
            pywhatkit.search(query)
            result = gs.summary(query,2)
            speak(result)
            print("Done")
        except:
            speak("No Output availablbe, try again")


def Youtube(query):
    if "youtube" in query:
        query = query.replace("youtube", "")
        query = query.replace("youtube search", "")
        speak("This is what i found on youtube:")
        web = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(web)
        # pywhatkit.playonyt(query)
        speak("Done, Sir")


def play(query):
    if "play" in query:
        query = query.replace("play", "")
        query = query.replace("youtube search", "")
        speak("This is what i found on youtube:")
        web = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")


def wiki_pedia(query):
    if "wikipedia" in query:
        query = query.replace("wikipedia","")
        query = query.replace("wikipedia search", "")
        speak("This is what i found on wikipedia:")
        result = wikipedia.summary(query,sentences=3)
        print(result)
        speak("According to Wikipedia :"+result)


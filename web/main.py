import pyttsx3
import speech_recognition as sr
from greetings import greet, bye
from findpath import mapPath
from openapp import openweb, closeapp, ott
from search import Google, play_on_spotify, play, wiki_pedia, Youtube
from events import event



class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("rate", 160)  # Set speech rate

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def take_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Hearing...")
                query = recognizer.recognize_google(audio, language='en-in')
                print(f"You Said: {query}\n")
                return query.lower()
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.\n")
                return None
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                return None

    def handle_command(self, query):
        if "bye" in query:
            self.speak("Okay, You can call me again as you wish Sir")
            bye()
            return False

        elif "hello" in query:
            self.speak("Hello Sir, How can I help you?")

        elif "how are you" in query:
            self.speak("I'm fine. How are you, Sir?")

        elif "thank you" in query:
            self.speak("You're welcome, Sir. I'm grateful to be of help.")

        elif "open" in query:
            openweb(query)

        elif "close" in query:
            closeapp(query)

        elif "google" in query:
            Google(query)

        elif "youtube" in query:
            Youtube(query)

        elif "wikipedia" in query:
            wiki_pedia(query)

        elif "stream" in query or "show" in query or "ott" in query:
            ott(query)

        elif "play" in query:
            play(query)

        elif "spotify" in query:
            play_on_spotify(query)

        elif "find route" in query:
            mapPath(query)

        elif "schedule" in query:
            event(query)
        return True

    def run(self):
        while True:
            query = self.take_command()
            if query and "ultron" in query:
                self.speak("How Can I Help you sir!!")
                while True:
                    query = self.take_command()
                    if query and not self.handle_command(query):
                        break
            elif query and "shutdown" in query:
                self.speak("Shutting down completely..")
                break

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
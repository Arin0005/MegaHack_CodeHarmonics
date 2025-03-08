import pyttsx3
import speech_recognition as sr
from greetings import greet, bye
from findpath import mapPath
from openapp import openweb, closeapp, ott
from search import Google, play_on_spotify, play, wiki_pedia, Youtube
from events import event
from performance_metrics import system_metrics  # Import the system_metrics function

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

    def ask_confirmation(self, prompt):
        self.speak(prompt)
        response = self.take_command()
        if response and "yes" in response:
            return True
        elif response and "no" in response:
            return False
        else:
            self.speak("I didn't understand your response. Please say 'yes' or 'no'.")
            return self.ask_confirmation(prompt)  # Retry


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
            app_name = query.replace("close", "").strip()
            if app_name:
                if self.ask_confirmation(f"Are you sure you want to close {app_name}?"):
                    closeapp(app_name)
                    self.speak(f"{app_name} has been closed.")
                else:
                    self.speak("Okay, I will not close it.")
            else:
                self.speak("Please specify the application to close.")

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

        elif "schedule meeting" in query or "create event" in query:
            event(query)

        elif "system performance" in query or "system metrics" in query:
            metrics = system_metrics()
            self.speak(f"CPU Usage is {metrics['cpu_usage']} percent.")
            self.speak(f"Memory Usage is {metrics['memory_percent']} percent.")
            # self.speak(f"Disk Usage is {metrics['disk_percent']} percent.")
            # self.speak(f"Network: Sent {metrics['bytes_sent']} MB, Received {metrics['bytes_recv']} MB.")
            # self.speak(f"System Boot Time: {metrics['boot_time']}.")
            if metrics['battery_percent'] != "N/A":
                self.speak(f"Battery is at {metrics['battery_percent']} percent.")
                if metrics['is_plugged']:
                    self.speak("The system is currently plugged in.")
                else:
                    self.speak(f"Estimated time left: {metrics['battery_time_left']} seconds.")
            else:
                self.speak("Battery information is not available.")

                # Provide feedback and suggest actions
                if metrics['cpu_usage'] > 80:
                    self.speak("Your CPU usage is very high. You Should close some background applications.")


        elif "shutdown" in query:
            if self.ask_confirmation("Are you sure you want to shut down the system?"):
                self.speak("Shutting down completely..")
                return False
            else:
                self.speak("Shutdown canceled.")
        return True

    def run(self):
        while True:
            query = self.take_command()
            if query and "ultron" in query:
                self.speak("How Can I Help you sir!!")
                while True:
                    query = self.take_command()
                    if query is None:
                        continue
                    if "quit" in query:
                        break
                    if not self.handle_command(query):
                        return  # Exit the run method, effectively shutting down the assistant
            elif query and "shutdown" in query:
                self.speak("Shutting down completely..")
                break

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
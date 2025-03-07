import pyaudio
import pyttsx3
import speech_recognition as sr
# from openapp import openweb as ow

# Initialize the pyttsx3 engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

# # Set default voice to David
# engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 160)  # Set speech rate


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def change_voice():
#     # Define voice names
#     voice_names = {0: "David", 1: "Zira", 2: "Mark"}
#
#     # Get current voice index
#     current_voice_id = engine.getProperty("voice")
#     current_voice_index = next((i for i, voice in enumerate(voices) if voice.id == current_voice_id), None)
#
#     # Cycle through the voices
#     next_voice_index = (current_voice_index + 1) % len(voices)
#     engine.setProperty("voice", voices[next_voice_index].id)
#     speak(f"Voice changed to {voice_names[next_voice_index]}")
#

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak....")
        r.pause_threshold = 1
        r.energy_threshold = 275  # Sensitivity to ambient noise

        audio = r.listen(source, 0, 3)  # Stops listening after 3 seconds

        try:
            print("Hearing...")
            query = r.recognize_google(audio, language='en-in')  # Google speech recognition
            print(f"You Said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.\n")
            return "None"
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return "None"
        return query



if __name__ == "__main__":
    i = 1
    while i:
        query = takecommand().lower()
        if "wake up" in query:
            from greetings import greet

            greet()

            while True:
                query = takecommand().lower()
                if "go to sleep" in query:  # Goes to sleep but doesn't shut down
                    speak("Okay, You can call me again as you wish Sir")
                    from greetings import bye
                    bye()
                    break

                # elif "change voice" in query:
                #     change_voice()

                elif "hello" in query:
                    speak("Hello Sir, How can I help you?")

                elif "how are you" in query:
                    speak("I'm fine. How are you, Sir?")

                elif "thank you" in query:
                    speak("You're welcome, Sir. I'm grateful to be of help.")

                elif "open" in query:
                    from openapp import openweb
                    openweb(query)

                elif "close" in query:
                    from openapp import closeapp
                    closeapp(query)

                elif "google" in query:
                    from search import Google
                    Google(query)

                elif "youtube" in query:
                    from search import Youtube
                    Youtube(query)

                elif "play" in query:
                    from search import play
                    play(query)

                elif "wikipedia" in query:
                    from search import wiki_pedia
                    wiki_pedia(query)

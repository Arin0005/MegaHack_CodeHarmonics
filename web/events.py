import speech_recognition as sr
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import datetime
import re

# Google Calendar API settings
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Update with your service account file

def authenticate_google_calendar():
    """Authenticate with Google Calendar using service account credentials."""
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def recognize_speech():
    """Capture speech input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand the speech.")
    except sr.RequestError:
        print("Error with the speech recognition service.")
    return None

def extract_event_details(text):
    """Extract event date and time from the input text using regex."""
    # Regex patterns for date and time
    date_patterns = [
        r"(\d{1,2} (january|february|march|april|may|june|july|august|september|october|november|december) \d{4})",  # 25 August 2025
        r"(\d{4}-\d{2}-\d{2})",  # 2025-08-25
        r"(\d{1,2}/\d{1,2}/\d{4})",  # 25/08/2025
    ]
    time_patterns = [
        r"(\d{1,2}:\d{2} (am|pm))",  # 5:00 pm
        r"(\d{1,2} (am|pm))",  # 5 pm
        r"(\d{2}:\d{2})",  # 17:00
    ]

    # Extract date
    event_date = None
    for pattern in date_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                event_date = datetime.datetime.strptime(match.group(0), "%d %B %Y" if " " in match.group(0) else "%Y-%m-%d" if "-" in match.group(0) else "%d/%m/%Y").strftime('%Y-%m-%d')
                break
            except ValueError:
                continue
    if not event_date:
        event_date = datetime.date.today().strftime('%Y-%m-%d')  # Default to today

    # Extract time
    event_time = None
    for pattern in time_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                if "am" in match.group(0).lower() or "pm" in match.group(0).lower():
                    event_time = datetime.datetime.strptime(match.group(0), "%I:%M %p" if ":" in match.group(0) else "%I %p").strftime('%H:%M')
                else:
                    event_time = match.group(0)  # Assume 24-hour format
                break
            except ValueError:
                continue
    if not event_time:
        event_time = "10:00"  # Default to 10:00 AM

    return event_date, event_time

def create_calendar_event(event_summary, event_date, event_time):
    """Create an event in Google Calendar."""
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)
    start_time = f"{event_date}T{event_time}:00"
    end_time = f"{event_date}T{(int(event_time.split(':')[0]) + 1):02d}:{event_time.split(':')[1]}:00"
    event = {
        'summary': event_summary,
        'start': {'dateTime': start_time, 'timeZone': 'America/New_York'},
        'end': {'dateTime': end_time, 'timeZone': 'America/New_York'},
    }
    try:
        event_result = service.events().insert(calendarId='arinthamke@gmail.com', body=event).execute()
        print(f"Event created: {event_result.get('htmlLink')}")
    except Exception as e:
        print(f"Error creating event: {e}")

def main():
    """Main function to handle speech input and event creation."""
    print("Say something like: 'Schedule a meeting on 25 August 2025 at 5 pm'")
    text = recognize_speech()
    if text:
        event_date, event_time = extract_event_details(text)
        if event_date and event_time:
            print(f"Extracted Date: {event_date}, Time: {event_time}")
            print(f"Do you want to create an event on {event_date} at {event_time}? (yes/no): ")
            confirmation = input("yes/no: ")
            if confirmation and "yes" in confirmation.lower():
                create_calendar_event("Meeting", event_date, event_time)
            else:
                print("Event creation canceled.")
        else:
            print("Failed to extract event details. Please try again.")

if __name__ == "__main__":
    main()
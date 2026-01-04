import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I did not catch that. Please say again.")
        return None
    return query.lower()
if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = take_command()
        if command:
            if "hello" in command:
                speak("Hello.. How are you?")
            elif "time" in command:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif "date" in command:
                today = datetime.datetime.now().strftime("%B %d, %Y")
                speak(f"Today's date is {today}")
            elif "open google" in command:
                webbrowser.open("https://www.google.com")
                speak("Opening Google")
            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube")
            elif "exit" in command or "quit" in command:
                speak("Goodbye")
                break
            else:
                speak("I can only perform basic commands right now.")
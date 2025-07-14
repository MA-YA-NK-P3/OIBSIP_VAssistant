import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speaking rate

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {date}")
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I can’t do that yet, but I’m learning!")

# Main loop
speak("Voice assistant started. Say something!")
while True:
    command = listen()
    respond_to_command(command)

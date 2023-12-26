import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser   
import os
import random

# it will allow take the voice of AI from the Microsoft Window
engine = pyttsx3.init('sapi5')
# the class is basically used to display the available voices in the devices
voices = engine.getProperty('voices')
# print(voices)
# this class will set the desired voice as the programmer want
engine.setProperty('voice', voices[0].id)


def speak(audio):  # This function is basically used for fetching the voice in the result
    engine.say(audio)
    engine.runAndWait()


def wishme():  # this function will wish the user according to the given condition
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        print(" Good Morning!\n")
        speak("Good Morning!")
        # speak("how can i help u today")
 
    elif hour >= 12 and hour <= 18:
        print(" Good Afternoon!\n")
        speak("Good Afternoon1")
        # speak("how can i help u today")
 
    else:
        print(" Good Evening!\n")
        speak("Good Evening!")
        # speak("how can i help u today")

    a = " I am Alex!!\n\n Your personal PC assistant\n\n PLEASE! Tell me how can I help you!!"
    print(a)
    speak(a)


# it takes microphonic input from the user and returns the result in print() form string form.
def takecommand():
    r = sr.Recognizer()  # it will recognize the voice  
    with sr.Microphone() as source:
        print(" I am listening...")
        # r.pause_threshold() = 1
        # the audio will be taken from the source i.e. a user's voice
        audio = r.listen(source)    

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry, can you please say it again...")
        return "None"
    return query  # it will again ask for query


if __name__ == "__main__":
    wishme()
    query = takecommand().lower()

    # Here, all the conditions are mentioned for query
    if 'what is' in query:
        speak("Searching for the best results...")
        query = query.replace("wikipedia" "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to research")
        print(results)
        speak(results)

    elif 'google' in query:
        webbrowser.open("google.com")
        # print(" opening google for you...")

    elif 'youtube' in query:
        webbrowser.open("youtube.com")
    # print(" opening google for you...")

    elif 'facebook' in query:
        webbrowser.open("facebook.com")
    # print(" opening google for you...")

    elif 'instagram' in query:
        webbrowser.open("instagram.com")
    # print(" opening google for you...")
 
    elif 'mail' in query:
        webbrowser.open("gmail.com")
    # print(" opening google for you...")

    elif ' college ' in query:
        webbrowser.open("https://saitm.ac.in")
    # print(" opening google for you...")

    elif 'time' in query:
        time1 = datetime.datetime.now()
        print(time1)
        speak(f"the current time is {time1}")

    elif 'code' in query:
        path = "C:\\Users\\Divyam Agarwal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
        # print(" opening google for you...")

    elif 'playlist' in query:
        webbrowser.open(
        "https://music.amazon.in/my/playlists/62e22608-3d49-4157-8273-b194a8d9ef1c")
        print("opening ur playlist")

    elif 'random' in query:                 
        path = "C:\\Users\\Divyam Agarwal\\Desktop\\chatbot"
        files = os.listdir(path)
        d = random.choice(files)
        os.startfile(d)

    
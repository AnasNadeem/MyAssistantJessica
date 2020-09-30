import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good morning Anas!')
    elif hour>=12 and hour<18:
        speak('Good afternoon Anas!')
    else:
        speak('Good night Anas')
    speak('This is Jessica. How may i help you?')

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 400
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print('Say that again please...')
        return "None"
    return query    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing task with query
        if "wikipedia" in query:
            speak('Searching query')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open('youtube.com')
            speak('Sure Anas')

        elif "open google" in query:
            webbrowser.open('google.com')
            speak('Sure Anas')

        elif "open my channel" in query:
            webbrowser.open('youtube.com/c/whoareyouanas')
            speak('Sure Anas Sir')

        elif "play music" or "play song" in query:
            music_path = 'E:\\Music'
            songs = os.listdir(music_path)
            for son in songs:
                mp3On = son.split('.')
                if mp3On[1] == 'mp3':          
                    ran_song = random.choice(son)
                    os.startfile(os.path.join(music_path, ran_song))

        
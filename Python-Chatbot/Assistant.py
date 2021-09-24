import datetime
import os
import random
import cv2
import pyttsx3
import speech_recognition as sr
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=6, phrase_time_limit=5)
    try:
        print("Recognizing...")
        Query = r.recognize_google(audio, language='en-in')
        print(f"user said : {Query}")
    except exception as e :
        speak("Say that again please...")
        return "none"
    return Query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning...")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon...")
    else:
        speak("Good Evening...")

def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.echo()
    server.starttls()
    server.login("your email id", to, content)
    server.close()


if __name__ == "__main__":
    speak("I am Jarvis sir, please tell me how can I help you")
    while True:
        query = takeCommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("Start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "#"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').toct
            speak(f'your ip address is {ip}')

        elif "wikipedia" in query:
            speak("searching wikipedia... ")
            query = query.replace("wikipedia", " ")
            results = wikipedia.Summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open google" in query:
            speak("what should I search in google")
            cm = takeCommand().lower()
            webbrowser.open(f'{cm}')

        elif "send message" in query:
            kit.sendwhatmsg("+911234567890", "This is for testing purpose", 2, 24)

        elif "play songs in youtube" in query:
            kit.playonyt("see you again")

        elif "email to " in query:
            try:
                speak("what should I say")
                content = takeCommand().lower()
                to = "example@gmail.com"
                SendEmail(to, content)
                speak("email has been sent")
            except exception as e:
                print(e)
                speak("sorry, I am unable to send this mail")

        elif "no thanks" in query:
            speak("thanks for using me, have a good day")
            sys.exit()

        speak("Do you have any other work")






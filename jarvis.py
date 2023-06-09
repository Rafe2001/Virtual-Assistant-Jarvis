from email.mime import audio
import speech_recognition as sr
import pyttsx3
import py
import wikipedia
import webbrowser
import datetime
import smtplib
import os
import subprocess
import requests
import json
import wolframalpha
import time
from bs4 import BeautifulSoup
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    
    try:
            print("Recognizing")
            statement = r.recognize_google(audio, language='en-in')
            print("the command is printed=", statement)
             
    except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
         
    return statement


def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
        print("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon")
    else:
        speak("Good Evening!")
        print("Good Evening")


print("Loading your personal assistant Jarvis A.I")
wishMe()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if day in Day_dict.keys():
        day_week = Day_dict[day]
        print(day_week)
        speak(f"The day is {day_week}")
        

def tellNews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=044e73a386d4459d930a1d2daaab5342",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=044e73a386d4459d930a1d2daaab5342",    
               "general":"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=044e73a386d4459d930a1d2daaab5342",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=044e73a386d4459d930a1d2daaab5342",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=044e73a386d4459d930a1d2daaab5342",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=044e73a386d4459d930a1d2daaab5342",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=044e73a386d4459d930a1d2daaab5342"
               }               
    
    content = None
    url = None
    speak("Which field news do you want,{business},{health},{sports},{technology},{enternainment}")
    
    field = input('Type the news that you want to hear:\n')
    for key, value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
            
    if url is True:
        print("url was not found")
            
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is a first news sir")
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]  
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more news visit{news_url}")
        
        a = input("Press 1 to continue and 2 to stop")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("Thats it sir")
    
    
def Temp():
    speak("What is the temperature")
    temp = takeCommand()
    temp = temp.lower()
    temp = temp.replace("what is the temperature","")
    

def TakeQuery():
    while (True):
        speak("This is your personal assistant jarvis")
        speak("Tell me how can I help you")
        statement = takeCommand().lower()
        if "tell your name" in statement:
            speak("My name is Jarvis")
            continue

        elif "goodbye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal assistant Jarvis is shutting down")
            print("Goodbye")
            break
        
        elif "How are you" in statement:
            speak("I am fine sir")
            continue
        
        elif "news" in statement:
            speak("Yes sir")
            tellNews()
            continue
    
        elif "from wikipedia" in statement:
           speak("Searching for wikipedia")
           statement = statement.replace("wikipedia", "")
           result = wikipedia.summary(statement, statement=4)
           speak("According to wikipedia")
           print(result)
           speak(result)
           continue
               
        elif "open google" in statement:
           webbrowser.open("https://www.google.com")
           speak("google crome is open now")
           time.sleep(1)
           continue        
        
        elif "open youtube" in statement:
           webbrowser.open("https://www.youtube.com")
           speak("youtube is open now")
           time.sleep(1)
           continue
       
        elif "open Linkedin" in statement:
            speak("Opening Linkedin Sir")
            webbrowser.open("https://www.linkedin.com")
            continue
        
        elif "open Facebook" in statement:
            speak("Opening Facebook sir")
            webbrowser.open("https://www.facebook.com")
            continue
        
        
        
        elif "which day is today" in statement:
            tellDay()
            continue
        
        elif "open gmail" in statement:
            speak("Opening gmail")
            webbrowser.open_new_tab("https://www.gmail.com")
            continue
        
        elif "the time" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir the time is {strTime}")
            continue
        
        elif "temperature" in statement:
            search = "Temperature in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text 
            speak(f"Current {search} is: {temp}")
            print(f"current {search} is: {temp}")
            continue  
        
        elif "weather" in statement:
            search = "Weather in mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            wheat = data.find("div", class_ = "BNeawe").text 
            speak(f"Current {search} is: {wheat}")
            print(f"current {search} is {wheat}")
            continue         
        
        else:
            speak("Application not available sir")
            
            
            
if __name__ == '__main__':
    TakeQuery()
       
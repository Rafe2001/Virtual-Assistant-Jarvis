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
import random
import pywhatkit as kit
from bs4 import BeautifulSoup
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    
    try:
            print("Recognizing...")
            statement = r.recognize_google(audio, language='en-in')
            print("the command is printed=", statement)
             
    except Exception as e:
            print(e)
            speak("Say that again sir")
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


print("Loading your personal assistant Jarvis")
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
        
def searchGoogle(say):
    kit.search(say)
    
def playYoutube(video):
    kit.playonyt(video)

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

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}",message)
    
def crack_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/",headers=headers).json()
    return res['joke']

def give_advice():
    url = "https://api.adviceslip.com/advice"
    res = requests.get(url).json()
    return res['slip']['advice']
    
 
def game_play():
    speak("Lets Playyy Rock, Paper, Scissors")
    print("Lets start playing")
    i = 0
    me_score = 0
    com_score = 0
    
    while(i<5):
        choose = ("Rock","Paper","Scissor")  
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if(query == "Rock"):
            if(com_choose == "Paper"):
                speak("paper")
                com_score+=1
                print(f"score:- me:-{me_score}, com:- {com_score}")
            
            elif(com_choose == "Rock"): 
                speak("rock") 
                print(f"Score:- me:-{me_score}, com:- {com_score}")
            
            else:
                speak("scissor")
                me_score+=1
                print(f"Score:- me:-{me_score}, com:- {com_choose}")
        
        elif(query == "Paper" or query == "taper"):
            if(com_choose == "Paper"):
                speak("paper")
                print(f"score:- me:-{me_score}, com:- {com_score}")
            
            elif(com_choose == "Rock"): 
                speak("rock") 
                me_score+=1
                print(f"Score:- me:-{me_score}, com:- {com_score}")
            
            else:
                speak("scissor")
                com_score+=1
                print(f"Score:- me:-{me_score}, com:- {com_choose}")
                        
        elif(query == "scissor" or query == "cissor"):
            if(com_choose == "Paper"):
                speak("paper")
                me_score+=1
                print(f"score:- me:-{me_score}, com:- {com_score}")
            
            elif(com_choose == "Rock"): 
                speak("rock") 
                com_score+=1
                print(f"score:- me:-{me_score}, com:- {com_score}")
            
            else:
                speak("scissor")
                print(f"score:- me:-{me_score}, com:- {com_choose}")                                                
        i+=1
    
    print(f"Final Score :- Me:-{me_score}, com:- {com_score}")  
     
    if(me_score>com_score):
        speak("you are the winner sir")
        print("You are winner of the game")        
    else:
        speak("you loosed the game sir hahahaha")
        print("You lose the game")
                      
            
def Temp():
    speak("What is the temperature")
    temp = takeCommand()
    temp = temp.lower()
    temp = temp.replace("what is the temperature","")
    

def TakeQuery():
    while (True):
        speak("This is your personal assistant jarvis A.I")
        speak("Tell me how can I help you")
        statement = takeCommand().lower()
        
        if "tell your name" in statement:
            speak("My name is Jarvis")
            continue

        elif "goodbye" in statement or "ok bye" in statement or "stop" in statement or "bye" in statement:
            speak("Your personal assistant Jarvis is shutting down")
            print("Goodbye")
            break
        
        elif "how are you" in statement:
            speak("I am fine sir")
            speak("Tell me about you")        
            continue
        
        elif "news" in statement:
            speak("Yes sir")
            tellNews()
            continue
        
        elif "wikipedia" in statement:
            speak("Searching Wikipedia Sir")
            statement = statement.replace("wikipedia","")
            results = wikipedia.summary(statement,sentences=3)
            speak(f"Accoring to the wikipedia{results}")
            print(results)
            continue   
        elif "advice" in statement:
            speak(f"Hope you will like the advice sir")
            advice = give_advice()
            speak(advice)
            print(advice)
            continue
        
        elif "send whatsapp message" in statement:
            speak("on what number should i send the message sir? please enter in the console")
            number = input("Please enter the message")
            speak("What is the message you want to send")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            continue
            
        elif "open google" in statement:
           webbrowser.open("https://www.google.com")
           speak("google crome is open now")    
           time.sleep(1)
           continue 
        elif "open discord" in statement:
           webbrowser.open("https://discord.com")
           speak("discord is open now")
           time.sleep(1)
           continue       
        
        elif "open youtube" in statement:
           webbrowser.open("https://www.youtube.com")
           speak("youtube is open now")
           time.sleep(1)
           continue

        elif "search on google" in statement:
            speak("What should i search on google? sir")             
            say = takeCommand().lower()
            searchGoogle(say) 
            continue 
        
        elif "open facebook" in statement:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook sir")
            time.sleep(1)
            continue
        
        elif "joke" in statement:
            speak(f"Hope you will like this one sir")
            joke = crack_joke()
            speak(joke)
            speak("for your convineance i'm writing on screen sir")
            print(joke)
            continue
        
        elif "play video on youtube" in statement:
            speak("what should i search on youtube sir")
            query = takeCommand().lower()
            playYoutube(query)
            continue
        
        elif "shutdown" in statement:
            speak("Do ou really want to shutdown?")
            shutdown = input("Do you really want to shut down ? (yes/no): ")
            if shutdown == "yes":
                speak("Shutting down the pc sir")
                os.system("shutdown /s /t 1")
                
            elif shutdown == "no":
                break
        
        
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
        
        elif "play a game" in statement:
            game_play()
            continue
        
        else:
            speak("Application not available sir")
            
            
            
if __name__ == '__main__':
    TakeQuery()
       

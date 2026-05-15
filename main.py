import speech_recognition as sr
import webbrowser 
import pyttsx3
import music_library
import os
import openai
from gtts import gTTS
import pygame
import time 

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "1d219bc4037a444e8ea6ca02cea31e52"
pygame.mixer.init()

def speak_old(text) :
    engine.say(text)
    engine.runAndWait()

def speak(text):

    tts = gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.music.unload()

    os.remove("temp.mp3")
     
def aiProcess(command): 
    openai.api_key = ""
     
    response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[
        {"role": "system", "content": "You are a helpful assistant name pragya  skilled in general tasks like alexa and google cloud.Give short responses please."},
        {"role": "user", "content":command}
       ]
    )
    return (response['choices'][0]['message']['content'])

def processCommand(c):
   
   c = c.lower()

   if  "open Google" in c.lower():
        webbrowser.open("https://google.com")

   elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

   elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

   elif "open fackbook" in c.lower():
        webbrowser.open("https://facebook.com") 

   elif "open chrome" in c.lower():
        webbrowser.open("https://chrome.com")

   elif c.lower().startswith("play"):

        song = c.lower().replace("play", "").strip()

        print("the song", song)

        found = False

        for key in music_library.music:

            if song in key:
                link = music_library.music[key]
                webbrowser.open(link)
                speak(f"Playing {key}")
                found = True
                break

        if not found:
            print("Available songs:", music_library.music.keys())
            speak("Song not found in music library")

   else :
       
    # Let openAI handle the request 
       output =  aiProcess(c)
       speak(output)

if  __name__ == "__main__":
   speak("Hello Pragya...... ")
   while True:
    r = sr.Recognizer()

# Listen for the wake word google
# Obtain audio from the microphone

    try:
        with sr.Microphone() as source:
          
          print("I'm listening")
          audio = r.listen(source,timeout=5,phrase_time_limit=5)

        word = r.recognize_google(audio)
        if word.lower() == ("Pragya"):
          speak("YES")

        # LISTEN FOR COMMAND 

        with sr.Microphone() as source:
          print("Virtual Assistant active.....")

          audio = r.listen(source, timeout=5, phrase_time_limit=5)

          command = r.recognize_google(audio)

        print("Full command:", command)

        processCommand(command)
      
    except Exception as e:
        print("Error; {0}".format(e))

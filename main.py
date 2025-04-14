import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)

engine.runAndWait()

def speak(string = "", num = 1, ratee = 150):
    for i in range(num):
        engine.setProperty('rate',ratee)
        engine.say(string)
        engine.runAndWait()
    
speak("Nigga",10, 2000)
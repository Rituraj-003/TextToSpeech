import pyttsx3

class TextToSpeech:
    def __init__(self):
    
        self.speaker = pyttsx3.init()
        self.speakTimes = 0
        self.volumeTimes = 0
        
    def speak(self,string):
        
        self.speaker.say(string)
        self.speaker.runAndWait()
        self.speakTimes += 1
        
    def set_speed(self,speed):
        
        self.speaker.setProperty('rate',speed)
        
        
    def set_volume(self,vol):
        
        self.speaker.setProperty('volume',vol)
        self.volumeTimes += 1
        
    def get_metric(self):
        
        print(f'Called Speak : {self.speakTimes} \nCalled Volume : {self.volumeTimes}')    
        
engine = TextToSpeech()
engine.set_volume(1)
engine.set_speed(150)

engine.speak("Nigger what the fuck dude are you fucking crazy")

engine.get_metric()


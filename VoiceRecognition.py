import speech_recognition as sr 
from gtts import gTTS
import playsound
import os


r = sr.Recognizer()
def voice_command_processor():
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=4)
        text = ''
        try:
            text=r.recognize_google(audio)
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print("Service Is Down")

        return text.lower()

def audio_playback(text):
    filename = "text.mp3"
    tts = gTTS(text=text,lang='en-us')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def execute_voice_command(text):
    if "what are you" in text:
        audio_playback("i am a i voice assistance system")

while True:
    command = voice_command_processor()
    print(command)
    execute_voice_command(command)
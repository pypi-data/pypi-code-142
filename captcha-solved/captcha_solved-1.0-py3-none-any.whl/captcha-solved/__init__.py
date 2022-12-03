import requests
import time
import os
from pydub import AudioSegment
import speech_recognition as sr
import uuid


def captcha(audio_url):
    doc = requests.get(audio_url)
    file_name = str(uuid.uuid4())
    with open(file_name + '.mp3', 'wb') as f:
        f.write(doc.content)
    time.sleep(10)
    sound = AudioSegment.from_mp3(file_name + '.mp3')
    sound.export(file_name + '.wav', format="wav")
    time.sleep(10)
    r = sr.Recognizer()
    with sr.AudioFile(file_name + '.wav') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
        except:
            pass
    mp3file = file_name + '.mp3'
    wavfile = file_name + '.wav'
    os.remove(mp3file)
    os.remove(wavfile)
    return text

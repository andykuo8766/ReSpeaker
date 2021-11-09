#!/usr/bin/python3
# -*- coding: utf8 -*-

import speech_recognition as sr
import tempfile
from gtts import gTTS
from pygame import mixer
import time

def speak(sentence, lang, loops=1):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(loops)



r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something: ")
    audio=r.listen(source)

print("Google Speech Recognition thinks you said: ")
speak("Google Speech Recognition thinks you said: ", 'en')
sent = r.recognize_google(audio, language="zh-TW")
speak(sent, 'zh-TW')
print("{}".format(sent))
time.sleep(10)
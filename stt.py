# -*- coding: utf8 -*-
import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something>>> ")
    audio=r.listen(source)

print("Google Speech Recognition thinks you said:")
sent = r.recognize_google(audio, language="zh-TW")
print("{}".format(sent))
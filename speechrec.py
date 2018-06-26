#!usr/bin/python3
import speech_recognition as sr
mic = sr.Microphone()
rec = sr.Recognizer()
with mic as source:
	audio = rec.record(source)

text = rec.recognize_google(audio)
print (text)





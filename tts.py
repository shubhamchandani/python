#!usr/bin/python3
from gtts import gTTS
import os
text = input("enter your text")
language = 'en'
myobj = gTTS(text=text, lang=language,slow = False)
myobj.save("audio.mp3")
os.system("espeak audio.mp3")


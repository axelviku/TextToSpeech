# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

tts=gTTS(text="Hello World",lang="en")
tts.save("hello.mp3")
os.system("start hello.mp3")

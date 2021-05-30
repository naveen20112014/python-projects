from gtts import gTTS
import os
speech=gTTS("Hello naveen, how are you?")
speech.save(r"C:\Users\BANDHAM\Desktop\Naveen_C\HELLO.mp3")
os.system(r"start C:\Users\BANDHAM\Desktop\Naveen_C\HELLO.mp3")
print('Program execution Completed')
print('Thank you')
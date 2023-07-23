from gtts import gTTS
from playsound import playsound

# text="asif bahut badmas hi"
text=input("enter your text")
s= gTTS(text)
s.save('myfile.mp3')
playsound('myfile.mp3')

  
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything to recongize ..  ")
    print("Listening...")
    audio = r.listen(source)
    print("Audio Processing...")
    try:
        outpuText = r.recognize_google(audio)
        print("You said : ", format(outpuText))
    except:
        print("Sorry..! Couldnt Recongize")

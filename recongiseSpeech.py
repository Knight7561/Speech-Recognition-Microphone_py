import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything ti recongize ..  ")
    audio = r.listen(source)
    try:
        outpuText = r.recognize_google(audio)
        print("You said : ", format(outpuText))
    except:
        print("Sorry..! Couldnt Recongize")

#voice recognition part
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice:")
    audio=r.listen(source)
    print ("ok done!!")

try:
    text=r.recognize_google(audio)
    print ("You said : "+text)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

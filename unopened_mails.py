unseen = mail.search(None, 'UnSeen') # unseen count
    print ("Number of UnSeen mails :"+str(unseen))
    tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    ttsname=("path/unseen.mp3") #Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

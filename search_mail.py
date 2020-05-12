result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    ttsname=("path/mail.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

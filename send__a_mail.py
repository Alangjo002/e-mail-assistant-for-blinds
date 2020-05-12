 mail = smtplib.SMTP('smtp.gmail.com',587)                                               #host and port area
    mail.ehlo()                                                                             #Hostname to send for this command defaults to the FQDN of the local host.
    mail.starttls()                                                                         #security connection
    mail.login('emailID','pswrd')                                                           #login section
    mail.sendmail('emailID','victimID',msg)                                                 #send section
    print ("Congrates! Your mail has been send. ")
    ts = gTTS(text="Congrates! Your mail has been send. ", lang='en')
    tsname=("path/send.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    mail.close()   
    
if int(text) == 2:
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)                                          #this is host and port area.... ssl security
    unm = ('your mail/ victim mail')                                                        #username
    psw = ('pswrd')                                                                         #password
    mail.login(unm,psw)                                                                     #login
    stat, total = mail.select('Inbox')                                                      #total number of mails in inbox
    print ("Number of mails in your inbox :"+str(total))
    ts = gTTS(text="Total mails are :"+str(total), lang='en')                              #voice out
    tsname=("path/total.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #unseen mails
    unseen = mail.search(None, 'UnSeen')                                                    # unseen count
    print ("Number of UnSeen mails :"+str(unseen))
    ts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    tsname=("path/unseen.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #search mails
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)')                                #fetch
    raw_email = email_data[0][1].decode("utf-8")                                            #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    ts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    tsname=("path/mail.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    #Body part of mails
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    ts = gTTS(text="Body: "+txt, lang='en')
    tsname=("path/body.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()
    mail.logout()

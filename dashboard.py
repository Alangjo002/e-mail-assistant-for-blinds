import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time

print ("-"*60)
print ("       Project: E-mail Assistant for Blinds")
print ("-"*60)

#project name
ts = gTTS(text="Project: E-mail assistant for blinds", lang='en')
tsname=("path/name.mp3")
ts.save(tsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

#login from os
login = os.getlogin
print ("You are logged In from : "+login())

#choices
print ("1. Composed a mail.")
ts = gTTS(text="option 1. Composed a mail.", lang='en')
tsname=("path/hello.mp3")
ts.save(tsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

print ("2. Check your inbox")
ts = gTTS(text="option 2. Check your inbox", lang='en')
tsname=("hello.mp3")
ts.save(tsname)

music = pyglet.media.load(ttsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)
#this is for input choices
ts = gTTS(text="Your choice ", lang='en')
tsname=("path/hello.mp3")
ts.save(ttsname)

music = pyglet.media.load(tsname, streaming = False)
music.play()

time.sleep(music.duration)
os.remove(tsname)

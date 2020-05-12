import pyttsx3

# One time initialization
engine = pyttsx3.init()

# Set properties _before_ you add things to say
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Queue up things to say.
# There will be a short break between each one
# when spoken, like a pause between sentences.
engine.say("The project is a python-based application for visually impaired persons using speech to text voice response, thus enabling everyone to control their mail accounts using their voice only and to be able to read,send, and perform all the other useful tasks. The system will prompt the user with voice commands to perform certain action and the user will respond to the same. The main benefit of this system is that the use of mouse is completely eliminated, the user will have to respond through voice only.")


# Flush the say() queue and play the audio
engine.runAndWait()

# Program will not continue execution until
# all speech is done talking

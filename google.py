import pywhatkit

command = input("search:")

if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
else:
        print("nothing")


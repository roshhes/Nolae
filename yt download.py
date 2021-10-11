import pywhatkit
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("900x500")
bg = PhotoImage(file ="E:/nolae/bg.PNG")


command = input("search:")

  
# Create Canvas
canvas1 = Canvas( root, width = 900,
                 height = 500)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
else:
        print("nothing")

root.mainloop()
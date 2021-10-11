from tkinter import *
from PIL import ImageTk,Image
from tkinter import *
from PIL import ImageTk,Image
from tkinter import Tk
import pygame
import os

root=Tk()
root.title('music')
root.iconbitmap('D:/nolae/n1.ico')
img= PhotoImage(file="D:/python/nolae/nol.gif")
imgl= Label(image=img)
def open():
    global my_img
    top=Toplevel()
    class MusicPlayer:
        def __init__(self,root):
            self.root = root
    # Title of the window
            top.self.root.title("Nolae")
    # WindowGeometry
            self.root.geometry("1000x600+200+200")
    # Initiating Pygame
            pygame.init()
    # Initiating Pygame Mixer
            pygame.mixer.init()
    # Declaring track Variable
            self.track = StringVar()
    # Declaring Status Variable
            self.status = StringVar()
  
    # Creating Track Frame for Song label & status label
            trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="black",fg="#eeb1b1",bd=5,relief=FLAT)
            trackframe.place(x=0,y=500,width=300,height=100)
    # Inserting Song Track Label
            songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",10),bg="#E59090",fg="black").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Status Label
            trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",10),bg="#E59090",fg="black").grid(row=0,column=1,padx=10,pady=5)

    # Creating Button Frame
            buttonframe = LabelFrame(self.root,text="",font=("times new roman",15,"bold"),bg="black",fg="black",bd=5,relief=FLAT)
            buttonframe.place(x=300,y=500,width=700,height=100)
    # Inserting Play Button
            playbtn = Button(buttonframe,text="▶",command=self.playsong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=FLAT).grid(row=0,column=3,padx=15,pady=15)
    # Inserting Pause Button
            playbtn = Button(buttonframe,text="⏸",command=self.pausesong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=FLAT).grid(row=0,column=5,padx=15,pady=15)
    # Inserting Unpause Button
            playbtn = Button(buttonframe,text="⏯",command=self.unpausesong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=FLAT).grid(row=0,column=7,padx=15,pady=15)
    # Inserting Stop Button
            playbtn = Button(buttonframe,text="⏹",command=self.stopsong,width=2,height=1,font=("times new roman",16,"bold"),fg="white",bg="black",relief=FLAT).grid(row=0,column=9,padx=15,pady=15)
    # Inserting Next Button

    # Creating Playlist Frame
            songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="#eeb1b1",fg="black",bd=5,relief=FLAT)
            songsframe.place(x=0,y=0,width=1000,height=500)
    # Inserting scrollbar
            scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
            self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="pink",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="#ffe9e9",fg="BLACK",bd=2,relief=FLAT)
    # Applying Scrollbar to listbox
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=self.playlist.xview)
            self.playlist.pack(fill=BOTH)
    # Changing Directory for fetching Songs
            os.chdir("Music")
    # Fetching Songs
            songtracks = os.listdir()
    # Inserting Songs into Playlist
            for track in songtracks:
                self.playlist.insert(END,track)

  # Defining Play Song Function
            def playsong(self):
    # Displaying Selected Song title
                    self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
                    self.status.set("-Playing")
    # Loading Selected Song
                    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
                    pygame.mixer.music.play()

            def stopsong(self):
    # Displaying Status
                    self.status.set("-Stopped")
    # Stopped Song
                    pygame.mixer.music.stop()

            def pausesong(self):
    # Displaying Status
                    self.status.set("-Paused")
    # Paused Song
                    pygame.mixer.music.pause()

            def unpausesong(self):
    # Displaying Status
                    self.status.set("-Playing")
    # Playing back Song
                    pygame.mixer.music.unpause()
    MusicPlayer(root)      
btn=Button(root,text="playlist", command=open).pack()
root = Tk()
# Passing Root to MusicPlayer Class


# Root Window Looping
root.mainloop()

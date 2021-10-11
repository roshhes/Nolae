from tkinter import *
from tkinter import Tk
root = Tk()


img= PhotoImage(file="D:/nolae/BTS.gif")
imgl= Label(image=img)
playbtn=Button(root,image=img,command='self.playsong;' , borderwidth=0)
playbtn.pack(pady=20)

lbl=Label(root,text='')
lbl.pack(pady=20)
def playsong(root):
    print("hello")


root.mainloop()
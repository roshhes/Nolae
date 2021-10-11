from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('music')
root.iconbitmap("D:/nolae/n1.ico")

def open():
    global my_img
    top=Toplevel()
    top.title("playlist")
    my_img=ImageTk.Photoimage(Image.open("nolae/n1.ico"))
    my_label=Label(top, image=my_img).pack()
    btn=Button(top,text="back to home",command=top.destroy).pack()

btn=Button(root,text="playlist", command=open).pack()

mainloop()

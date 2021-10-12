
from tkinter import *
#to create a window
root = Tk()

#root window is the parent window
fram = Frame(root)

#adding label to search box
Label(fram,text='search on youtube').pack(side=LEFT)

#adding of single line text box
entry= Entry(fram)

#positioning of text box
entry.pack(side=LEFT, fill=BOTH, expand=1)


#setting focus
entry.focus_set()

#adding of search button
butt = Button(fram, text='done')
butt.pack(side=RIGHT)
fram.pack(side=TOP)
root.mainloop()

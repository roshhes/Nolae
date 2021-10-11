# Import module 
from tkinter import *
from PIL import ImageTk,Image
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("900x500")
  
# Add image file
bg = PhotoImage(file ="E:/nolae/bg.PNG")
  
# Create Canvas
canvas1 = Canvas( root, width = 400,
                 height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
  

# Execute tkinter
root.mainloop()
# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *

# Creating master Tkinter window
master = Tk()
master.title('face detection')
master.geometry("250x140")

# Tkinter string variable
# able to store any string value
v = IntVar()
v.set("0")

# Dictionary to create multiple buttons
values = {"click photo" : "1",
         "capture video" : "2",
         "upload photo" : "3",
         "upload video" : "4",
         }

def clicked():
   option = Label(master, text=value)
   return option

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
   Radiobutton(master, text = text, variable = v,
            value = value,command=lambda:clicked(v.get()), indicator = 0,
            background = "light blue").pack(fill = X, ipady = 4)

option = Label(master, text=v.get())
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()


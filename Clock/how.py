from tkinter import *

root = Tk()
var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)

var.set("Good Morning! How are you doing?")
label.pack()
root.mainloop()
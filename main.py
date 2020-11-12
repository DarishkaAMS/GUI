from tkinter import *
from tkinter.ttk import *
from time import strftime

ROOT = Tk()
ROOT.title("My first clock")


def time():
    time_str = strftime('%H:%M:%S %p')
    label.config(text=time_str)
    label.after(1000, time) # 1 sec


label = Label(ROOT, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()
mainloop() # to run the Tkinter event loop.

import pyautogui
import tkinter as tk
from tkinter.filedialog import *

ROOT = tk.Tk()

basic_canvas = tk.Canvas(ROOT, width=300, heigh=300)
basic_canvas.pack()


def take_screenshot():
    my_screenshot = pyautogui.screenshot()
    save_path = asksaveasfile()
    my_screenshot.save(save_path + "_screenshot.png")


screenshot_btn = tk.Button(text="Take Screenshot", command=take_screenshot, font=10)
basic_canvas.create_window(150, 150, window=screenshot_btn)
ROOT.mainloop()

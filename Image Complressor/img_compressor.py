import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = PIL.Image.open(file_path)
my_height, my_width = img.size

img = img.resize((my_height, my_width), PIL.Image.ANTIALIAS)
save_path = asksaveasfile()

img.save(save_path + "_compressed.JPG")
# 434 KB (444,487 bytes)


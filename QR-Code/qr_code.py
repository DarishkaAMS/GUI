import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr_code = pyqrcode.create("Life is Amazing")
qr_code.png("my_first_qr.png", scale=8)

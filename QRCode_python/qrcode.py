import pyqrcode
import png
from pyqrcode import QRCode

frase = str(input("Digite uma frase para transformar em QrCode: "))

# transforma em Qrcode #
qr = pyqrcode.create(frase)
# Salva o qrcode #
qr.png(r'qr.png', scale=8)
import pyqrcode
import png

def qrcode(data):
    q=pyqrcode.create(data)
    q.png('QR Code.png',scale=6)
    print('QR Code Generated!')
    
data ="https://youtu.be/fHBR1j1kJ1I?si=VEHcM2zAwdHNIF3_"
qrcode(data)

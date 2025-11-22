import qrcode

data = "Bang test"
img = qrcode.make(data)
img.save("qr.png")
print("QR code save as qr.png")
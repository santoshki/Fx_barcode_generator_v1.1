import cv2
from pyzbar.pyzbar import decode

def BarcodeReader(image):
    print("barcode reading function.", image)
    image = str(image) + ".png"
    img = cv2.imread(image)
    detectedBarcodes = decode(img)

    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        for barcode in detectedBarcodes:
            if barcode.data != "":
               barcode_value = barcode.data.decode("utf-8")
               print("Scanned barcode value:", barcode_value)
        return barcode_value


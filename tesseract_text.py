import os
import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_from_file(file_path):
    text = pytesseract.image_to_string(Image.open(file_path))
    return text

print(extract_from_file("./temp/inverted_img.jpg"))


"""
D. Brawn Manufacture     

Invoice no. DVT-AX-345678

Payment date: 03/12/2006 

Reference Designation Qty Unit price Total CHF Sales
Work
SERVICE D COMPLETE OVERHAUL 1 5500.00 5500.00 220
SERVICE D REFRESHING COMPLETE CASE 1 380.00 380.00 220
AND RHODIUM BATH
Exterior parts:
JO.297.065.FP FLAT GASKET 1 3.00 3.00 220
JO.197.075.FP FLAT GASKET 1 4.00 4.00 220
JO.199.059.0S FLAT ROUND GASKET 1 6.00 6.00 220
VI.261.036.BC W.G.FIXATION SCREWS 10 4.00 40.00 220
Al.465.055.BC WHITE GOLD "FOIL" 1 70.00 70.00 220
PAIR OF HAND
LENGTH: 10/13.50MM
CALIBRE 2868
SPECIAL DISCOUNT -3003.00 -3003.00
Discount -900.00 -900.00
Total CHF 2100.00
RETURN AFTER REPAIR
NO COMMERCIAL VALUE
Payment:
Mr. John Doe

Green Street 15, Office 4

1234 Vermut

New Caledonia

Credit Card: Visa
Card No: 112345678
"""
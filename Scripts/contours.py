import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('../temp/bw_image.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)

n_boxes = len(d['level'])
for i in range(n_boxes):
    if d['conf'][i] != '-1':
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 900, 1080)  # Set your desired width and height
cv2.imshow('img', img)
cv2.waitKey(0)
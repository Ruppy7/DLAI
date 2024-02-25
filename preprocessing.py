import cv2
from PIL import Image

image_file = './Samples/sample4.jpg'
img = cv2.imread(image_file)

#INVERT AN IMAGE, WHITE TO BLACK AND BLACK TO WHITE
#inverted_img = cv2.bitwise_not(img)
#cv2.imwrite('temp/inverted_img_sample4.jpg', inverted_img)


# BINARIZATION (THRESHOLDING)
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv2.imwrite('temp/grayscale_img_sample4.jpg', gray_image)

thresh, im_bw = cv2.threshold(gray_image, 100, 150, cv2.THRESH_BINARY)
cv2.imwrite('temp/bw_image_sample4.jpg', im_bw)


# cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('img', 800, 1080)
# cv2.imshow('img', img,)
# cv2.waitKey(0)
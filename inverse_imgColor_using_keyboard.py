import sys
import cv2
import numpy as np

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image load failed")
    sys.exit()

cv2.namedWindow("image")
cv2.imshow("image", img)

while True:
    key = cv2.waitKey()
    if key == 27:
        break

    # if 'i' or 'I' is pressed, inversed color will be applied to the img file
    elif key == ord('i') or key == ord("I"):
        img = ~img
        cv2.imshow("image", img)

cv2.destroyAllWindows()
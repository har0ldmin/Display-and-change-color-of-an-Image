import sys
import cv2


print("Hello OpenCV2, ", cv2.__version__)

# Load img
img = cv2.imread("japan.tiff")

if img is None:
    print("Upload failed..")
    sys.exit()


cv2.namedWindow("Image")
cv2.imshow("Image", img)

# Escape
while True:
    key = cv2.waitKey()
    if cv2.waitKey() == ord("q"):
        break

cv2.destroyAllWindows()

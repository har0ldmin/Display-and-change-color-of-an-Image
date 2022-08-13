import sys
import glob
import cv2


# Load image using glob.glob()
img_files = glob.glob("./images/*.jpg")

for f in img_files:
    print(f)

# Display an image on a full sized screen
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Infinite Loop
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])
    cv2.imshow("image", img)

    # Escape method 1)
    '''if cv2.waitKey(1500) >= 0:   # ESC > 0
        break'''

    # Escape method 2)
    if cv2.waitKey(1500) == ord("q"):
        break
    
    # Rotates the images in img_files
    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
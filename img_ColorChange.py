import os
import sys
import cv2

print("Hello OpenCV2, ", cv2.__version__)

# Load img and set it to grey 
img = cv2.imread("japan.tiff", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Upload failed..")
    sys.exit()


# Method 1
cv2.imwrite("japan_grey.tiff", img)


# Method 2
''' imwrite() has the ability to compress the image while writing it into the file. 
Control JPEG image quality in cv2.imwrite() with cv2.IMWRITE_JPEG_QUALITY '''
cv2.imwrite("japan_grey.jpeg", img, [cv2.IMWRITE_JPEG_QUALITY, 70])


# Method 3_ Change path
# Set path
# path = "   "
# cv2.imwrite(os.path.join(path , "japan_grey.tiff"), img)


# file size checker function
def print_file_size(file):
    file_Size = os.path.getsize(file)
    file_Size_MB = round(file_Size/1024/1024,2)
    print("Image File Size is " + str(file_Size_MB) + "MB" )

print_file_size("japan_grey.tiff")
print_file_size("japan_grey.jpeg")

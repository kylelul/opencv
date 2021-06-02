import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt


img = cv.imread("30.jpeg")
cv.imshow('cat',img)

# plt.imshow(img)
# plt.show()        # in opencv image is BGR, matplotlib display it with RGB so cause different color

# 1. BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2. BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# 3. BGR to LAB
LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', LAB)

# 4. BGR to RGB
RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',RGB)
# plt.imshow(RGB)
# plt.show()      #now opencv display rgb image with bgr, matplot display rgb with rgb

# 5. HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsvbgr',hsv_bgr)



cv.waitKey(0)
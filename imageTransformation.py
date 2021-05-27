import cv2 as cv
import numpy as np 

img = cv.imread("30.jpeg")

cv.imshow('cat',img)

# 1. Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img,100,100)
cv.imshow("translated",translated)

# 2. Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions=(width, height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,30)
cv.imshow("rotated",rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow("rotatedrotated", rotated_rotated)    # by this you will see the black area rotated 
                                                # together as part of previous image


# 3. Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

# 4. Flipping
flip = cv.flip(img,-1)
cv.imshow("flip",flip)








cv.waitKey(0)
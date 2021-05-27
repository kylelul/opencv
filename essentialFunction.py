import cv2 as cv

img = cv.imread("30.jpeg")
cv.imshow("cat",img)

# 1. Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2. Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)

# 3. Edge Cascade(Canny)
# canny = cv.Canny(img,125,175)
canny = cv.Canny(blur,125,175) # Blurry image's canny edge can be more clean
cv.imshow("canny", canny)

# 4. Dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("dilated", dilated)

# 5. Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("eroded",eroded)

# 6. resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

# 7. Cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)
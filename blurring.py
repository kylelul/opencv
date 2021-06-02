import cv2 as cv

img = cv.imread('30.jpeg')
cv.imshow('cat',img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow('averageblur',average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussianblur',gauss)

# Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Medianblur',median)

# Bilateral
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral', bilateral)



cv.waitKey(0)
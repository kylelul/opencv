import cv2 as cv 
import numpy as np 

img = cv.imread('30.jpeg')
cv.imshow('cat',img)
blank = np.zeros(img.shape[:2],dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)

merged = cv.merge([b,g,r])
cv.imshow("Merged Image",merged)

print(f'merged',merged.shape)

cv.waitKey(0)

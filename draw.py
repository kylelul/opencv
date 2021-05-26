import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('blank',blank)

# 1. Paint the Image a certain color
# blank[200:400,300:400] = 0,255,0
# cv.imshow('Green',blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0),(blank.shape[1]//2,blank.shape[0]//3),(0,255,0), thickness=-1)
cv.imshow("rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//3),40,(0,0,255),thickness=3)
cv.imshow("Circle",blank)

# 4. Draw a line
cv.line(blank, (400,400), (200,200),(0,255,0),thickness=5)
cv.imshow("line",blank)

# 5. Write text
cv.putText(blank,"hello", (225,225),cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow("text",blank)


cv.waitKey(0)

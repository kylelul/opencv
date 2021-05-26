import cv2 as cv
from matplotlib import pyplot as plt


def rescaleFrame(frame, scale=0.75):
    # Works for img/video/live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
 
# def changeRes(width, height):
#     # Live video only
#     capture.set(3,width)
#     capture.set(4,height)


# load video
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read() 
    frame_resized = rescaleFrame(frame)
    # frame_changeres = changeRes(width=200,height=100)
    cv.imshow('Video',frame)
    cv.imshow('VideoResize', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
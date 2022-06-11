import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype = 'uint8') #unit8 is basiccally an image. creating a blank photo

cv.imshow('Blank', blank)
# img = cv.imread(r"C:\Users\ibner\MyLearning\Opencv\Resources\Photos\cat.jpg")
# cv.imshow('Cat', img)


#paint image in certain color
# blank[:] = 0, 255, 0 #its green
# cv.imshow('Green', blank)

#color certain portions 

# blank[200:300, 300:400] = 0, 255, 0 
# cv.imshow('Certain Portion', blank)

# #Draw rectanle
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)


# #Draw circle similarly for line cv.line

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//22), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

#text

cv.putText(blank, 'Hello my name is adil', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)
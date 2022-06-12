import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"C:\Users\ibner\MyLearning\Opencv\Resources\Photos\park.jpg")
cv.imshow('park', img)

#BGR to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

#BGR to hsv
#how human see and conceive colors
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# # BGR to L*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# # BGR to RGB
# matplotlib display as rgb as inversion
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# # HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

# cv.waitKey(0)

cv.waitKey(0)
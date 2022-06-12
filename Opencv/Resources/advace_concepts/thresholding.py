import cv2 as cv
from cv2 import threshold

img =  cv.imread(r"C:\Users\ibner\OneDrive\Desktop\new desktop\opencv2\opencv-course\Resources\Photos\cats.jpg")
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
#at 155 threshold ,it wiill enccounter will change to 255
cv.imshow('Simple thresholded',thresh )

#inverse
threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)

#adaptive find optimum threshold value
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,
11, 3)
cv.imshow('Adaptive thresh', adaptive_thresh)




cv.waitKey(0)
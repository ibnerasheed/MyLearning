import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\ibner\MyLearning\Opencv\Resources\Photos\park.jpg")
cv.imshow('park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')



b, g ,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g,  blank])
red = cv.merge([blank, blank, r])

cv.imshow('Green', green)
cv.imshow('Red', red)
cv.imshow('Blue',blue)

# cv.imshow('Green', g)
# cv.imshow('Red', r)
# cv.imshow('Blue',b)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)





cv.waitKey(0)
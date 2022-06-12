

import cv2 as cv

img = cv.imread(r"C:\Users\ibner\MyLearning\Opencv\Resources\Photos\cats.jpg")
cv.imshow('cats', img)

# Averaging the first method of blurring
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur,less blurr than avg but more natural
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
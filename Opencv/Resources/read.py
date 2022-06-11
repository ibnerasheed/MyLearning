import cv2 as cv
from sympy import capture

#img = cv.imread(r"C:\Users\ibner\MyLearning\Opencv\Resources\Photos\cat_large.jpg")
#cv.imshow('cat', img)

#reading videos

capture = cv.VideoCapture(r"C:\Users\ibner\MyLearning\Opencv\Resources\Videos\dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
#cv.waitKey(0)
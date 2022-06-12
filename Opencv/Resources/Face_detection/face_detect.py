import cv2 as cv

img = cv.imread(r"C:\Users\ibner\Downloads\testimg.jpeg")
cv.imshow('class', img)

#uses edges to detect images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
cv.imshow('Gray Image', gray)

haar_cascade = cv.CascadeClassifier(r'C:\Users\ibner\MyLearning\Opencv\Resources\Face_detection\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors =  1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)





cv.waitKey(0)
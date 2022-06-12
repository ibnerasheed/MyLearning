import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier(r'C:\Users\ibner\MyLearning\Opencv\Resources\Face_detection\haar_face.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load(r'C:\Users\ibner\MyLearning\Opencv\Resources\Face_detection\features.npy', allow_pickle = True)
# labels = np.load(r'C:\Users\ibner\MyLearning\Opencv\Resources\Face_detection\labels.npy', allow_pickle = True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\ibner\MyLearning\Opencv\Resources\Face_detection\face_trained.yml')

img = cv.imread(r"C:\Users\ibner\MyLearning\Opencv\Resources\Faces\val\ben_afflek\2.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#detect face

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)
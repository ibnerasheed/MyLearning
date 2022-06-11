import cv2 as cv

def changeRes(width, height):
    #only for live video
    capture.set(3, width)
    capture.set(4, height)




def rescaleFrame(frame,  scale = 0.75):
    #images, videos, livevide
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)



capture = cv.VideoCapture(r"C:\Users\ibner\MyLearning\Opencv\Resources\Videos\dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, scale = 0.25)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
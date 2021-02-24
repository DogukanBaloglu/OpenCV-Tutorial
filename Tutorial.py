### pip install opencv-contrib-python
### pip install caer
import cv2 as cv

# Ölçekleme
def rescaleFrame(frame, scale=0.75): #for images videos and live video
   width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width,height)
  return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
def changesRes(width,height): # Just for live video
    capture.set(3,width)
    capture.set(4,height)

##Fotoğraf Okuma
img = cv.imread("Photos/cat2.jpeg")
cv.imshow("Kedi", img)
cv.waitKey(0)

##Video Okuma
capture =cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized= rescaleFrame(frame, scale=1.2)
    cv.imshow("Dog_Video", frame)
    cv.imshow("Resized_video",frame_resized)
    if cv.waitKey(20) & 0xFF==ord("d"):
      break
capture.release()
cv.destroyWindow()



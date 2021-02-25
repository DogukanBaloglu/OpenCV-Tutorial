import cv2 as cv
import numpy as np

img =cv.imread("Photos/Cat.jpeg")
cv.imshow("cat", img)

#Translation
def translate(img, x, y):
    tranMat= np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0]) #shape[1] =width, shape[0] =height
    return cv.warpAffine(img, tranMat, dimensions)
# -x --> left
# -y --> up
# x --> right
# y --> down

translated=translate(img, -50, -50)
cv.imshow("Translated", translated)

#Rotation
def rotate(img, angle ,rotPoint=None):
    (height,width)= img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated=rotate(img, 45) # can be negative angle
cv.imshow("rot",rotated)

#Resizing
resized =cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#Flipping
flipped=cv.flip(img,-1) # Can be -1,0,1
cv.imshow("Flipped",flipped)

#Cropping
cropped =img[50:100,20:150]
cv.imshow("cropped", cropped)

cv.waitKey(0)
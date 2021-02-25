import cv2 as cv
import numpy as np

img =cv.imread("Photos/Cat.jpeg")
cv.imshow("cat", img)

blank=np.zeros(img.shape, dtype="uint8")
cv.imshow("blak",blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

canny=cv.Canny(img,125,175)
cv.imshow("canny",canny)

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
canny=cv.Canny(blur,125,175)
cv.imshow("canny",canny)

contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

ret,thresh =cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)

contours,hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank,contours,-1,(255,0,0), 1)
cv.imshow("Counters Draw", blank)


cv.waitKey(0)
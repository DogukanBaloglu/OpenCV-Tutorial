import cv2 as cv
import numpy as np

img =cv.imread("Photos/Cat.jpeg")
cv.imshow("cat", img)

#Averaging
average = cv.blur(img,(3,3)) #(a,a) kernel size
cv.imshow("Average", average)

#Gaussian Blur
gaussian= cv.GaussianBlur(img,(3,3),0)
cv.imshow("gaussian", gaussian)

#Median Blur
meadian =cv.medianBlur(img, 3)
cv.imshow("median", meadian)

#Bilateral Blur
bilateral =cv.bilateralFilter(img, 10, 25, 25)
cv.imshow("bilateral",bilateral)

cv.waitKey(0)
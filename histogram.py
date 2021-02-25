import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img =cv.imread("Photos/cat2.jpeg")
cv.imshow("cat", img)

blank=np.zeros(img.shape[:2], dtype="uint8")

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask =cv.bitwise_and(gray,gray, mask=circle)
cv.imshow("mask",mask)

#Grayscale hist
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title("Gray Scale Hist")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
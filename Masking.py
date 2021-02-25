import cv2 as cv
import numpy as np

img =cv.imread("Photos/Cat.jpeg")
cv.imshow("cat", img)

blank=np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2-30), 50, 255, -1)
cv.imshow("Circle",circle)

rectangle =cv.rectangle(blank.copy(), (30,30), (200,200), 255, -1)

shape = cv.bitwise_and(rectangle,circle)


masked = cv.bitwise_and(img,img,mask=circle)
cv.imshow("Masked",masked)

masked_2 = cv.bitwise_and(img,img,mask=shape)
cv.imshow("Masked_2",masked_2)


cv.waitKey(0)
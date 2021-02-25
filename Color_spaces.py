import cv2 as cv
import matplotlib.pyplot as plt


img =cv.imread("Photos/Cat.jpeg")
cv.imshow("cat", img)

#BGR to gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#BGR to HSV
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

#BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow("lab", lab)

plt.imshow(img)
plt.show()

#BGR to RGB
rgb =cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

plt.imshow(rgb)
plt.show()

#HSV to bgr
hsv_bgr= cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("hsv_bgr",hsv_bgr)

#LAB to BGR
lab_bgr= cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("lab_bgr",lab_bgr)


cv.waitKey(0)

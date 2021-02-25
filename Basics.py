import cv2 as cv
img = cv.imread("Photos/Cat.jpeg")
cv.imshow("Cat", img )

#Converting greyscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#blur
blur =cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT) #(3,3),(5,5),(7,7) -< blur level
cv.imshow("blur", blur )

#Edge Cascade
#canny =cv.Canny(img, 125,175)
#cv.imshow("Canny Edges", canny)

canny =cv.Canny(blur, 125,175)
cv.imshow("Canny Edges", canny)

#Dilating the image
dilated= cv.dilate(canny ,(7,7), iterations=3 )
cv.imshow("dilated", dilated)

#Eroding
eroded=cv.erode(dilated, (7,7), iterations=3)
cv.imshow("eroded",eroded)

#Resize
resize=cv.resize(img,(800,500),interpolation=cv.INTER_AREA)
cv.imshow("resize",resize)

#Cropping
cropped=img[50:200,200:400]
cv.imshow("cropped",cropped)


cv.waitKey(0)
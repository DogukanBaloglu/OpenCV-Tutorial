import cv2 as cv
import numpy as np

img =cv.imread("Photos/Cat.jpeg")
cv.imshow("cat", img)

blank=np.zeros(img.shape[:2], dtype="uint8")

b,g,r=cv.split(img)
cv.imshow("b",b) # mavi yoğunluklu bölgeler daha beyaz içinde içermeyen yeerler siyaha yakın
cv.imshow("g",g) # yeşil yoğunluklu bölgeler daha beyaz içinde içermeyen yeerler siyaha yakın
cv.imshow("r",r) # kırmızı yoğunluklu bölgeler daha beyaz içinde içermeyen yeerler siyaha yakın

print(img.shape) #(168, 300, 3)
print(b.shape) # (168, 300)
print(g.shape) # (168, 300)
print(r.shape) # (168, 300)

merged =cv.merge([b,g,r])
cv.imshow("merged", merged)

blue = cv.merge([b,blank,blank])
green= cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

cv.waitKey(0)
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype="uint8")
#cv.imshow("Blank",blank)
#img = cv.imread("Photos/cat2.jpeg")
#cv.imshow("Kedi", img)

#blank[0:300, 0:200] =0,255,0
#cv.imshow("Blank",blank)

#cv.rectangle(blank, (10,10), (100,150), (255,0,0), thickness=3) # cv.rectangle(blank,size_of_shape,color,çizgi_kalınlığı) BGR
#cv.rectangle(blank, (10,10), (100,150), (255,0,0), thickness=cv.FILLED) -> içini dolduruyor ya da "-1" vererek de elde edilebilir.
#cv.imshow("Rec",blank)

#cv.circle(blank,(250,250),40,(0,0,255),thickness=2)
#cv.imshow("Circle",blank)

#cv.line(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness=3 ) #0,0 dan başlayıp tam ortaya kadar giden çizgi
#cv.imshow("line", blank)

cv.putText(blank, "Dogukan", (100,200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255),2)
cv.imshow("text", blank)


cv.waitKey(0)
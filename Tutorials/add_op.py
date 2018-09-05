import cv2
import numpy as np

img1 = cv2.imread('Albert.jpg')
img2 = cv2.imread('download.jpg')

img3 = img1 + img2
#in img3, if(201,50,100) + (200,20,155) = (255,70,255) as max is 255.
img4 = cv2.add(img1,img2)
img5 = cv2.addWeighted(img1,0.6,img2,0.4,0)

cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.imshow('img5',img5)

cv2.waitKey(0)
cv2.destroyAllWindows()



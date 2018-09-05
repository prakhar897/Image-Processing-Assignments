import cv2
import numpy as np


img1 = cv2.imread('Albert.jpg')
img2 = cv2.imread('moon.jpg')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,100,255,cv2.THRESH_BINARY_INV)
#what does ret do?

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)
#why two same arguments


dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst


#cv2.imshow('roi',roi)
cv2.imshow('mask',img1_bg)
cv2.imshow('roi',img2_fg)
cv2.imshow('img2',img2)
cv2.imshow('img1',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()

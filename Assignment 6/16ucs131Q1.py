import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('moon.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)

BLACK =[0,0,0]

img2 = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_CONSTANT,value=BLACK)
cv2.imshow('padimage',img2)

height,width = img2.shape[:2]
tx = 200
ty = 175
T = np.float32([[1,0,tx],
    [0,1,ty]])

f_img = cv2.warpAffine(img2,T,(width,height))

cv2.imshow('Final Image',f_img)
cv2.imwrite('fimage.jpg',f_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

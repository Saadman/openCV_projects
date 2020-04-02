import numpy as np
import cv2
import random

img = cv2.imread("images/LobularCarcinoma.jpg",1)
cv2.imshow("Fuzzy",img)

##img2=cv2.imread("fuzzy.png",0)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("B&W",img2)


#blurring the image

blur=cv2.GaussianBlur(img2,(3,3),0)
cv2.imshow("Blur",blur)

thresh=85

ret,threshold=cv2.threshold(blur,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold",threshold) #simple thresholding seems to do a better job at segmenting

adapt_thresh=cv2.adaptiveThreshold(blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,155,1)

cv2.imshow("Threshold_adaptive",adapt_thresh)

contours, hierarchy = cv2.findContours(adapt_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


img3=blur.copy()
index=-1
thickness=4
color=(255,0,230)

cv2.drawContours(img3,contours,index,color,thickness)
cv2.imshow("Contours",img3)

#Get area of contours

objects=np.zeros([img.shape[0],img.shape[1],3],'uint8')

for c in contours:
	area=cv2.contourArea(c)
	
	if area>=1000:
		print(area)
		cv2.drawContours(objects,[c],-1,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),-1)

	

cv2.imshow("area",objects)
cv2.waitKey(0)
cv2.destroyAllWindows()
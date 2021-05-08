import cv2,numpy as np

img=cv2.imread("Black.jpg",0)
img=np.zeros((512,512,3),np.uint8)
cv2.circle(img,(256,256),100,(255,255,0),-1)
cv2.circle(img,(256,256),80,(0,255,255),-1)
cv2.circle(img,(256,256),60,(0,255,0),-1)



cv2.imshow("new window",img)
cv2.waitKey(0)
cv2.destroyWindow("new window")

import cv2,numpy as np

img=np.zeros((512,512,3),np.uint8)
img[np.where((img==[0,0,0]).all(axis=2))]=[0,255,255]
text=" THANK YOU"
cv2.putText(img,text,(10,250),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
cv2.imshow("text",img)
cv2.waitKey(0)
cv2.destroyWindow("text")
cv2.imwrite("black.jpg",img)


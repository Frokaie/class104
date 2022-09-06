import cv2


img=cv2.imread("PRO-104-OpenCV-Image-Assets-main/butterfly.jpg")
cv2.imshow("Display Image",img)
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale",grey_img)
cv2.waitKey(5000)
#print(img)
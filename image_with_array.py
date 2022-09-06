import numpy as np
import cv2

black=np.zeros([600,600])
#print(black)
#cv2.imshow("black",black)

f_row=black[1:2]
#print(f_row)

f_col=black[:,1:2]
#print(f_col)

black[200:400,200:400]=50
cv2.imshow("black",black)
print(black)

cv2.waitKey(1000)
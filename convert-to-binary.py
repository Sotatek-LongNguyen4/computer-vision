
import numpy as np
import cv2

image = cv2.imread("pic1.jpg")
cv2.imshow("color image", image)
cv2.waitKey(0)

#convert to gray image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#threshold
ret,threshold_binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("threshold", threshold_binary)
cv2.waitKey()
cv2.destroyAllWindows()
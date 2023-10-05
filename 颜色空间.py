import cv2
import numpy as np
img = cv2.imread('curry.jpeg')
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#获取BGR像素对应的HSV值
blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)
lower_blue = hsv_blue - np.array([[[50, 100, 100]]])
upper_blue = hsv_blue - np.array([[[-50, 0, 0]]])

mask = cv2.inRange(img, lower_blue, upper_blue)
img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
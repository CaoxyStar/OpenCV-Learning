import time
import cv2

img = cv2.imread('1.jpg')
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
e1 = cv2.getTickCount()
time_1 = time.time()
for i in range(5, 49, 2):
    img = cv2.medianBlur(img, i)
    cv2.imshow('img', img)
e2 = cv2.getTickCount()
time_2 = time.time()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)
print(time_2 - time_1)
print(cv2.useOptimized())
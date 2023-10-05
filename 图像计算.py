import cv2
import numpy as np

img1 = cv2.imread('1.jpg')
img1 = cv2.resize(img1, (960, 480))
img2 = cv2.imread('curry.jpeg')
img2 = cv2.resize(img2, (960, 480))
cv2.namedWindow('img1', cv2.WINDOW_NORMAL)
cv2.namedWindow('img2', cv2.WINDOW_NORMAL)
cv2.namedWindow('mixed', cv2.WINDOW_NORMAL)
mixed = cv2.addWeighted(img1, 1, img2, 0.2, -50)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('mixed', mixed)
cv2.waitKey(0)
cv2.destroyAllWindows()
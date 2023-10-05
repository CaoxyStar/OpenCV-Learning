import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('opencv.jpeg')
img2 = cv2.imread('1.jpg')
print(img1.shape)
rows, cols, channels = img1.shape
roi = img2[0:rows, 0:cols]
plt.subplot(231)
plt.imshow(img1)
plt.title('img')

img2gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
plt.subplot(232)
plt.imshow(mask, 'gray')
plt.title('mask')

mask_inv = cv2.bitwise_not(mask)
plt.subplot(233)
plt.imshow(mask_inv, 'gray')
plt.title('mask_inv')

img2_bg = cv2.bitwise_and(roi, roi, mask=mask)
plt.subplot(234)
plt.imshow(img2_bg)
plt.title('img2_bg')
print(mask_inv)

img1_bg = cv2.bitwise_and(img1, img1, mask=mask_inv)
plt.subplot(235)
plt.imshow(img1_bg)
plt.title('img1_bg')

dst = cv2.add(img1_bg, img2_bg)
plt.subplot(236)
plt.imshow(dst)
plt.title('dst')
plt.show()

img2[0:rows, 0:cols] = dst
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.imshow('result', img2)
cv2.imwrite('mixed.jpg', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

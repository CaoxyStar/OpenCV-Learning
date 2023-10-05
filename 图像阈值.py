import cv2
from matplotlib import pyplot as plt

img = cv2.imread('12.jpg', 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)      #低于阈值设为0， 高于不变
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  #高于阈值设为0， 低于则不变
ret, thresh3 = cv2.threshold(img, 127, 200, cv2.THRESH_TRUNC)   #高于阈值设为阈值，低于则不变
plt.subplot(2, 2, 1)
plt.imshow(img, "gray")
plt.title('img')
plt.subplot(2, 2, 2)
plt.imshow(thresh1, "gray")
plt.title("change")
plt.subplot(2, 2, 3)
plt.imshow(thresh2, "gray")
plt.title("change")
plt.subplot(2, 2, 4)
plt.imshow(thresh3, "gray")
plt.title("TRUNC")
plt.show()
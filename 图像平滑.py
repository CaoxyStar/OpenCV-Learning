import cv2
from matplotlib import pyplot as plt
import  numpy as np

img = cv2.imread('12.jpg')
dst = cv2.GaussianBlur(img, (51, 51), 0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

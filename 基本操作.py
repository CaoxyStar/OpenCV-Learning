import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('1.jpg', 1)
b, g, r = cv2.split(img)           #BGR 012
img_update = cv2.merge((b, g, g))
car = img[900:1050, 200:420]    #先height后width
img[200:350, 100:320] = car
replicate = cv2.copyMakeBorder(img, 100, 100, 10, 10, cv2.BORDER_CONSTANT, value = (255, 255, 0))

print(img.shape)
plt.subplot(231)
plt.imshow(replicate, 'gray')
plt.title('replicate')
plt.show()
'''
print(img.item(10, 10, 2))      #使用item加快访问修改速度
img.itemset((10, 10, 2), 255)
print(img.item(10, 10, 2))
print(img.shape)
print(img.size)
print(img.shape[0]*img.shape[1])
print(img.dtype)
200 900 420 1050
'''


'''
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img_update)
# cv2.imwrite('img_bgg.jpg', img_update)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



